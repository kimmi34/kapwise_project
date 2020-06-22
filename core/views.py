from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from .serializers import UserSerializer,GeoSerializer,AddressSerializer,CompanySerializer
from .models import User,Geo,Company,Address
from rest_framework import status


def home(request):
    return render(request,'homepage.html')

class ViewAllUsers(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        users = User.objects.all()
        users_data = []
        for user in users:
            user_serializer = UserSerializer(user)
            user_data = user_serializer.data 

            comp = Company.objects.get(id = user.id)
            comp_serializer = CompanySerializer(comp)
            user_data['company'] = comp_serializer.data 

            add = Address.objects.get(id = user.id)
            add_serializer = AddressSerializer(add)
            user_data['address'] = add_serializer.data 

            geo = Geo.objects.get(id = user.id)
            geo_serializer = GeoSerializer(geo)
            user_data['address']['geo'] = geo_serializer.data 

            users_data.append(user_data)
        return Response(users_data)


class Get10UsersFromAPI(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        resp = requests.get('https://jsonplaceholder.typicode.com/users')
        resp_json = resp.json()

        for person in resp_json:

            user_id = person['id']

            geo_data = person['address']['geo']
            geo_data['id'] = user_id

            comp_data = person['company']
            comp_data['id'] = user_id

            add_data = person['address']
            add_data['id'] = user_id
            add_data['geo'] = user_id

            user_data = person 
            user_data['address'] = user_id
            user_data['company'] = user_id
           
            try:
                Geo.objects.get(id = user_id)
            except:
                geo_serializer = GeoSerializer(data = geo_data)
                if geo_serializer.is_valid():
                    geo_serializer.save()

            try:
                Address.objects.get(id = user_id)
            except:
                add_serializer = AddressSerializer(data = add_data)
                if add_serializer.is_valid():
                    add_serializer.save()
            
            try:
                Company.objects.get(id = user_id)
            except:
                comp_serializer = CompanySerializer(data = comp_data)
                if comp_serializer.is_valid():
                    comp_serializer.save()

            try:
                User.objects.get(id = user_id)
            except:
                user_serializer = UserSerializer(data = user_data)
                if user_serializer.is_valid():
                    user_serializer.save()
        
        return Response(resp.json())

class DeleteAllUsers(APIView):
    permission_classes = [AllowAny]
    def delete(self,request):
        geos = Geo.objects.all()
        for geo in geos:
            geo.delete()
        add = Address.objects.all()
        for a in add:
            a.delete()
        comp = Company.objects.all()
        for c in comp:
            c.delete()
        users = User.objects.all()
        for u in users:
            u.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteGivenUser(APIView):
    permission_classes = [AllowAny]
    def delete(self,request,id):
        try:
            user = User.objects.get(id = id)
            geo = Geo.objects.get(id = id)
            comp = Company.objects.get(id = id)
            add = Address.objects.get(id = id)
            user.delete()
            comp.delete()
            add.delete()
            geo.delete()
            return Response({'status':'User deleted successfully'})
        except:
            return Response({'error':"User with given id doesn't exist"})
        
class GetGivenUser(APIView):
    permission_classes = [AllowAny]
    user_data = {}
    def get(self,request,user_id):
        print(user_id)
        user = User.objects.get(id = user_id)
        user_serializer = UserSerializer(user)
        user_data = user_serializer.data 

        comp = Company.objects.get(id = user_id)
        comp_serializer = CompanySerializer(comp)
        user_data['company'] = comp_serializer.data 

        add = Address.objects.get(id = user_id)
        add_serializer = AddressSerializer(add)
        user_data['address'] = add_serializer.data 

        geo = Geo.objects.get(id = user_id)
        geo_serializer = GeoSerializer(geo)
        user_data['address']['geo'] = geo_serializer.data 

        return Response(user_data)

class PostUser(APIView):
    permission_classes = [AllowAny]
    def post(self,request):  
        try:    
            user_id = User.objects.all().order_by("-id")[0].id + 1
        except:
            user_id = 1
        print(user_id)
        given_data = request.data

        geo_data = given_data['address']['geo']
        geo_data['id'] = user_id

        comp_data = given_data['company']
        comp_data['id'] = user_id

        add_data = given_data['address']
        add_data['id'] = user_id
        add_data['geo'] = user_id

        user_data = given_data 
        user_data['address'] = user_id
        user_data['company'] = user_id
        user_data['id'] = user_id
           
        
        geo_serializer = GeoSerializer(data = geo_data)
        if geo_serializer.is_valid():
            geo_serializer.save()
        else:
            return Response(geo_serializer.errors)


        comp_serializer = CompanySerializer(data = comp_data)
        if comp_serializer.is_valid():
            comp_serializer.save()
        else:
            return Response(comp_serializer.errors)

        add_serializer = AddressSerializer(data = add_data)
        if add_serializer.is_valid():
            add_serializer.save()
        else:
            return Response(add_serializer.errors)
           
      
       
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User added'})
        else:
            return Response(user_serializer.errors)
        
        return Response({'message': 'Not added'})

        



        
       
