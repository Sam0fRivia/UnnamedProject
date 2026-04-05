"""
data.py — VetConnect AI embedded data store
No CSV files required. All data lives here.
"""

import pandas as pd

# ── Veterinary Clinics ─────────────────────────────────────────────────────────

VETS_DATA = [
    {"Name": "Government Veterinary Hospital",      "Area": "Shivajinagar",  "Latitude": 12.9833, "Longitude": 77.6033, "Type": "Government", "Phone": "080-22201234", "Hours": "9am–5pm",   "Emergency": True,  "Rating": 4.0, "Specialties": "General, Large Animals"},
    {"Name": "Cessna Lifeline Veterinary Hospital", "Area": "Domlur",        "Latitude": 12.9611, "Longitude": 77.6387, "Type": "Private",    "Phone": "080-25350423", "Hours": "24 hours",   "Emergency": True,  "Rating": 4.7, "Specialties": "Surgery, ICU, Oncology"},
    {"Name": "Bangalore Pet Hospital",              "Area": "Indiranagar",   "Latitude": 12.9719, "Longitude": 77.6412, "Type": "Private",    "Phone": "080-25201100", "Hours": "8am–10pm",  "Emergency": False, "Rating": 4.5, "Specialties": "Dermatology, Dentistry"},
    {"Name": "CUPA Small Animal Hospital",          "Area": "Hebbal",        "Latitude": 13.0358, "Longitude": 77.5970, "Type": "NGO",        "Phone": "080-23632839", "Hours": "9am–6pm",   "Emergency": False, "Rating": 4.3, "Specialties": "Street Animal Rescue, Sterilisation"},
    {"Name": "Pet Vet Clinic",                      "Area": "Richmond Town", "Latitude": 12.9614, "Longitude": 77.6033, "Type": "Private",    "Phone": "080-22111234", "Hours": "9am–8pm",   "Emergency": False, "Rating": 4.2, "Specialties": "General, Vaccinations"},
    {"Name": "Blue Cross Vet Clinic",               "Area": "Jayanagar",     "Latitude": 12.9250, "Longitude": 77.5938, "Type": "NGO",        "Phone": "080-26630000", "Hours": "9am–5pm",   "Emergency": False, "Rating": 4.4, "Specialties": "Rescue, Rehabilitation"},
    {"Name": "Vetic Pet Clinic",                    "Area": "Koramangala",   "Latitude": 12.9352, "Longitude": 77.6245, "Type": "Private",    "Phone": "080-67800000", "Hours": "8am–11pm",  "Emergency": True,  "Rating": 4.6, "Specialties": "Internal Medicine, Imaging"},
    {"Name": "PetSuites Emergency & Specialty",     "Area": "Whitefield",    "Latitude": 12.9698, "Longitude": 77.7499, "Type": "Private",    "Phone": "080-48524852", "Hours": "24 hours",   "Emergency": True,  "Rating": 4.8, "Specialties": "Emergency, Critical Care, Surgery"},
    {"Name": "Fauna Care Animal Hospital",          "Area": "HSR Layout",    "Latitude": 12.9116, "Longitude": 77.6389, "Type": "Private",    "Phone": "080-41235678", "Hours": "9am–9pm",   "Emergency": False, "Rating": 4.3, "Specialties": "Exotic Animals, Avian"},
    {"Name": "Sarjapur Animal Hospital",            "Area": "Sarjapur",      "Latitude": 12.8978, "Longitude": 77.6856, "Type": "Private",    "Phone": "080-49867890", "Hours": "9am–8pm",   "Emergency": False, "Rating": 4.1, "Specialties": "General, Orthopaedics"},
    {"Name": "Vet Xpress",                          "Area": "Marathahalli",  "Latitude": 12.9561, "Longitude": 77.7012, "Type": "Private",    "Phone": "080-45012345", "Hours": "8am–10pm",  "Emergency": False, "Rating": 4.2, "Specialties": "General, Grooming"},
]

# ── Rescue NGOs ────────────────────────────────────────────────────────────────

