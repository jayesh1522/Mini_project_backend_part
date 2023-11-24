from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Medicine)
admin.site.register(UserInfo)
admin.site.register(MedicalRecord)
