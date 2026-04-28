from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import pandas as pd
import os
import joblib
from .models import History, Doctor, Appointment

path = os.path.dirname(__file__)
model = joblib.load(open(os.path.join(path, 'best_model.pkl'), 'rb'))
label_encoder = joblib.load(open(os.path.join(path, 'label_encoder.pkl'), 'rb'))

SYMPTOMS = ["fever", "headache", "nausea", "vomiting", "fatigue",
            "joint_pain", "skin_rash", "cough", "weight_loss", "yellow_eyes"]

DISEASE_TIPS = {
    "dengue": [
        "Stay hydrated — drink plenty of fluids and ORS",
        "Rest completely, avoid physical exertion",
        "Monitor platelet count with regular blood tests",
        "Avoid aspirin or ibuprofen — use paracetamol only",
        "Use mosquito repellent to prevent spreading",
        "Visit ER if bleeding or severe pain occurs",
    ],
    "malaria": [
        "Complete the full course of prescribed antimalarials",
        "Use mosquito nets while sleeping",
        "Stay in a cool, well-ventilated room",
        "Take paracetamol for fever management",
        "Avoid alcohol during treatment",
        "Follow up with blood tests after treatment",
    ],
    "typhoid": [
        "Drink only boiled or bottled water",
        "Eat soft, easily digestible foods",
        "Complete the full antibiotic course",
        "Wash hands thoroughly before eating",
        "Avoid raw vegetables and street food",
        "Rest adequately to help immune response",
    ],
    "hepatitis": [
        "Avoid alcohol completely during recovery",
        "Eat small, frequent, low-fat meals",
        "Get adequate rest — avoid overexertion",
        "Avoid medications that stress the liver",
        "Follow up with liver function tests regularly",
        "Maintain strict hand and food hygiene",
    ],
    "tuberculosis": [
        "Complete the full 6-month antibiotic course",
        "Cover mouth when coughing or sneezing",
        "Ensure good ventilation in your living space",
        "Eat a nutritious, protein-rich diet",
        "Avoid contact with immunocompromised people",
        "Attend all follow-up appointments and sputum tests",
    ],
    "influenza": [
        "Rest at home and avoid contact with others",
        "Stay hydrated with water and warm liquids",
        "Use paracetamol for fever and body aches",
        "Wash hands frequently to prevent spread",
        "Consider annual flu vaccination going forward",
        "Seek care if breathing difficulty develops",
    ],
    "default": [
        "Consult your doctor for a proper diagnosis",
        "Stay well hydrated throughout the day",
        "Rest and avoid strenuous physical activity",
        "Monitor your symptoms and note any changes",
        "Maintain a balanced, nutritious diet",
        "Take any prescribed medications as directed",
    ],
}

SLOTS = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
         "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]


def get_tips(disease):
    disease_lower = disease.lower()
    for key in DISEASE_TIPS:
        if key in disease_lower:
            return DISEASE_TIPS[key]
    return DISEASE_TIPS["default"]


def get_doctors_for_disease(disease):
    disease_lower = disease.lower()
    matched = []
    for doc in Doctor.objects.all():
        if any(d in disease_lower or disease_lower in d for d in doc.disease_list()):
            matched.append(doc)
    if not matched:
        matched = list(Doctor.objects.filter(specialty__icontains="General")[:3])
    return matched


def index(req):
    total = History.objects.count()
    appt_count = Appointment.objects.count()
    recent = History.objects.order_by('-id')[:3]
    return render(req, "index.html", {"total": total, "recent": recent, "appt_count": appt_count})


def prediction(req):
    if req.method == 'POST':
        user_input = [req.POST.get(s, 0) for s in SYMPTOMS]
        input_df = pd.DataFrame([user_input], columns=SYMPTOMS)
        result = model.predict(input_df)[0]
        res = label_encoder.inverse_transform([result])[0]
        his = History(
            fever=user_input[0], headache=user_input[1], nausea=user_input[2],
            vomiting=user_input[3], fatigue=user_input[4], joint_pain=user_input[5],
            skin_rash=user_input[6], cough=user_input[7], weight_loss=user_input[8],
            yellow_eyes=user_input[9], res=res
        )
        his.save()
        doctors = get_doctors_for_disease(res)
        tips = get_tips(res)
        return render(req, "prediction.html", {
            "res": res,
            "inputs": dict(zip(SYMPTOMS, user_input)),
            "doctors": doctors,
            "tips": tips,
        })
    return render(req, "prediction.html")


def fprediction(req):
    if req.method == 'POST':
        csv_file = req.FILES["csv_file"]
        df = pd.read_csv(csv_file)
        input_df = df.drop("disease", axis='columns', errors='ignore')
        result = model.predict(input_df)[0]
        res = label_encoder.inverse_transform([result])[0]
        row = input_df.iloc[0]
        his = History(
            fever=row[0], headache=row[1], nausea=row[2], vomiting=row[3],
            fatigue=row[4], joint_pain=row[5], skin_rash=row[6], cough=row[7],
            weight_loss=row[8], yellow_eyes=row[9], res=res
        )
        his.save()
        doctors = get_doctors_for_disease(res)
        tips = get_tips(res)
        return render(req, "fprediction.html", {"res": res, "doctors": doctors, "tips": tips})
    return render(req, "fprediction.html")


def history(req):
    his = History.objects.all().order_by('-id')
    return render(req, "history.html", {"his": his})


def doctors_view(req):
    disease = req.GET.get('disease', '')
    if disease:
        docs = get_doctors_for_disease(disease)
        tips = get_tips(disease)
    else:
        docs = Doctor.objects.all()
        tips = []
    appointments = Appointment.objects.order_by('-created_at')[:5]
    return render(req, "doctors.html", {
        "doctors": docs,
        "disease": disease,
        "tips": tips,
        "slots": SLOTS,
        "appointments": appointments,
    })


@require_POST
def book_appointment(req):
    doctor_id = req.POST.get('doctor_id')
    slot = req.POST.get('slot')
    disease = req.POST.get('disease', 'General Consultation')
    patient_name = req.POST.get('patient_name', 'Patient')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    appt = Appointment.objects.create(
        doctor=doctor, slot=slot, disease=disease, patient_name=patient_name
    )
    return JsonResponse({
        'success': True,
        'message': f'Appointment confirmed with Dr. {doctor.name} at {slot}',
        'appt_id': appt.id,
    })
