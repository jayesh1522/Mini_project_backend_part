import datetime as dt
from email import message
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.utils import json
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

# Create your views here.
from .serializers import *
from .models import *

class MedicineView(APIView):
    medicine_serialzer=MedicineSerializer
    
    
    def get(self, request,*args,**kwargs):
        
        try:
            medicine_id=kwargs.get('medicine_id')
            qs=Medicine.objects.all()
            qs=self.medicine_serialzer(qs.get(medicine_id=medicine_id)).data
           
            return(
                Response(qs,status=HTTP_200_OK
                )
            )
        except:
            try:
                qs=Medicine.objects.all()
                serializer=self.medicine_serialzer(qs,many=True)
                return Response({
                            "data":serializer.data,
                            "message":"Medicine List"
                        },
                        status=HTTP_200_OK)
            except:
                return Response({

                            "message":"Not Found"
                        },
                        status=HTTP_404_NOT_FOUND)
        
        
    def post(self,request):
        n=30
        name=request.data.get('name')
        description=request.data.get('description')
        repeat=request.data.get('repeat')
        medicine_id=request.data.get('medicine_id')
        count=request.data.get('count')
        dosage=request.data.get('dosage')
       
        
        
        
        

        try:
            
            person=UserInfo.objects.get(user_id=request.data.get('person'))
            pre_medicine=Medicine.objects.get(medicine_id=medicine_id)
            
            pre_medicine.before_breakfast=(dt.datetime.combine(dt.date(1,1,22),person.breakfast)-dt.timedelta(minutes=n)).time() if request.data.get('before_breakfast')=="True" else None
            pre_medicine.after_breakfast=(dt.datetime.combine(dt.date(1,1,22),person.breakfast)+dt.timedelta(minutes=n)).time() if request.data.get('after_breakfast')=="True" else None
            pre_medicine.before_lunch=(dt.datetime.combine(dt.date(1,1,22),person.lunch)-dt.timedelta(minutes=n)).time() if request.data.get('before_lunch')=="True" else None
            pre_medicine.after_lunch=(dt.datetime.combine(dt.date(1,1,22),person.lunch)+dt.timedelta(minutes=n)).time() if request.data.get('after_lunch')=="True" else None
            pre_medicine.before_dinner=(dt.datetime.combine(dt.date(1,1,22),person.dinner)-dt.timedelta(minutes=n)).time() if request.data.get('before_dinner')=="True" else None
            pre_medicine.after_dinner=(dt.datetime.combine(dt.date(1,1,22),person.dinner)+dt.timedelta(minutes=n)).time() if request.data.get('after_dinner')=="True" else None
            
            
           
                
            
            if name is not None and name!="":
                pre_medicine.name=name
            if description is not None and description!="":
                pre_medicine.description=description
            if repeat is not None and repeat!="":
                pre_medicine.repeat=repeat
            if count is not None and count !="":
                pre_medicine.count=count
            if dosage is not None and dosage !="":
                pre_medicine.dosage=dosage
                
            pre_medicine.save()
            product=pre_medicine
            
            return Response({
                        'status': True,
                        'message': 'Medicine data Updated',
                        'medicine':self.medicine_serialzer(product).data
                    },
                    status=HTTP_201_CREATED)
            
        except:
            try: 
                person=UserInfo.objects.get(user_id=request.data.get('person'))
                
                before_breakfast=(dt.datetime.combine(dt.date(1,1,22),person.breakfast)-dt.timedelta(minutes=n)).time() if request.data.get('before_breakfast')=="True" else None
                after_breakfast=(dt.datetime.combine(dt.date(1,1,22),person.breakfast)+dt.timedelta(minutes=n)).time() if request.data.get('after_breakfast')=="True" else None
                before_lunch=(dt.datetime.combine(dt.date(1,1,22),person.lunch)-dt.timedelta(minutes=n)).time() if request.data.get('before_lunch')=="True" else None
                after_lunch=(dt.datetime.combine(dt.date(1,1,22),person.lunch)+dt.timedelta(minutes=n)).time() if request.data.get('after_lunch')=="True" else None
                before_dinner=(dt.datetime.combine(dt.date(1,1,22),person.dinner)-dt.timedelta(minutes=n)).time() if request.data.get('before_dinner')=="True" else None
                after_dinner=(dt.datetime.combine(dt.date(1,1,22),person.dinner)+dt.timedelta(minutes=n)).time() if request.data.get('after_dinner')=="True" else None
               
                product=Medicine.objects.create(
                    name=name,
                    description=description,
                    person=person,
                    repeat=repeat,
                    before_breakfast=before_breakfast,
                    after_breakfast=after_breakfast,
                    before_lunch=before_lunch,
                    after_lunch=after_lunch,
                    before_dinner=before_dinner,
                    after_dinner=after_dinner,
                    count=count,
                    dosage=dosage,
                    )

                return Response({
                            'status': True,
                            'message': 'Medicine data Uploaded',
                            'medicine':self.medicine_serialzer(product).data
                        },
                        status=HTTP_201_CREATED)
            except :
                return Response({
                            'status': False,
                            'message': 'Data not Uploaded',

                        },
                        status=HTTP_400_BAD_REQUEST)
            
            

        
            
