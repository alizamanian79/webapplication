from django.shortcuts import render  
from rest_framework import status  
from rest_framework.request import Request  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from .serializers import ShopSerializer  
from django.contrib.auth import get_user_model  
from django.shortcuts import get_object_or_404


from .models import Shop  

User = get_user_model()  

class ShopListView(APIView):  

    def get(self, request: Request, *args, **kwargs):  
        # Filter shops for the authenticated user and only active ones.  
        shops = Shop.objects.filter(active=True, owner=request.user)  

        # Serialize the data  
        serializer = ShopSerializer(shops, many=True)  
        
        # Return the response  
        return Response(serializer.data, status=status.HTTP_200_OK)

class ShopCreateView(APIView):  

    def get(self, request, *args, **kwargs):
        blueprint = {
            'message': 'This is a new shop api',
            'method': 'POST',
            'properties': {
                'title': 'فروشگاه مینایی',
                'description': 'عرضه کننده لوازم ارایشی',
                'address':'نیاوران',
                'owner':1,
                'active': True
            },
        }
        return Response(blueprint, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        serializer=ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{"message":"Item Added Successfuy"})
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ShopRetrieveView(APIView):

    def get(self, request, slug, *args, **kwargs):
        shop = get_object_or_404(Shop, slug=slug)
        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ShopUpdateView(APIView):  
    def get(self, request, *args, **kwargs):
        blueprint = {
            'message': 'Send shop id from url',
            'method': 'PUT',
            'properties': {           
                'title': 'فروشگاه مینایی',
                'description': 'عرضه کننده لوازم ارایشی',
                'address':'نیاوران',
                'slug':"فروشگاه-مینایی",
                'owner':1,
                'active': True
            },
        }
        return Response(blueprint, status=status.HTTP_200_OK)
    def put(self, request,pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        serializer=ShopSerializer(shop, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ShopDeleteView(APIView):  
    def get(self, request, *args, **kwargs):
        blueprint = {
            'message': 'Send shop id from url to delete',
            'method': 'DELETE',
            'properties': {},
        }
        return Response(blueprint, status=status.HTTP_200_OK)
    def delete(self, request, pk, *args, **kwargs):
        shop = get_object_or_404(Shop, pk=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 