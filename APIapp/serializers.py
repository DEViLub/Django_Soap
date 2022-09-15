from dataclasses import fields
from rest_framework import serializers
from .models import Item

class ItemSerialiser(serializers.ModelSerializer):
    class Meta: #interMeta class
        model = Item
        fields = '__all__'
        