NGOS_DATA = [
    {"Name": "CUPA",                         "Area": "Bangalore",  "Phone": "080-22947300", "Service": "Rescue & Sterilisation", "WhatsApp": False, "Accepts_Street_Animals": True},
    {"Name": "Charlie Animal Rescue Centre", "Area": "Yelahanka",  "Phone": "9483911110",   "Service": "Emergency Rescue",       "WhatsApp": True,  "Accepts_Street_Animals": True},
    {"Name": "People For Animals",           "Area": "Bangalore",  "Phone": "080-28602682", "Service": "Animal Welfare",         "WhatsApp": False, "Accepts_Street_Animals": True},
    {"Name": "Blue Cross Bangalore",         "Area": "Bangalore",  "Phone": "080-26630000", "Service": "Rescue & Rehoming",      "WhatsApp": False, "Accepts_Street_Animals": True},
    {"Name": "Sarvoham Animal Foundation",   "Area": "Bangalore",  "Phone": "9886040000",   "Service": "Rescue & Sanctuary",     "WhatsApp": True,  "Accepts_Street_Animals": True},
    {"Name": "CARE Animal Shelter",          "Area": "Bangalore",  "Phone": "080-28602682", "Service": "Emergency & Shelter",    "WhatsApp": True,  "Accepts_Street_Animals": True},
    {"Name": "Friendicoes SECA",             "Area": "Bangalore",  "Phone": "9686040000",   "Service": "Spay/Neuter & Rescue",   "WhatsApp": True,  "Accepts_Street_Animals": False},
    {"Name": "Animal Rahat",                 "Area": "Bangalore",  "Phone": "9448113355",   "Service": "Working Animal Welfare", "WhatsApp": False, "Accepts_Street_Animals": False},
]

# ── Breed-specific health risks ────────────────────────────────────────────────

BREED_RISKS = {
    # Dogs
    "Labrador Retriever":   ["Hip dysplasia", "Obesity", "Ear infections"],
    "German Shepherd":      ["Hip dysplasia", "Degenerative myelopathy", "Bloat (GDV)"],
    "Golden Retriever":     ["Cancer (high risk)", "Hip dysplasia", "Skin allergies"],
    "Pug":                  ["Brachycephalic syndrome", "Eye ulcers", "Skin fold infections"],
    "Bulldog":              ["Brachycephalic syndrome", "Joint problems", "Skin infections"],
    "Beagle":               ["Epilepsy", "Hypothyroidism", "Intervertebral disc disease"],
    "Dachshund":            ["Intervertebral disc disease (IVDD)", "Obesity", "Dental disease"],
    "Doberman":             ["Dilated cardiomyopathy", "Von Willebrand disease", "Wobbler syndrome"],
    "Boxer":                ["Cancer", "Cardiomyopathy", "Hip dysplasia"],
    "Husky":                ["Eye conditions (PRA)", "Hip dysplasia", "Hypothyroidism"],
    "Indian Pariah / INDog":["Generally hardy", "Tick-borne diseases", "Mange"],
    # Cats
    "Persian":              ["Polycystic kidney disease", "Brachycephalic airway issues", "Dental crowding"],
    "Siamese":              ["Amyloidosis", "Crossed eyes (cosmetic)", "Dental disease"],
    "Maine Coon":           ["Hypertrophic cardiomyopathy (HCM)", "Hip dysplasia", "Spinal muscular atrophy"],
    "Bengal":               ["Progressive retinal atrophy (PRA)", "HCM", "Flat-chested kitten syndrome"],
    "Ragdoll":              ["HCM", "Polycystic kidney disease", "Bladder stones"],
    "Domestic Shorthair":   ["Obesity", "Dental disease", "Hyperthyroidism (older cats)"],
    "Domestic Longhair":    ["Hairballs", "Dental disease", "Obesity"],
}

# ── Common first aid situations (for quick-reference guide) ───────────────────

