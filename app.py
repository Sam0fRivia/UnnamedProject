import streamlit as st
from math import radians, cos, sin, sqrt, atan2

from llm import ask_vet_ai, triage_symptoms
from data import get_vets

st.set_page_config(page_title="VetConnect AI", layout="centered")

for k, v in {"page": "chat", "chat_history": [], "triage_result": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


with st.sidebar:
    st.title("VetConnect AI")
    st.markdown("---")
    if st.button("AI Vet Chat", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()
    if st.button("Symptom Triage", use_container_width=True):
        st.session_state.page = "triage"
        st.rerun()
    if st.button("Find Clinics", use_container_width=True):
        st.session_state.page = "clinics"
        st.rerun()
    st.markdown("---")
    st.caption("Not a substitute for professional veterinary care.")


if st.session_state.page == "chat":
    st.header("AI Vet Assistant")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Describe your pet's symptoms...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_vet_ai(user_input, st.session_state.chat_history[-10:])
            st.markdown(response)

        st.session_state.chat_history.append({"role": "assistant", "content": response})

    if st.session_state.chat_history and st.button("Clear chat"):
        st.session_state.chat_history = []
        st.rerun()


elif st.session_state.page == "triage":
    st.header("Symptom Triage")

    with st.form("triage_form"):
        col1, col2 = st.columns(2)
        with col1:
            species  = st.selectbox("Species", ["Dog", "Cat", "Rabbit", "Bird", "Other"])
            age      = st.text_input("Age", placeholder="e.g. 3 years")
        with col2:
            weight   = st.text_input("Weight (kg)", placeholder="e.g. 12")
            duration = st.text_input("Symptom duration", placeholder="e.g. 6 hours")

        symptoms  = st.text_area("Describe symptoms", height=100, placeholder="e.g. vomiting, lethargy, pale gums")
        submitted = st.form_submit_button("Run Triage", type="primary")

    if submitted and symptoms.strip():
        with st.spinner("Analysing..."):
            result = triage_symptoms(species, age, weight, symptoms, duration)
        st.session_state.triage_result = result

    if st.session_state.triage_result:
        st.markdown("---")
        r = st.session_state.triage_result
        if "Red" in r:
            st.error("Emergency — contact a vet immediately.")
        elif "Amber" in r:
            st.warning("Vet visit recommended soon.")
        else:
            st.success("Monitor at home.")
        st.markdown(r)


elif st.session_state.page == "clinics":
    st.header("Find Nearby Clinics")

    emergency_only = st.checkbox("Show emergency clinics only")
    user_lat, user_lon = 12.9716, 77.5946

    vets = get_vets()
    if emergency_only:
        vets = vets[vets["Emergency"]]

    vets = vets.copy()
    vets["Distance (km)"] = vets.apply(
        lambda r: round(haversine(user_lat, user_lon, r["Latitude"], r["Longitude"]), 2), axis=1
    )
    vets = vets.sort_values("Distance (km)").head(6)

    for _, row in vets.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{row['Name']}** — {row['Area']}")
            st.caption(f"{row['Phone']}  |  {row['Hours']}  |  {row['Distance (km)']} km")
        with col2:
            if row["Emergency"]:
                st.success("24h")
            st.caption(row["Type"])
        st.divider()

st.caption("VetConnect AI — AI output is informational only.")
