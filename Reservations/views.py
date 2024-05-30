from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer, UserSerializer

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

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
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
        
        
# This viewset method allows GET and POST methods
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    

