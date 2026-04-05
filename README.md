# VetConnect AI

An AI-powered veterinary assistant that helps pet owners understand their pet's symptoms, triage urgency levels, and find nearby veterinary clinics. Features AI chat for symptom discussion, rapid severity assessment with possible conditions, and clinic location services. Built with Streamlit, Ollama/Llama 3.2, Pandas, and Haversine distance calculation. Provides structured guidance but is not a substitute for professional veterinary care.

## Project Structure

```
vetconnect-ai/
├── app.py          # Streamlit UI and page routing
├── llm.py          # LLM integration and prompt templates
├── data.py         # Vet clinic database and data loading
└── requirements.txt
```

### File Details

**`app.py`** — Main Streamlit application
- Three-page navigation: Chat, Triage, Clinics
- Session state management for chat history
- Haversine distance calculation for nearby clinics
- Location-based filtering and sorting

**`llm.py`** — LLM integration layer
- Ollama model interface (Llama 3.2)
- Two specialized prompts: general vet chat and symptom triage
- Message history support for conversational context

**`data.py`** — Clinic database
- Pre-loaded vet clinic data for Hyderabad
- Includes 7 clinics with names, locations, hours, emergency status
- Returns pandas DataFrame for easy querying

## Usage

### 1. AI Vet Chat
Ask questions about your pet's symptoms in natural language. The AI provides:
- Estimated severity level
- Likely causes
- Immediate actions
- When to seek professional care

**Example:** _"My dog has been vomiting for 2 hours and won't eat"_

### 2. Symptom Triage
Structured form for rapid assessment. Input:
- Species (Dog, Cat, Rabbit, Bird, Other)
- Age and weight
- Symptom description
- Duration

Returns a color-coded triage level:
- Green — Monitor at home
- Amber — Vet visit recommended soon
- Red — Emergency, contact vet immediately

### 3. Find Clinics
View nearby veterinary clinics sorted by distance. Filter by:
- Emergency availability (24-hour clinics)
- Distance from default location (Hyderabad center: 12.9716°N, 77.5946°E)

Shows clinic name, area, phone, hours, and distance.

## Important Disclaimer

Not a substitute for professional veterinary care. VetConnect AI provides informational guidance only and should not replace consultation with a licensed veterinarian. Always seek professional medical advice for serious symptoms or emergencies.

---

**VetConnect AI** — Hackathon Project
