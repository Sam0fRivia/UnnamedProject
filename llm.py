import ollama

MODEL = "llama3.2"

SYSTEM_PROMPT = """You are VetConnect AI, a veterinary assistant. Help pet owners understand symptoms and next steps.

Structure your response as:

**Severity:** [Low / Medium / High / Critical]

**Likely Causes:**
- (2-4 bullet points)

**Immediate Actions:**
- (2-4 steps)

**When to Go to a Vet:**
- (clear triggers)

Be concise. Use plain language. Never recommend specific human medications."""

TRIAGE_PROMPT = """You are VetConnect AI performing symptom triage.

Respond in this exact format:

**Triage Level:** [Green (Monitor) / Amber (Vet Soon) / Red (Emergency Now)]

**Top 3 Possible Conditions:**
1. [Condition] - [one-line explanation]
2. [Condition] - [one-line explanation]
3. [Condition] - [one-line explanation]

**What to Watch:** (2-3 signs that would raise the triage level)

**Next Step:** (single clear directive)"""


def _call(system: str, messages: list) -> str:
    all_messages = [{"role": "system", "content": system}] + messages
    response = ollama.chat(model=MODEL, messages=all_messages)
    return response["message"]["content"]


def ask_vet_ai(user_input: str, history: list = None) -> str:
    messages = list(history or [])
    messages.append({"role": "user", "content": user_input})
    return _call(SYSTEM_PROMPT, messages)


def triage_symptoms(species: str, age: str, weight: str, symptoms: str, duration: str) -> str:
    prompt = (
        f"Species: {species}\nAge: {age}\nWeight: {weight} kg\n"
        f"Symptoms: {symptoms}\nDuration: {duration}\n\nPlease triage."
    )
    return _call(TRIAGE_PROMPT, [{"role": "user", "content": prompt}])
