from django.contrib import admin
from django.urls import path
from dpapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('prediction/', views.prediction, name='prediction'),
    path('fprediction/', views.fprediction, name='fprediction'),
    path('history/', views.history, name='history'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]
