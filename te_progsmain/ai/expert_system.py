import random

symps = {
    "fever": ["flu", "pneumonia", "COVID-19"],
    "cough": ["flu", "pneumonia", "COVID-19"],
    "shortness of breath": ["pneumonia", "COVID-19"],
    "fatigue": ["flu", "pneumonia", "COVID-19"],
    "body aches": ["flu"],
    "sore throat": ["flu", "COVID-19"],
    "headache": ["flu"],
    "loss of smell or taste": ["COVID-19"],
    "diarrhea": ["COVID-19"],
}

treatments = {
    "flu": ["get rest", "drink fluids", "take over-the-counter medication"],
    "pneumonia": ["antibiotics", "oxygen therapy", "hospitalization"],
    "COVID-19": ["quarantine", "symptomatic treatment", "seek medical attention if symptoms worsen"],
}

def find_condition(symptoms):
    match = set()
    for symptom in symptoms:
        if symptom in symps:
            match.update(symps[symptom])
    return match

def treat(diseases):
    matched = set()
    for disease in diseases:
        if disease in treatments:
            matched.update(treatments[disease])
    return matched

user_input = input("Enter symptoms (comma-separated): ")
user_symptoms = [symptom.strip() for symptom in user_input.split(",")]

matched_diseases = find_condition(user_symptoms)
matched_treatments = treat(matched_diseases)

if matched_diseases:
    print("The symptoms may be associated with the following diseases:")
    for disease in matched_diseases:
        print("-", disease)

    print("\nRecommended treatments:")
    for treatment in matched_treatments:
        print("-", treatment)
else:
    print("No matching diseases found for the entered symptoms.")