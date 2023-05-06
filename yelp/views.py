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
            if list_object is not None:
                list_id = list_object.id
                queryset = ListItems.objects.filter(list=list_id)
                serializer = ListItemsSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                Response({'message':'No list found'}, status = status.HTTP_204_NO_CONTENT)
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
        # data = getResturants(params)
        data = [{"resturant_id":"Dpk5P5tY2uPXdU5anbJYsQ","resturant_name":"Earls Kitchen + Bar","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/lpk7Icd-qOfSb8BYpfdmfg/o.jpg","resturant_url":"https://www.yelp.com/biz/earls-kitchen-bar-mclean?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["American (New)","Cocktail Bars"],"resturant_rating":4.0,"resturant_address":["7902 Tysons One Pl","McLean, VA 22102"],"resturant_phone_number":"(703) 847-1870","resturant_distance":992.5591025074102},{"resturant_id":"oJLfppou07mHIpZt1Dg1Ag","resturant_name":"Fogo de Chão Brazilian Steakhouse","resturant_image":"https://s3-media4.fl.yelpcdn.com/bphoto/vPwctbY-qyLRGmOzuecbLQ/o.jpg","resturant_url":"https://www.yelp.com/biz/fogo-de-chao-brazilian-steakhouse-tysons-7?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Steakhouses","Brazilian"],"resturant_rating":4.0,"resturant_address":["1775 Tysons Blvd","Ste 50","Tysons, VA 22102"],"resturant_phone_number":"(703) 556-0200","resturant_distance":571.4442103601776},{"resturant_id":"Lv0ldjgioQJMQi7fsVQ7xg","resturant_name":"North Italia - McLean","resturant_image":"https://s3-media1.fl.yelpcdn.com/bphoto/qHsM1DHphtR4jdnVGg2o6A/o.jpg","resturant_url":"https://www.yelp.com/biz/north-italia-mclean-mclean-2?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Italian","Pizza","Cocktail Bars"],"resturant_rating":4.0,"resturant_address":["1651 Boro Pl","McLean, VA 22102"],"resturant_phone_number":"(571) 765-2070","resturant_distance":841.5086598299506},{"resturant_id":"25drr0ej_Lp0xQrvIU2rjg","resturant_name":"Eddie V's Prime Seafood","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/RNVXOoqpyTXudwCzmvCkZg/o.jpg","resturant_url":"https://www.yelp.com/biz/eddie-vs-prime-seafood-mclean-4?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Seafood","Steakhouses","Lounges"],"resturant_rating":4.0,"resturant_address":["7900 Tysons One Pl","Mclean, VA 22102"],"resturant_phone_number":"(703) 442-4523","resturant_distance":1042.1675044608876},{"resturant_id":"trR4kHhXqK7eol8kMEAk-A","resturant_name":"Andy’s Pizza - Tysons","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/1P0jdWTvoMg1rJsbiVKxIA/o.jpg","resturant_url":"https://www.yelp.com/biz/andy-s-pizza-tysons-mclean-3?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Pizza","Beer Bar"],"resturant_rating":4.5,"resturant_address":["2001 International Dr","McLean, VA 22102"],"resturant_phone_number":"(703) 775-2212","resturant_distance":528.581915291289},{"resturant_id":"MR30ZkWTWxWUaY2CHKZBMw","resturant_name":"Wildfire","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/L6-ToXR6r1qaVgBBE8yd6g/o.jpg","resturant_url":"https://www.yelp.com/biz/wildfire-mclean-12?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Steakhouses","American (Traditional)","Wine Bars"],"resturant_rating":3.5,"resturant_address":["2001 International Dr","McLean, VA 22102"],"resturant_phone_number":"(703) 442-9110","resturant_distance":400.44249266516306},{"resturant_id":"D-RWa2Ans-ZhaFR3FbPUhg","resturant_name":"Founding Farmers - Tysons","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/COQ2RuA09tpUviI7tBGqoA/o.jpg","resturant_url":"https://www.yelp.com/biz/founding-farmers-tysons-tysons-6?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Bars","American (New)","Breakfast & Brunch"],"resturant_rating":3.5,"resturant_address":["1800 Tysons Blvd","Tysons, VA 22102"],"resturant_phone_number":"(703) 442-8783","resturant_distance":617.6076121538458},{"resturant_id":"qO6JzOPfPvlh6hOGcbcdLw","resturant_name":"Coastal Flats","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/pHQlUOUUQ3II5Jp9XocFNA/o.jpg","resturant_url":"https://www.yelp.com/biz/coastal-flats-mclean?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Seafood","Salad","American (Traditional)"],"resturant_rating":4.0,"resturant_address":["7860-L","Mclean, VA 22102"],"resturant_phone_number":"(703) 356-1440","resturant_distance":1223.1351402637251},{"resturant_id":"QgsCrTGlq_7R5IirExdnNw","resturant_name":"Agora Tysons","resturant_image":"https://s3-media1.fl.yelpcdn.com/bphoto/2bUAXqn909nDNF3gIobTqg/o.jpg","resturant_url":"https://www.yelp.com/biz/agora-tysons-tysons-2?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Mediterranean","Cocktail Bars","Turkish"],"resturant_rating":4.0,"resturant_address":["7911 Westpark Dr","Tysons, VA 22102"],"resturant_phone_number":"(703) 663-8737","resturant_distance":661.3694436066497},{"resturant_id":"XRTxsZTQVbPR35Sfq3iaAQ","resturant_name":"Hokkaido Ramen Santouka - Tysons Corner","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/o2WPYpxMcEE5J-x-Dkflrw/o.jpg","resturant_url":"https://www.yelp.com/biz/hokkaido-ramen-santouka-tysons-corner-tysons?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Ramen"],"resturant_rating":4.0,"resturant_address":["1636 Boro Pl","Tysons, VA 22102"],"resturant_phone_number":"(703) 857-0748","resturant_distance":875.3878673219173},{"resturant_id":"gdAUfrUdoYg9hx3vP30anA","resturant_name":"Randy's Prime Seafood and Steaks","resturant_image":"https://s3-media1.fl.yelpcdn.com/bphoto/_Q3PhrYHMFuAtimnxnUSkw/o.jpg","resturant_url":"https://www.yelp.com/biz/randy-s-prime-seafood-and-steaks-vienna?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["American (New)","Seafood","Steakhouses"],"resturant_rating":4.5,"resturant_address":["8051 Leesburg Pike","Vienna, VA 22182"],"resturant_phone_number":"(703) 552-5110","resturant_distance":1803.2441016161831},{"resturant_id":"iAwv3mCOXIeqf2Z389RZWA","resturant_name":"Circa at The Boro","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/i5qKq8Olq1nZ2mPwtLDtbg/o.jpg","resturant_url":"https://www.yelp.com/biz/circa-at-the-boro-tysons?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["American (New)","Sandwiches","Cocktail Bars"],"resturant_rating":4.5,"resturant_address":["1675 Silver Hill Dr","Tysons, VA 22102"],"resturant_phone_number":"(571) 419-6272","resturant_distance":870.8331296983188},{"resturant_id":"PG8xpIvwvX3ObPWefizI-g","resturant_name":"Patsy's American","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/hOESGQUjgmT0LmAUIQG7gg/o.jpg","resturant_url":"https://www.yelp.com/biz/patsys-american-vienna?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["American (Traditional)","Seafood","Cocktail Bars"],"resturant_rating":4.0,"resturant_address":["8051 Leesburg Pike","Vienna, VA 22182"],"resturant_phone_number":"(703) 552-5100","resturant_distance":1804.1356123536862},{"resturant_id":"qbT0H8xT4lSeFe_qhmJz-w","resturant_name":"Roll Play Grill","resturant_image":"https://s3-media4.fl.yelpcdn.com/bphoto/p390TRPlzOy177RIc7Z6bg/o.jpg","resturant_url":"https://www.yelp.com/biz/roll-play-grill-vienna-4?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Vietnamese"],"resturant_rating":4.5,"resturant_address":["8150 Leesburg Pike","Ste 100","Vienna, VA 22182"],"resturant_phone_number":"(703) 891-5665","resturant_distance":1304.9147017237055},{"resturant_id":"COzerevWBRDFKoloMYwkFw","resturant_name":"Lebanese Taverna","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/BEaFPS_Pt08sou9rtjCqfQ/o.jpg","resturant_url":"https://www.yelp.com/biz/lebanese-taverna-mclean?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Lebanese"],"resturant_rating":3.5,"resturant_address":["1840 G International Dr","Tysons Galleria","Mclean, VA 22102"],"resturant_phone_number":"(703) 847-5244","resturant_distance":505.044029022585},{"resturant_id":"sXTsbeCnUQV3kOk2faH7QA","resturant_name":"Rango’s Tex-Mex & Grill","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/jB3VNRqTJUVDZ3s8PJbImw/o.jpg","resturant_url":"https://www.yelp.com/biz/rango-s-tex-mex-and-grill-vienna-3?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Tex-Mex","Mexican"],"resturant_rating":4.5,"resturant_address":["1934 Old Gallows Rd","Vienna, VA 22182"],"resturant_phone_number":"(571) 282-3054","resturant_distance":1808.0802535074597},{"resturant_id":"dobS5m6QeZH4Ca17wshqMw","resturant_name":"Maggiano's Little Italy","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/TCO9pke0EQ20DBp5xamcpQ/o.jpg","resturant_url":"https://www.yelp.com/biz/maggianos-little-italy-mclean?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Italian","Bars"],"resturant_rating":3.5,"resturant_address":["2001 International Dr","McLean, VA 22102"],"resturant_phone_number":"(703) 356-9000","resturant_distance":535.7116137620227},{"resturant_id":"hxhmK2KSZovFPjf3zqC-Cw","resturant_name":"Cafe Ile","resturant_image":"https://s3-media4.fl.yelpcdn.com/bphoto/riNo3agp2HBpNJjnDHMS3A/o.jpg","resturant_url":"https://www.yelp.com/biz/cafe-ile-mclean?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Sushi Bars","Coffee & Tea","Desserts"],"resturant_rating":5.0,"resturant_address":["8270 Greensboro Dr","Ste 120","McLean, VA 22102"],"resturant_phone_number":"(571) 378-1168","resturant_distance":715.2647868647385},{"resturant_id":"AsAMGMxhRvuDFvqcWC6k7A","resturant_name":"El Bebe","resturant_image":"https://s3-media3.fl.yelpcdn.com/bphoto/2ssikdinIGp4jXW9lAKULg/o.jpg","resturant_url":"https://www.yelp.com/biz/el-bebe-tysons?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Tacos"],"resturant_rating":4.0,"resturant_address":["8354 Broad St","Tysons, VA 22102"],"resturant_phone_number":"(571) 378-0171","resturant_distance":888.0695373107912},{"resturant_id":"--XintCRRNpzSijy8KT98g","resturant_name":"Han Palace","resturant_image":"https://s3-media2.fl.yelpcdn.com/bphoto/0CM-tWYDgeu9T_9Vc-QZdQ/o.jpg","resturant_url":"https://www.yelp.com/biz/han-palace-mclean-3?adjust_creative=Hd_oPBarUTWLZGRcDWcPeQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Hd_oPBarUTWLZGRcDWcPeQ","resturant_categories":["Dim Sum","Cantonese"],"resturant_rating":3.0,"resturant_address":["7900 Westpark Dr","McLean, VA 22102"],"resturant_phone_number":"(571) 378-0162","resturant_distance":772.1418002452474}]
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


