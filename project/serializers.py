from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #Campos que seran consultados 
        fields = ('id', 'title' ,'description', 'technology', 'create_at',)
        #Campos de solo lectura 
        read_only_fields = ('create_at',)