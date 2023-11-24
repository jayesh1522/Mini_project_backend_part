from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    dob = models.DateField()
    breakfast = models.TimeField()
    lunch = models.TimeField()
    dinner = models.TimeField()

    def __str__(self):
        return self.name



class Schedule(models.Model):
    day = models.CharField(max_length=20)
    # pill1_time = models.

    def __str__(self):
        return self.name


class Medicine(models.Model):

    REPEAT_CHOICES = (("daily", "Daily"), ("alter", "Alternate"))

    medicine_id = models.AutoField(primary_key="True")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    person = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE)
    repeat = models.CharField(
        max_length=20, choices=REPEAT_CHOICES,  default="daily")
    before_breakfast = models.TimeField(null=True,blank=True)
    after_breakfast = models.TimeField(null=True,blank=True)
    before_lunch = models.TimeField(null=True,blank=True)
    after_lunch = models.TimeField(null=True,blank=True)
    before_dinner = models.TimeField(null=True,blank=True)
    after_dinner = models.TimeField(null=True,blank=True)
    
    count=models.IntegerField(default=0)
    dosage=models.IntegerField(default=1)

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    INTEGER_CHOICES = (("true", "True"), ("false", "False"))
    
    time=models.TimeField(auto_now=True)
    
    date=models.DateField()
    medicine=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    before_breakfast = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)
    after_breakfast = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)
    before_lunch = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)
    after_lunch = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)
    before_dinner = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)
    after_dinner = models.CharField(max_length=20,choices=INTEGER_CHOICES, null=True)

