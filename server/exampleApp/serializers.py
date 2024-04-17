from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        return "rishav"
    
    class Meta:
        model = Customer
        fields = ["pk", "name", "email", "created"]

