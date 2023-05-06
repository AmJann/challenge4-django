from rest_framework import generics,status, views
from rest_framework.response import Response
from .serializers import *
from .models import *
from .requests import *
from user.models import *
import pandas as pd

class getListItems(generics.ListAPIView):
    def get(self,request):
        user_id = request.query_params.get('user_id', '')
        group_id = request.query_params.get('group_id', '')

        if user_id and group_id:
            list_object = List.objects.get(user = user_id, group = group_id)
            list_id = list_object.id
            queryset = ListItems.objects.filter(list=list_id)
            serializer = ListItemsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'message':'Invalid Group or user Id', 'user':user_id, 'group':group_id}, status = status.HTTP_400_BAD_REQUEST)



class createListItems(generics.CreateAPIView):
    def post(self,request):
        user= request.data.get('user_id')
        group= request.data.get('group_id')
        items = request.data.get('items')

        serializer = ListSerializer(data = {"group": group, "user": user})

        if serializer.is_valid():
            list_object = serializer.save()
            list_id = list_object.id

            for item in items:
                item['list'] = list_id

                item_serializer = ListItemsSerializer(data=item)

                if item_serializer.is_valid():
                    item_serializer.save()

                else:
                    return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'List and Item created successfully'}, status=status.HTTP_201_CREATED)



class UpdateItemAPIView(generics.UpdateAPIView):
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer

    def put(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        try:
            item = ListItems.objects.get(id=item_id)
        except ListItems.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteItemAPIView(generics.DestroyAPIView):
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer



class getResturantsData(views.APIView):
    def post(self,request):
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        params = {'latitude':latitude, 'longitude':longitude}
        data = getResturants(params)
        if type(data) == list:
            return Response({'data':data}, status=status.HTTP_200_OK)
        else:
            return Response({'error':data}, status=status.HTTP_400_BAD_REQUEST)


class getResturantsDataByIds(views.APIView):
    def post(self,request):
        user = request.data.get('user_id')
        group = request.data.get('group_id')
        list_id = List.objects.get(user=user, group =group)
        items = ListItems.objects.filter(list = list_id)

        if items:
            ids = [x.resturant_id for x in items]
            data = getResturantsbyId(ids)
            return Response({'data':data}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'No items found'}, status=status.HTTP_400_BAD_REQUEST)


class getSuggestion(generics.GenericAPIView):
    def post(self,request):
        users_list = request.data.get("users_list")
        group_id = request.data.get("group_id")
        group = Groups.objects.get(id = group_id)
        list = []
        response = {}
        for id in users_list:
            user = User.objects.get(id = id)
            if user and group:
                list_object = List.objects.get(user = id, group = group_id)
                if list_object:
                    list_id = list_object.id
                    queryset = ListItems.objects.filter(list=list_id)
                    serializer = ListItemsSerializer(queryset, many=True)
                    list += serializer.data

        df = pd.DataFrame(list)
        
        resturant = df.groupby('resturant_name').apply(lambda x: (x['user_rating'].astype(float) * len(x)).sum() / len(x)).sort_values(ascending=False)
        rated = df.groupby('resturant_name').apply(lambda x: (x['resturant_rating'].astype(float) * len(x)).sum() / len(x)).sort_values(ascending=False)
        df['resturant_categories'] = df['resturant_categories'].str.split(',')
        df['resturant_categories'] = df['resturant_categories'].explode(ignore_index = True)
        cusine = df.groupby('resturant_categories').apply(lambda x: (x['user_rating'].astype(float) * len(x)).sum() / len(x)).sort_values(ascending=False)
        response['favourite_cusine'] = cusine.index[0]
        response['favourite_resturant'] = resturant.index[0]
        response['best_rated'] = rated.index[0]

        if response:
            return Response({"message":"Here are the suggestions","data":response}, status = status.HTTP_200_OK)
        else:
            return Response({'error':'No items found'}, status=status.HTTP_400_BAD_REQUEST)