FIRST_AID_QUICKREF = [
    {"Situation": "Minor cut or wound",       "Steps": "Clean with saline, apply gentle pressure, cover with clean bandage. Watch for swelling or discharge.", "Go to Vet": "Deep wound, won't stop bleeding, signs of infection"},
    {"Situation": "Bee/wasp sting",           "Steps": "Remove stinger with card edge (not tweezers). Apply cold pack. Watch for swelling of face/throat.", "Go to Vet": "Face swelling, difficulty breathing, collapse"},
    {"Situation": "Eye discharge",            "Steps": "Gently wipe with damp cotton wool (outward from corner). Do not use eye drops unless prescribed.", "Go to Vet": "Cloudiness, squinting, redness, or swelling"},
    {"Situation": "Vomiting (once or twice)", "Steps": "Withhold food for 4–6 hours. Offer small sips of water. Reintroduce bland food (boiled chicken/rice).", "Go to Vet": "Blood in vomit, more than 3 times, lethargy, distended belly"},
    {"Situation": "Diarrhoea (mild)",         "Steps": "Bland diet. Ensure constant access to water. Small frequent meals.", "Go to Vet": "Blood, more than 24 hours, puppy/kitten, lethargy"},
    {"Situation": "Limping (no trauma)",      "Steps": "Rest and restrict movement. Check paw for thorns/cuts. Do not give painkillers.", "Go to Vet": "Cannot bear weight, swelling, or limping persists beyond 24h"},
    {"Situation": "Tick found on skin",       "Steps": "Use fine-tipped tweezers or a tick hook. Grasp close to skin, pull upward steadily. Clean area with alcohol.", "Go to Vet": "Tick mouth remains, signs of fever/lethargy within 2 weeks"},
    {"Situation": "Overheating (mild)",       "Steps": "Move to cool area. Apply cool (not cold) water to paws and ears. Offer water in small amounts.", "Go to Vet": "Seizures, collapse, vomiting, gums pale or grey"},
]

# ── Vaccination schedule reference ────────────────────────────────────────────

VACCINATION_SCHEDULE = {
    "Dog": [
        {"Age": "6–8 weeks",    "Vaccine": "Distemper, Parvovirus (DHPPi core)", "Type": "Core"},
        {"Age": "10–12 weeks",  "Vaccine": "DHPPi booster + Leptospirosis",       "Type": "Core"},
        {"Age": "14–16 weeks",  "Vaccine": "DHPPi final + Rabies",                "Type": "Core"},
        {"Age": "12–16 months", "Vaccine": "Annual booster — all core vaccines",  "Type": "Booster"},
        {"Age": "Every year",   "Vaccine": "Rabies + Leptospirosis",               "Type": "Annual"},
        {"Age": "Every 3 years","Vaccine": "DHPPi (after initial boosters)",       "Type": "Triennial"},
    ],
    "Cat": [
        {"Age": "6–8 weeks",    "Vaccine": "Feline herpesvirus, Calicivirus, Panleukopenia (FVRCP)", "Type": "Core"},
        {"Age": "10–12 weeks",  "Vaccine": "FVRCP booster",                                          "Type": "Core"},
        {"Age": "14–16 weeks",  "Vaccine": "FVRCP final + Rabies",                                   "Type": "Core"},
        {"Age": "12–16 months", "Vaccine": "FVRCP + Rabies booster",                                 "Type": "Booster"},
        {"Age": "Every 1–3 yrs","Vaccine": "FVRCP + Rabies (per vet advice)",                        "Type": "Adult"},
    ],
}


# ── Public API ─────────────────────────────────────────────────────────────────

def get_vets(location: str | None = None) -> pd.DataFrame:
    df = pd.DataFrame(VETS_DATA)
    if location:
        df = df[df["Area"].str.contains(location, case=False, na=False)]
    return df


def get_ngos() -> pd.DataFrame:
    return pd.DataFrame(NGOS_DATA)


def get_breed_risks(breed: str) -> list[str]:
    for key in BREED_RISKS:
        if breed.lower() in key.lower() or key.lower() in breed.lower():
            return BREED_RISKS[key]
    return []


def get_first_aid_quickref() -> pd.DataFrame:
    return pd.DataFrame(FIRST_AID_QUICKREF)


def get_vaccination_schedule(species: str) -> pd.DataFrame:
    data = VACCINATION_SCHEDULE.get(species, [])
    return pd.DataFrame(data) if data else pd.DataFrame()
