from rest_framework import serializers
from .models import User,Address,Company,Geo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address 
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo 
        fields = '__all__'