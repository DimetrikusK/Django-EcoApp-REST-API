from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CourseListSerializer, EcoCardListSerializer, EcoSovietListSerializer
from .models import Course, Ecocard, Ecosoviet
from .urls import *


class CourseListView(APIView):

    """Cписок курсов"""

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseListSerializer(course, many=True)
        return Response(serializer.data)

    """Передаем id курса для вывода спика карт"""

    def post(self, request):
        return redirect(reverse(f'eco:card', args=[request.data]))


class EcoCardListView(APIView):

    """Список карт"""

    def get(self, request, pk):
        card = Ecocard.objects.filter(coursenameid=pk)
        serializer = EcoCardListSerializer(card, many=True)
        return Response(serializer.data)

    """Передаем id карты для вывода списка советов"""

    def post(self, request, pk):
        return redirect(reverse(f'eco:soviet_list', args=[request.data]))


class EcoSovietListView(APIView):

    """Вывод советов"""

    def get(self, request, pk):
        soviet = Ecosoviet.objects.filter(cardnameid=pk)
        serializer = EcoSovietListSerializer(soviet, many=True)
        return Response(serializer.data)


# class EcoSovietDetailView(APIView):
#
#     def get(self, request, pk):
#         soviet = get_object_or_404(Ecosoviet, id=pk)
#         serializer = EcoSovietListSerializer(soviet)
#         return Response(serializer.data)


    #   Web морда

# class CourseView(ListView):
#     template_name = 'main.html'
#     context_object_name = 'list'
#
#     def get_queryset(self):
#         return Course.objects.all()
#
#
# class EcoCardView(LoginRequiredMixin, DetailView):
#     model = Course
#     template_name = 'detail_card.html'
#
#
# class EcoSovietListView(LoginRequiredMixin, DetailView):
#     model = Ecocard
#     template_name = 'list_soviet.html'
#
#
# class EcoSovietDetail(LoginRequiredMixin, DetailView):
#     model = Ecosoviet
#     template_name = 'detail_soviet.html'
