import os, sys, django
sys.path.insert(0, '/home/claude/dp_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dp_project.settings')
django.setup()

from dpapp.models import Doctor

Doctor.objects.all().delete()

doctors = [
    dict(name="Arjun Mehta", specialty="Infectious Disease Specialist", experience=12, rating=4.9, fee=500, available_today=True, location="Civil Lines, Kanpur", diseases="dengue,malaria,typhoid,influenza,tuberculosis", avatar_initials="AM", avatar_color="blue"),
    dict(name="Priya Sharma", specialty="General Physician & Internist", experience=8, rating=4.8, fee=350, available_today=True, location="Swaroop Nagar, Kanpur", diseases="dengue,malaria,typhoid,influenza,common cold,gastroenteritis", avatar_initials="PS", avatar_color="green"),
    dict(name="Rakesh Verma", specialty="Internal Medicine Specialist", experience=15, rating=4.6, fee=700, available_today=False, location="Kidwai Nagar, Kanpur", diseases="dengue,typhoid,malaria,tuberculosis,hepatitis", avatar_initials="RV", avatar_color="amber"),
    dict(name="Sunita Agarwal", specialty="Hepatologist & Gastroenterologist", experience=10, rating=4.7, fee=600, available_today=True, location="Civil Lines, Kanpur", diseases="hepatitis,jaundice,gastroenteritis", avatar_initials="SA", avatar_color="teal"),
    dict(name="Vikram Joshi", specialty="Gastroenterologist", experience=9, rating=4.5, fee=550, available_today=True, location="Govind Nagar, Kanpur", diseases="hepatitis,jaundice,gastroenteritis,typhoid", avatar_initials="VJ", avatar_color="purple"),
    dict(name="Anil Gupta", specialty="Pulmonologist & Chest Specialist", experience=14, rating=4.8, fee=650, available_today=True, location="Harsh Nagar, Kanpur", diseases="tuberculosis,influenza,common cold,pneumonia", avatar_initials="AG", avatar_color="blue"),
    dict(name="Meena Dixit", specialty="General Physician", experience=6, rating=4.4, fee=300, available_today=True, location="Shyam Nagar, Kanpur", diseases="malaria,dengue,common cold,influenza,gastroenteritis", avatar_initials="MD", avatar_color="coral"),
    dict(name="Suresh Pandey", specialty="Endocrinologist & Diabetologist", experience=11, rating=4.7, fee=700, available_today=False, location="Civil Lines, Kanpur", diseases="diabetes,obesity,thyroid disorders", avatar_initials="SP", avatar_color="amber"),
]

for d in doctors:
    Doctor.objects.create(**d)

print(f"Seeded {Doctor.objects.count()} doctors successfully.")
