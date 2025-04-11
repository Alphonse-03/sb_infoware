from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Restaurant
from .serializers import RestaurantSerializer,RestaurantAddSerializer
import traceback

class RestaurantsManagement(APIView):
    def get(self,request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response({
            "message":serializer.data
        })
    
    def post(self,request):
        serializer = RestaurantAddSerializer(data=request.data)
        if serializer.is_valid():
            Restaurant.objects.create(**serializer.validated_data)
            return Response({
                "message":"Restaurant added successfully",
                "dish":serializer.data
            })
        else:
            return Response({
                "message":"Failed to add Restaurant",
                "errors":serializer.errors
            })