from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    def get(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = self.get_serializer(items, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    def get(self, request, pk):    
        items =  get_object_or_404(Menu, pk=pk)
        serializer = self.get_serializer(items)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        items =  get_object_or_404(Menu, pk=pk)
        serializer = self.get_serializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        items = get_object_or_404(Menu, pk=pk)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
