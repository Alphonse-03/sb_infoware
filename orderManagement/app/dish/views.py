from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dish
from .serializers import DishSerializer,DishOrderSerializer

class DishManagement(APIView):
    def get(self,request):
        restaurant_id = request.GET.get('restaurant_id')
        if restaurant_id:
            queryset = Dish.objects.filter(restaurant_name__restaurant_id=restaurant_id)
        else:
            queryset = Dish.objects.all()
        serializer = DishSerializer(queryset, many=True)
        return Response({
            "message":serializer.data
        })
    
    def post(self,request):
        serializer = DishOrderSerializer(data=request.data)
        if serializer.is_valid():
            Dish.objects.create(**serializer.validated_data)
            return Response({
                "message":"Dish added successfully",
                "dish":serializer.data
            })
        else:
            return Response({
                "message":"Failed to add dish",
                "errors":serializer.errors
            })