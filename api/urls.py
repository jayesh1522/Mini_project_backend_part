from django.urls import include, path
from rest_framework import routers
from .views import *



urlpatterns = [
    path('medicine/<int:medicine_id>/',MedicineView.as_view(),name="medicine"),
    path('medicine/',MedicineView.as_view(),name="medicine_list"),
    path('user/',UserInfoView.as_view(),name="user_info"),
    path('record/',MedicalRecordView.as_view(), name="medical_record")
    ]