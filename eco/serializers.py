from rest_framework import serializers
from .models import Course, Ecocard, Ecosoviet


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        # lookup_field =


class EcoCardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ecocard
        fields = '__all__'


class EcoSovietListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ecosoviet
        fields = ['title', 'description']
