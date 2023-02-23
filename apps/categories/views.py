from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from apps.users.mixins import CustomLoginRequiredMixin
import random
# Create your views here.
class CategoryAdd(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):

        serializer = CategorySerializer()
        serializer.validate(request.data)

        color_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        request.data._mutable = True
        request.data['color_code'] = request.data['color_code'] if 'color_code' in request.data else color_code

        return self.create(request, *args, **kwargs)

class CategoryUpdate(CustomLoginRequiredMixin, generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

class CategoryDelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
                
class CategoryList(CustomLoginRequiredMixin, generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None
