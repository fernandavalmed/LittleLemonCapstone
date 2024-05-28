from rest_framework import serializers
from .models import Menu, Booking

from django.contrib.auth.models import User
from rest_framework import serializers

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


#define Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
     model = User
     fields = ['url', 'username', 'email', 'groups']