"""
llm.py — VetConnect AI local model interface
All inference via Ollama. No internet required after model pull.
"""

import ollama

# ── Model ─────────────────────────────────────────────────────────────────────
# llama3.2 (3B) — best local quality/speed balance.
# Swap to "phi3" or "llama3.2:1b" for lower-RAM devices.
MODEL = "llama3.2"

# ── System prompts ─────────────────────────────────────────────────────────────

_VET_SYSTEM = """You are VetConnect AI, a knowledgeable, calm, and compassionate veterinary assistant.
You help pet owners assess their animal's condition and decide on the right next steps.

Always structure your response exactly like this:

**Severity:** [Low / Medium / High / Critical]

**What this likely is:**
(2–3 sentences explaining the probable cause in plain language)

**What to do right now:**
- (Step 1)
- (Step 2)
- (Step 3)

**Home care tips** *(for Low/Medium only)*:
- (what to watch for, feeding advice, rest)

**Go to a vet immediately if:**
- (2–3 specific warning signs)

**A word of reassurance:**
(One warm, empathetic sentence for the owner.)

Rules:
- Never recommend specific dosages of human medications
- Always flag Critical cases clearly and early
- Use plain language — assume the owner is stressed and non-medical"""

_TRIAGE_SYSTEM = """You are VetConnect AI performing a rapid veterinary triage.

Respond in exactly this format:

**Triage Level:** [🟢 Green — Monitor at Home / 🟡 Amber — Vet Within 24h / 🔴 Red — Emergency Now]

**Most likely condition:** (name + one-line explanation)

**Other possibilities:**
1. (condition — reason)
2. (condition — reason)

**Watch for these warning signs:**
- (sign that would escalate triage level)
- (sign that would escalate triage level)

**Your next step:** (single clear directive — one sentence)

Be direct. Owners are stressed. No hedging."""

_MEDICATION_SYSTEM = """You are a veterinary pharmacology assistant.
Be accurate, specific, and flag anything dangerous with ⚠️.

Structure your response as:

**Safety verdict:** [✅ Generally Safe / ⚠️ Use with Caution / 🚫 Dangerous / ☠️ Toxic — Do Not Use]

**Safe dose range:** (if applicable, or "Not recommended")

**Common side effects:**
- (list)

**Critical warnings:**
- (anything that warrants immediate vet contact)

**Better alternatives:** (if the medication is unsafe)

Keep it brief. Owners need fast, clear answers."""

_HEALTH_SUMMARY_SYSTEM = """You are a veterinary health advisor generating a personalised pet health summary.

Given the pet's profile, generate a structured health report card with:

**Health Overview:**
(2 sentences based on species, age, weight, and any noted conditions)

**Age-related health priorities:**
- (screening or check recommended for this life stage)
- (vaccination or parasite prevention note)
- (dental, weight, or diet note)

**Breed/species watch list:**
- (1–2 conditions common in this species/breed to watch for)

**Recommended vet visit frequency:** (e.g. Every 6 months / Annual / Quarterly)

**One tip for this month:**
(Practical, specific, and actionable.)

Keep it warm, positive, and useful — not alarmist."""

_FIRST_AID_SYSTEM = """You are a veterinary first aid advisor.
Given a specific situation, provide a concise, numbered first aid procedure.

Format:
**Situation:** (restate briefly)

**Do this now:**
1. (step)
2. (step)
3. (step)
4. (step)

**Important:** (one critical caution)

**When to stop home care and go to a vet:** (one sentence)

Be specific, numbered, and use plain language."""


# ── Public API ─────────────────────────────────────────────────────────────────

def ask_vet_ai(user_input: str, history: list[dict] | None = None) -> str:
    """Conversational AI vet assistant with optional history."""
    messages = [{"role": "system", "content": _VET_SYSTEM}]
    if history:
        messages.extend(history[-10:])
    messages.append({"role": "user", "content": user_input})
    r = ollama.chat(model=MODEL, messages=messages)
    return r["message"]["content"]


def triage_symptoms(species: str, age: str, weight: str, symptoms: str, duration: str) -> str:
    """Structured Green/Amber/Red triage assessment."""
    prompt = (
        f"Species: {species}\nAge: {age}\nWeight: {weight} kg\n"
        f"Symptoms: {symptoms}\nDuration: {duration}\n\nPerform triage."
    )
    messages = [{"role": "system", "content": _TRIAGE_SYSTEM}, {"role": "user", "content": prompt}]
    r = ollama.chat(model=MODEL, messages=messages)
    return r["message"]["content"]


def ask_medication_info(medication: str, species: str) -> str:
    """Safety assessment for a medication and species."""
    prompt = f"Is '{medication}' safe for a {species}? Full assessment please."
    messages = [{"role": "system", "content": _MEDICATION_SYSTEM}, {"role": "user", "content": prompt}]
    r = ollama.chat(model=MODEL, messages=messages)
    return r["message"]["content"]


def generate_health_summary(pet: dict) -> str:
    """Generate a personalised health report card for a pet profile."""
    prompt = (
        f"Name: {pet.get('name')}\n"
        f"Species: {pet.get('species')}\n"
        f"Breed: {pet.get('breed', 'Unknown')}\n"
        f"Age: {pet.get('age')}\n"
        f"Weight: {pet.get('weight')} kg\n"
        f"Known conditions/notes: {pet.get('notes', 'None')}\n\n"
        "Generate a personalised health report card."
    )
    messages = [{"role": "system", "content": _HEALTH_SUMMARY_SYSTEM}, {"role": "user", "content": prompt}]
    r = ollama.chat(model=MODEL, messages=messages)
    return r["message"]["content"]


def ask_first_aid(situation: str, species: str) -> str:
    """First aid procedure for a specific situation."""
    prompt = f"Species: {species}\nSituation: {situation}\nProvide first aid steps."
    messages = [{"role": "system", "content": _FIRST_AID_SYSTEM}, {"role": "user", "content": prompt}]
    r = ollama.chat(model=MODEL, messages=messages)
    return r["message"]["content"]
