from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Orders
from dish.models import Dish
from restaurant.models import Restaurant
from .serializers import OrdersSerializer,CreateOrderSerializer,OrdersIDSerializer
import traceback

class OrdeManagement(APIView):
    def get(self,request):
        queryset = Orders.objects.all()
        serializer = OrdersSerializer(queryset, many=True)
        return Response({
            "message":serializer.data
        })
    
    def post(self,request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            Orders.objects.create(
                customer_name=serializer.validated_data['customer_name'],
                restaurant_name=Restaurant.objects.get(restaurant_id = serializer.validated_data['restaurant_name']),
                dish_name=Dish.objects.get(dish_id = serializer.validated_data['dish_name']),
                order_status='Pending'
            )
            return Response({
                "message":"Order has been created successfully",
                "dish":serializer.data
            })
        else:
            return Response({
                "message":"Failed to create order",
                "errors":serializer.errors
            })
        
class OrdeStatusManagement(APIView):
    def get(self,request,pk):
        queryset = Orders.objects.filter(order_id=pk)
        serializer = OrdersIDSerializer(queryset, many=True)
        return Response({
            "message":serializer.data
        })
    def patch(self,request,pk):
        try:
            print(request.data)
            Orders.objects.filter(order_id=pk).update(
                order_status=request.data['status']
            )
            
            return Response({
                "message":"status has been sucessfully updated",
            })
        except Exception as ex:
            print(ex,traceback.format_exc())
            return Response({
                "message":"Failed to Update the Order",
            })
    
    def delete(self,request,pk):
        try:
            Orders.objects.filter(order_id=pk).delete()
            return Response({
                "message":"Order has been sucessfully deleted",
            })
        except Exception as ex:
            
             return Response({
                "message":"Failed to delete the Order",
            })