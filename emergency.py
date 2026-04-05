"""
emergency.py — VetConnect AI emergency guide data
All guides embedded as dataclasses. No CSV required.
"""

from dataclasses import dataclass, field


@dataclass
class EmergencyGuide:
    name: str
    severity: str                   # "Critical" | "High" | "Medium"
    icon: str
    summary: str
    immediate_dos: list[str]
    immediate_donts: list[str]
    step_by_step: list[str]
    call_vet_if: list[str]
    estimated_window: str
    reassurance: str
    related: list[str] = field(default_factory=list)  # Cross-links to other emergencies


EMERGENCY_GUIDES: dict[str, EmergencyGuide] = {

    "Road Accident / Hit by Vehicle": EmergencyGuide(
        name="Road Accident / Hit by Vehicle",
        severity="Critical",
        icon="🚨",
        summary="Internal injuries, shock, or spinal damage are common even without visible wounds. Speed is critical.",
        immediate_dos=[
            "Stay calm — your panic transfers directly to the animal",
            "Approach slowly and speak in a low, soothing tone",
            "Slide a stiff board, tray, or jacket under the animal — keep the spine flat",
            "Control visible bleeding with a clean cloth and firm, steady pressure",
            "Keep the animal warm with a blanket or jacket",
            "Get to an emergency vet within 30 minutes",
        ],
        immediate_donts=[
            "Do NOT lift the animal by its legs or middle — spinal injury risk",
            "Do NOT give any food, water, or human medication",
            "Do NOT leave the animal alone once you've started helping",
            "Do NOT muzzle if the animal is having difficulty breathing",
        ],
        step_by_step=[
            "Ensure the road is safe — turn on hazard lights, slow traffic",
            "Check for responsiveness: call the animal's name, clap gently",
            "Look for visible bleeding; apply clean cloth with steady pressure",
            "Improvise a stretcher (board, jacket, or blanket held taut by two people)",
            "Slide the animal onto the stretcher without bending its spine",
            "Call the nearest 24-hour emergency vet and tell them you're en route",
            "Keep the animal in a dark, quiet, warm space during transport",
            "Monitor breathing every 2–3 minutes",
        ],
        call_vet_if=[
            "Any loss of consciousness, even brief",
            "Limbs that cannot move or appear paralysed",
            "Pale, white, blue, or grey gums",
            "Laboured, rapid, or absent breathing",
            "Blood from mouth, nose, or ears",
            "Swollen, rigid, or distended abdomen",
        ],
        estimated_window="Internal bleeding can be fatal within 1–2 hours. Do not wait for symptoms to worsen.",
        reassurance="You are doing the right thing. Moving carefully and staying calm is the most helpful thing right now.",
        related=["Severe Bleeding", "Unconscious / Unresponsive", "Broken Bone / Fracture"],
    ),

    "Severe Bleeding": EmergencyGuide(
        name="Severe Bleeding",
        severity="Critical",
        icon="🩸",
        summary="Uncontrolled bleeding can cause fatal blood loss within minutes. Direct, sustained pressure is the priority.",
        immediate_dos=[
            "Apply a clean cloth, gauze, or folded clothing directly on the wound",
            "Press FIRMLY and steadily — do not lift the cloth to check; add more layers on top",
            "Elevate the injured limb above heart level if possible",
            "Keep the animal still and warm",
            "Get to an emergency vet immediately while maintaining pressure",
        ],
        immediate_donts=[
            "Do NOT remove the cloth once applied — clots form underneath",
            "Do NOT apply a tourniquet unless bleeding is life-threatening and you're trained",
            "Do NOT apply ice directly to the wound",
            "Do NOT give aspirin or ibuprofen — they thin the blood",
        ],
        step_by_step=[
            "Put on gloves if available; use a plastic bag over your hand if not",
            "Locate the source of bleeding",
            "Place the thickest clean material you have firmly over the wound",
            "Apply continuous firm pressure — set a timer and do not peek for at least 3 minutes",
            "If blood soaks through, add more layers on top — do not remove the original",
            "Secure with a bandage or torn cloth to free your hands for transport",
            "Call ahead to the vet so they're ready when you arrive",
        ],
        call_vet_if=[
            "Blood is bright red and spurting (arterial bleeding)",
            "Wound is deep enough to see tissue, fat, or bone",
            "Bleeding hasn't slowed after 5 minutes of firm pressure",
            "Animal is becoming limp, weak, or losing consciousness",
        ],
        estimated_window="Arterial bleeding can be fatal in under 5 minutes. Venous wounds give more time but still need urgent care.",
        reassurance="Direct pressure is the most effective first aid for bleeding. You don't need special supplies — just pressure and calm.",
        related=["Road Accident / Hit by Vehicle", "Unconscious / Unresponsive"],
    ),

    "Poison / Toxic Ingestion": EmergencyGuide(
        name="Poison / Toxic Ingestion",
        severity="Critical",
        icon="☠️",
        summary="Toxins act fast. Do NOT induce vomiting without vet guidance — with some poisons it makes things worse.",
        immediate_dos=[
            "Identify what was ingested and how much — bring the packaging",
            "Note the exact time of ingestion",
            "Call a vet or poison helpline immediately — even before symptoms appear",
            "Keep the animal calm and confined",
            "Collect a sample of any vomit in a sealed bag",
        ],
        immediate_donts=[
            "Do NOT induce vomiting unless explicitly told to by a vet",
            "Do NOT give milk, oil, or home remedies",
            "Do NOT wait for symptoms — most poisons are easiest to treat early",
            "Do NOT let the animal eat or drink until a vet advises",
        ],
        step_by_step=[
            "Remove the animal from the toxin source",
            "Photograph or bag the packaging of whatever was ingested",
            "Call your vet or an emergency animal poison helpline immediately",
            "Report: species, weight, substance, estimated amount, and time",
            "Follow vet instructions exactly — they may ask you to induce vomiting OR specifically not to",
            "Transport immediately; bring the packaging",
            "Watch for: drooling, tremors, seizures, dilated pupils, collapse",
        ],
        call_vet_if=[
            "Ingestion of: xylitol, grapes/raisins, chocolate, rat poison, human medications, household cleaners, lilies (cats)",
            "Vomiting, excessive drooling, or seizures after eating something unknown",
            "Sudden muscle tremors or weakness",
            "Collapse or loss of consciousness",
        ],
        estimated_window="Some toxins (xylitol, certain rat poisons) cause irreversible damage within 30 minutes. Call immediately.",
        reassurance="Getting the vet on the phone right now — even from home — is the single most important step. They will guide you.",
        related=["Unconscious / Unresponsive", "Seizure"],
    ),

    "Breathing Difficulty / Choking": EmergencyGuide(
        name="Breathing Difficulty / Choking",
        severity="Critical",
        icon="💨",
        summary="Oxygen deprivation causes brain damage within minutes. Any laboured breathing is an emergency.",
        immediate_dos=[
            "Keep the animal as calm as possible — exertion worsens oxygen demand",
            "If choking: open the mouth carefully and look for a visible object",
            "For small dogs and cats: hold upside down briefly — gravity may dislodge the object",
            "Extend the neck gently to open the airway",
            "If gums are turning blue or white — you need to reach a vet within 10 minutes",
        ],
        immediate_donts=[
            "Do NOT reach blindly into the throat — you can push objects deeper",
            "Do NOT use a muzzle or anything that restricts breathing",
            "Do NOT leave the animal unattended",
            "Do NOT keep trying if blind attempts aren't working — transport immediately",
        ],
        step_by_step=[
            "Observe gum colour: pink = okay, white/blue/purple = critical emergency",
            "Open mouth gently and check for a visible foreign object",
            "If object visible: carefully remove with fingers or tweezers",
            "If not visible: do NOT keep trying blindly",
            "For small animals: hold securely, invert, give 2–3 firm back blows between shoulder blades",
            "For large dogs: Heimlich — stand behind, two hands below ribcage, firm upward thrust",
            "Rush to vet; keep the head slightly extended during transport",
        ],
        call_vet_if=[
            "Blue, white, or grey gums at any point",
            "Open-mouth breathing in a cat (almost always an emergency)",
            "Breathing that is rapid, laboured, or involves the belly heaving",
            "Loss of consciousness",
            "Choking attempt failed after 2 tries",
        ],
        estimated_window="Brain damage begins after 4–6 minutes without oxygen. Blue gums mean very little time.",
        reassurance="Stay low, stay slow, stay quiet. Panic raises your pet's oxygen demand. Your calm is literally life-saving.",
        related=["Unconscious / Unresponsive", "Allergic Reaction"],
    ),

    "Heatstroke": EmergencyGuide(
        name="Heatstroke",
        severity="Critical",
        icon="🌡️",
        summary="Body temperature above 40°C (104°F) is dangerous. Above 41.5°C (107°F) causes organ failure.",
        immediate_dos=[
            "Move the animal immediately to a cool, shaded, or air-conditioned space",
            "Apply cool (NOT ice cold) water to paw pads, neck, armpits, and groin",
            "Use a fan to increase evaporation",
            "Offer small amounts of cool water if the animal is alert and swallowing",
            "Get to a vet even if the animal seems to recover — internal damage isn't always visible",
        ],
        immediate_donts=[
            "Do NOT use ice or ice-cold water — it constricts blood vessels, trapping heat inside",
            "Do NOT cover with wet towels and leave — this traps steam",
            "Do NOT force water if the animal is semi-conscious or vomiting",
            "Do NOT assume recovery means no internal damage",
        ],
        step_by_step=[
            "Get the animal out of the heat source immediately",
            "Check responsiveness: can it stand, does it respond to its name?",
            "Apply cool (room temperature) wet cloths to paw pads, groin, armpits, neck",
            "Fan actively — evaporation is the key cooling mechanism",
            "Offer small sips of cool water every few minutes if alert",
            "Monitor: is panting slowing? Is the animal becoming more alert?",
            "Transport to vet even if improving — wrap in a damp cool towel for the journey",
        ],
        call_vet_if=[
            "Temperature above 40°C / 104°F",
            "Vomiting, diarrhoea, or bloody stool",
            "Seizures or muscle tremors",
            "Loss of consciousness or inability to stand",
            "No improvement within 5 minutes of cooling",
        ],
        estimated_window="Organ failure can occur within 15–30 minutes at critical temperatures. Cool first, transport immediately.",
        reassurance="You caught this. Cooling with room-temperature water and moving them out of the heat is already helping.",
        related=["Seizure", "Unconscious / Unresponsive"],
    ),

    "Seizure": EmergencyGuide(
        name="Seizure",
        severity="High",
        icon="⚡",
        summary="Most seizures stop within 1–2 minutes. Your job is to keep the animal safe during the episode.",
        immediate_dos=[
            "Time the seizure the moment it begins",
            "Clear the area of hard or sharp objects",
            "Stay nearby to observe — do not restrain",
            "Keep the room quiet and dark — light and noise can extend seizures",
            "After the seizure: stay calm, speak softly, let the animal come around naturally",
        ],
        immediate_donts=[
            "Do NOT put your hand near the mouth — they cannot swallow their tongue, but they CAN bite",
            "Do NOT restrain the animal's body movement",
            "Do NOT give food or water until fully recovered",
            "Do NOT move during seizure unless immediately near stairs or water",
        ],
        step_by_step=[
            "Start timing immediately — duration is the most critical thing to report",
            "Clear the floor of sharp or heavy objects",
            "Turn off bright lights; mute TVs, ask others to leave the room",
            "Kneel nearby and observe without touching",
            "After shaking stops: soft voice, dim light, let the animal rest in place",
            "Note: duration, which limbs, any urination or defecation",
            "Call vet with: duration, description, and whether this is a first seizure",
        ],
        call_vet_if=[
            "Seizure lasts more than 2 minutes — this is a medical emergency",
            "More than one seizure within 24 hours",
            "Animal doesn't return to normal within 30 minutes post-seizure",
            "This is the first ever seizure",
            "Animal is very young, very old, recently ill, or recently injured",
        ],
        estimated_window="A seizure over 5 minutes without medication can cause permanent brain damage. Past 2 minutes — go now.",
        reassurance="Watching a seizure is frightening, but most are over quickly. Your silence and calm presence is genuinely helping.",
        related=["Poison / Toxic Ingestion", "Heatstroke", "Unconscious / Unresponsive"],
    ),

    "Broken Bone / Fracture": EmergencyGuide(
        name="Broken Bone / Fracture",
        severity="High",
        icon="🦴",
        summary="Keep the animal still and prevent weight-bearing. Improper movement significantly worsens the injury.",
        immediate_dos=[
            "Restrict movement — confine to a small, quiet space",
            "Support the injured limb in the position you found it — do not try to straighten it",
            "Muzzle if the animal is biting from pain, using a strip of cloth",
            "Use a rigid carrier, box, or flat board for transport",
            "Keep warm and as calm as possible",
        ],
        immediate_donts=[
            "Do NOT attempt to splint or set the bone yourself",
            "Do NOT allow the animal to walk or bear weight on the limb",
            "Do NOT straighten or manipulate the limb",
            "Do NOT give human pain medications — ibuprofen and paracetamol are toxic to pets",
        ],
        step_by_step=[
            "Approach slowly — a dog in pain may bite even its owner",
            "Gently confine without forcing the injured area",
            "If bone is through skin (open fracture): cover with clean, damp cloth only — do not push it in",
            "Slide the animal onto a flat rigid surface for transport",
            "Call the vet to prepare for X-ray and pain management",
            "Drive smoothly — reduce jolts",
        ],
        call_vet_if=[
            "Bone is visible through the skin",
            "Limb is at an abnormal angle",
            "Animal cannot bear any weight on a limb after a fall or impact",
            "Severe swelling, bruising, or deformity at a joint",
        ],
        estimated_window="Not immediately life-threatening but pain and swelling worsen quickly. Vet within 2–4 hours.",
        reassurance="Keeping the animal still and calm is the best you can do. You don't need to fix it — just get them there safely.",
        related=["Road Accident / Hit by Vehicle", "Severe Bleeding"],
    ),

    "Unconscious / Unresponsive": EmergencyGuide(
        name="Unconscious / Unresponsive",
        severity="Critical",
        icon="🆘",
        summary="Unconsciousness is always a life-threatening emergency. Check breathing immediately.",
        immediate_dos=[
            "Check for breathing: watch the chest, hold your cheek near their nose",
            "Check gum colour — pink is good, blue/white/grey is critical",
            "If breathing: place in recovery position (on their side)",
            "If not breathing: begin CPR if you know how",
            "Call ahead to an emergency vet immediately",
        ],
        immediate_donts=[
            "Do NOT shake or jostle the animal to wake them",
            "Do NOT give water or anything by mouth",
            "Do NOT leave alone even for a moment",
        ],
        step_by_step=[
            "Call name and tap shoulder gently — any response?",
            "Check breathing for 10 seconds: chest rise, air from nose",
            "Check gum colour by lifting the lip",
            "If not breathing: lay on right side, extend neck, begin CPR",
            "CPR for dogs: both hands on chest behind elbow, compress 1/3 depth, 100–120/min, 30:2 ratio",
            "CPR for cats: one hand around chest, compress with thumb and fingers, same rate",
            "Alternate CPR with breathing checks every 2 minutes",
            "Have someone else drive while you continue CPR en route",
        ],
        call_vet_if=["Any loss of consciousness — always, no exceptions"],
        estimated_window="Brain damage begins within 4 minutes without circulation. Call and drive simultaneously.",
        reassurance="CPR buys time. Even imperfect CPR is vastly better than nothing. You can do this.",
        related=["Road Accident / Hit by Vehicle", "Breathing Difficulty / Choking", "Seizure"],
    ),

    "Allergic Reaction / Anaphylaxis": EmergencyGuide(
        name="Allergic Reaction / Anaphylaxis",
        severity="Critical",
        icon="🐝",
        summary="Severe allergic reactions can close the airway within minutes. Swelling of face or throat is an emergency.",
        immediate_dos=[
            "Remove the source of the allergen if identifiable (sting, food, topical)",
            "Keep the animal calm and still — movement speeds allergen spread",
            "Monitor breathing and gum colour closely",
            "Note the time the reaction began",
            "Get to an emergency vet immediately if facial swelling is present",
        ],
        immediate_donts=[
            "Do NOT give antihistamines without vet instruction — correct dose varies by species and weight",
            "Do NOT induce vomiting if the reaction is from food",
            "Do NOT leave unattended if breathing appears affected",
        ],
        step_by_step=[
            "Identify and remove the allergen source if safe to do so",
            "Check breathing: is it laboured, wheezing, or rapid?",
            "Observe face and muzzle — is there visible swelling?",
            "Check gum colour every 2 minutes",
            "If bee/wasp sting: scrape out stinger with a card — do not squeeze it",
            "If hives only (no breathing change): call vet for advice; may monitor at home",
            "If any breathing change or facial swelling: drive to emergency vet NOW",
        ],
        call_vet_if=[
            "Any swelling of the face, muzzle, or throat",
            "Difficulty breathing or audible wheezing",
            "Vomiting, diarrhoea, and lethargy occurring together after a potential allergen exposure",
            "Collapse or sudden extreme weakness",
            "Known history of severe allergic reactions",
        ],
        estimated_window="Anaphylaxis can close the airway in 15–30 minutes. Facial swelling means go immediately.",
        reassurance="Allergic reactions look alarming. Hives alone are manageable — but facial swelling changes everything. You're right to act fast.",
        related=["Breathing Difficulty / Choking", "Unconscious / Unresponsive"],
    ),

    "Snake Bite": EmergencyGuide(
        name="Snake Bite",
        severity="Critical",
        icon="🐍",
        summary="Assume every snake bite is from a venomous species until confirmed otherwise. Time is critical.",
        immediate_dos=[
            "Keep the animal completely still — movement speeds venom absorption",
            "Keep the bitten area below heart level",
            "Note the time of the bite",
            "Try to remember or photograph the snake (do NOT approach it)",
            "Get to an emergency vet immediately — antivenoms must be given early to work",
        ],
        immediate_donts=[
            "Do NOT cut the wound or try to suck out venom — these are myths and cause harm",
            "Do NOT apply a tourniquet",
            "Do NOT apply ice to the wound",
            "Do NOT give pain medications, especially NSAIDs — they affect clotting",
            "Do NOT let the animal walk if avoidable",
        ],
        step_by_step=[
            "Carry the animal — do not let it walk",
            "Keep calm and keep the animal calm — restrict all movement",
            "Note or photograph the snake safely from a distance",
            "Note exact time of bite",
            "Call the vet en route — they need time to prepare antivenom",
            "Keep the bite site immobile and below heart level during transport",
            "Watch for: rapid swelling, bleeding from wounds, tremors, paralysis",
        ],
        call_vet_if=[
            "Any confirmed or suspected snake bite — always seek vet care",
            "Rapid swelling at or around the bite site",
            "Drooling, weakness, or collapse",
            "Bleeding from the bite that won't stop",
            "Neurological signs: tremors, difficulty walking, drooping eyelids",
        ],
        estimated_window="Venom spreads with movement. Some neurotoxins cause respiratory failure within 1–2 hours. Antivenoms work best when given early.",
        reassurance="Keeping your pet completely still and getting to a vet quickly are the two things that matter most right now. You can do both.",
        related=["Severe Bleeding", "Unconscious / Unresponsive"],
    ),

    "Eye Injury": EmergencyGuide(
        name="Eye Injury",
        severity="High",
        icon="👁️",
        summary="Eyes are fragile and can deteriorate rapidly. Do not rub, rinse without guidance, or delay.",
        immediate_dos=[
            "Prevent the animal from pawing or rubbing the eye — use an e-collar if available",
            "Keep the animal calm and in a dim environment",
            "If a chemical was splashed: rinse with plain water or saline for 5 minutes immediately",
            "Cover loosely with a damp cloth if the eye is protruding",
        ],
        immediate_donts=[
            "Do NOT apply eye drops, ointments, or medications without vet advice",
            "Do NOT try to remove embedded objects",
            "Do NOT let the animal scratch or rub the eye",
        ],
        step_by_step=[
            "Gently restrain the animal to prevent self-injury",
            "Look at the eye without touching: cloudy, red, bulging, discharge?",
            "If chemical exposure: flush gently with water or saline for at least 5 minutes",
            "Improvised e-collar: cut the bottom off a plastic bottle or use a cereal box",
            "Keep in dim light — bright light is painful with eye injuries",
            "Transport carefully to avoid bumps; call vet en route",
        ],
        call_vet_if=[
            "Eye is bulging or appears out of the socket",
            "Visible cut or laceration on the eye surface",
            "Sudden cloudiness or colour change",
            "Animal holding eye closed and unable to open it",
            "Any penetrating object",
        ],
        estimated_window="Some eye injuries cause permanent blindness within hours without treatment. Same-day vet visit is essential.",
        reassurance="Keeping them from rubbing is genuinely protecting their vision right now. You're doing the right thing.",
        related=["Allergic Reaction / Anaphylaxis"],
    ),
}


def get_all_emergencies() -> list[str]:
    return list(EMERGENCY_GUIDES.keys())


def get_emergency_guide(name: str) -> EmergencyGuide | None:
    return EMERGENCY_GUIDES.get(name)


def get_critical_emergencies() -> list[str]:
    return [k for k, v in EMERGENCY_GUIDES.items() if v.severity == "Critical"]