class UserInfoView(APIView):
    user_serializer=UserInfoSerializer
    
    
    def get(self,request,*args,**kwargs):
        try:
            userid=request.data.get('user_id')
        
            user_data=UserInfo.objects.filter(user_id=userid).get()

            return Response({
                        "status":True,
                        "data":"user data",
                        "detail":self.user_serializer(user_data).data
                    },
                    status=HTTP_200_OK)
        except:
            return Response({
                        "message":"User not Found"
                    },
                    status=HTTP_404_NOT_FOUND)
    
    def post(self,request):
        print(request.data)
        name=request.data.get('name')
        email=request.data.get('email')
        dob=request.data.get('dob')
        breakfast=request.data.get('breakfast')
        lunch=request.data.get('lunch')
        dinner=request.data.get('dinner')
        user_id=request.data.get("user_id")
        try:
            pre_user=UserInfo.objects.get(user_id=user_id)

            if name is not None and name!="":
                pre_user.name=name
            if email is not None and email!="":
                pre_user.email=email
            if dob is not None and dob!="":
                pre_user.dob=dob
            if breakfast is not None and breakfast!="":
                pre_user.breakfast=breakfast
            if lunch is not None and lunch!="":
                pre_user.lunch=lunch
            if dinner is not None and dinner!="":
                pre_user.dinner=dinner

            pre_user.save()

          


            person=pre_user
            n=30

            medicine1=Medicine.objects.filter(person=user_id)

            medicine1.exclude(before_breakfast=None).update(
                before_breakfast=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(breakfast,"%H:%M:%S").time())-dt.timedelta(minutes=n)).time())
            medicine1.exclude(after_breakfast=None).update(
                after_breakfast=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(breakfast,"%H:%M:%S").time())+dt.timedelta(minutes=n)).time())

            medicine1.exclude(before_lunch=None).update(
                before_lunch=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(lunch,"%H:%M:%S").time())-dt.timedelta(minutes=n)).time())
            medicine1.exclude(after_lunch=None).update(
                after_lunch=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(lunch,"%H:%M:%S").time())+dt.timedelta(minutes=n)).time())

            medicine1.exclude(before_dinner=None).update(
                before_dinner=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(dinner,"%H:%M:%S").time())-dt.timedelta(minutes=n)).time())
            medicine1.exclude(after_dinner=None).update(
                after_dinner=(dt.datetime.combine(
                    dt.date(1,1,22),dt.datetime.strptime(dinner,"%H:%M:%S").time())+dt.timedelta(minutes=n)).time())

            return Response({
                            "status":True,
                            "message":"data Updated",
                            "user":self.user_serializer(person).data
                        },
                        status=HTTP_201_CREATED)

        except:    
            try:
                person=UserInfo.objects.create(
                    name=name,
                    email=email,
                    dob=dob,
                    breakfast=breakfast,
                    lunch=lunch,
                    dinner=dinner,
                )
                return Response({
                            "status":True,
                            "message":"data uploaded",
                            "user":self.user_serializer(person).data
                        },
                        status=HTTP_201_CREATED)

            except:
                return Response({
                            "status":False,
                            "message":"data not uploaded",
                        },
                        status=HTTP_400_BAD_REQUEST)
    
  
        

            
            
class MedicalRecordView(APIView):
    serializer=MedicalRecordSerializer
    
    def get(self,request):
        print(request.data)
        print(request.GET.get("date"))
        date=request.GET.get("date")
        
        # date=request.data.get("date")
        try:
            qs=MedicalRecord.objects.filter(date=date).order_by("medicine")
            records=self.serializer(qs, many=True).data
            return(Response({"status":True,
                             "message":"Medical Records",
                             "date":date,
                             "data":records},status=HTTP_200_OK))
        except:
            return(Response({"status":False,
                             "message":"Not Found"},status=HTTP_404_NOT_FOUND))
    
    def post(self,request):
        print(request)
        before_breakfast=request.data.get("before_breakfast")
        after_breakfast=request.data.get("after_breakfast")
        before_lunch=request.data.get("before_lunch")
        after_lunch=request.data.get("after_lunch")
        before_dinner=request.data.get("before_dinner")
        after_dinner=request.data.get("after_dinner")
        
        date=dt.date.today()
        
        medicine=request.data.get("medicine")
        # medicine=Medicine.objects.get(medicine_id=request.data.get("medicine"))
        
        try:
            
                pre_record=MedicalRecord.objects.get(date=date,medicine__medicine_id=medicine)

                if before_breakfast is not None and before_breakfast!="":
                    pre_record.before_breakfast=before_breakfast
                if after_breakfast is not None and after_breakfast!="":
                    pre_record.after_breakfast=after_breakfast
                if before_lunch is not None and before_lunch!="":
                    pre_record.before_lunch=before_lunch
                if after_lunch is not None and after_lunch!="":
                    pre_record.after_lunch=after_lunch
                if before_dinner is not None and before_dinner!="":
                    pre_record.before_dinner=before_dinner
                if after_dinner is not None and after_dinner!="":
                    pre_record.after_dinner=after_dinner

                pre_record.save()
                medical_record=pre_record
                
                return(Response({"status":True,
                         "message":"Data Uploaded",
                         "record":self.serializer(medical_record).data},status=HTTP_201_CREATED))
            
            
        except:
            try:
                medicine=Medicine.objects.get(medicine_id=medicine)
                medical_record=MedicalRecord.objects.create(date=date,
                                                            medicine=medicine,
                                                            before_breakfast=before_breakfast,
                                                            after_breakfast=after_breakfast,
                                                            before_lunch=before_lunch,
                                                            after_lunch=after_lunch,
                                                            before_dinner=before_dinner,
                                                            after_dinner=after_dinner)
                return(Response({"status":True,
                         "message":"Data Uploaded",
                         "record":self.serializer(medical_record).data},status=HTTP_201_CREATED))
            
            except:
                return Response({
                            "status":False,
                            "message":"data not uploaded",
                        },
                        status=HTTP_400_BAD_REQUEST)