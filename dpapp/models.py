from django.db import models

class History(models.Model):
    fever = models.CharField(max_length=10)
    headache = models.CharField(max_length=10)
    nausea = models.CharField(max_length=10)
    vomiting = models.CharField(max_length=10)
    fatigue = models.CharField(max_length=10)
    joint_pain = models.CharField(max_length=10)
    skin_rash = models.CharField(max_length=10)
    cough = models.CharField(max_length=10)
    weight_loss = models.CharField(max_length=10)
    yellow_eyes = models.CharField(max_length=10)
    res = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"#{self.id} - {self.res}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    rating = models.FloatField()
    fee = models.IntegerField()
    available_today = models.BooleanField(default=True)
    location = models.CharField(max_length=200, default='Kanpur, UP')
    diseases = models.TextField(help_text='Comma-separated disease names this doctor treats')
    avatar_initials = models.CharField(max_length=3, default='DR')
    avatar_color = models.CharField(max_length=20, default='blue')

    def __str__(self):
        return f"Dr. {self.name} — {self.specialty}"

    def disease_list(self):
        return [d.strip().lower() for d in self.diseases.split(',')]

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100, default='Patient')
    disease = models.CharField(max_length=100)
    slot = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [('confirmed','Confirmed'),('cancelled','Cancelled')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')

    def __str__(self):
        return f"Appt #{self.id} — {self.doctor.name} — {self.slot}"
