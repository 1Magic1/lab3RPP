from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patient/<str:patient_id>/', views.patient_view, name='patient_view'),
    path('patient/<str:patient_id>/update/', views.update_patient_info, name='update_patient_info'),
    path('doctor/<str:doctor_id>/', views.doctor_view, name='doctor_view'),
    path('doctor/<str:doctor_id>/create_prescription/<str:patient_id>/', views.create_prescription, name='create_prescription'),
    path('doctor/<str:doctor_id>/update_medical_card/<str:patient_id>/', views.update_medical_card, name='update_medical_card'),
    path('pharmacist/', views.pharmacist_view, name='pharmacist_view'),
    path('pharmacist/sell/<int:prescription_index>/', views.sell_medicine, name='sell_medicine'),
]
