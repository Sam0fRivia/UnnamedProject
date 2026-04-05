import pandas as pd

VETS_DATA = [
    {"Name": "Government Veterinary Hospital",    "Area": "Shivajinagar",  "Latitude": 12.9833, "Longitude": 77.6033, "Type": "Government", "Phone": "080-22201234", "Hours": "9am-5pm",  "Emergency": True},
    {"Name": "Cessna Lifeline Veterinary Hospital","Area": "Domlur",       "Latitude": 12.9611, "Longitude": 77.6387, "Type": "Private",    "Phone": "080-25350423", "Hours": "24 hours", "Emergency": True},
    {"Name": "Bangalore Pet Hospital",            "Area": "Indiranagar",   "Latitude": 12.9719, "Longitude": 77.6412, "Type": "Private",    "Phone": "080-25201100", "Hours": "8am-10pm", "Emergency": False},
    {"Name": "CUPA Small Animal Hospital",        "Area": "Hebbal",        "Latitude": 13.0358, "Longitude": 77.5970, "Type": "NGO",        "Phone": "080-23632839", "Hours": "9am-6pm",  "Emergency": False},
    {"Name": "Vetic Pet Clinic",                  "Area": "Koramangala",   "Latitude": 12.9352, "Longitude": 77.6245, "Type": "Private",    "Phone": "080-67800000", "Hours": "8am-11pm", "Emergency": True},
    {"Name": "PetSuites Emergency & Specialty",   "Area": "Whitefield",    "Latitude": 12.9698, "Longitude": 77.7499, "Type": "Private",    "Phone": "080-48524852", "Hours": "24 hours", "Emergency": True},
    {"Name": "Fauna Care Animal Hospital",        "Area": "HSR Layout",    "Latitude": 12.9116, "Longitude": 77.6389, "Type": "Private",    "Phone": "080-41235678", "Hours": "9am-9pm",  "Emergency": False},
]


def get_vets() -> pd.DataFrame:
    return pd.DataFrame(VETS_DATA)
