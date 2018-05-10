from rest_framework import serializers
from .models import Bid , AuctionItem




class BidAppSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bid_detail_api')
    name = serializers.SerializerMethodField()
    class Meta:
        model = Bid
        fields = [  'url' ,
                    'id' ,
                    'total_bids',
                    'amount',
                    'name' ,
                ]
    def get_name(self, obj):
        return obj.user.full_name

class AuctionAppSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='item_detail_api')
    bid_set = BidAppSerializer(many=True, read_only=True)

    image= serializers.SerializerMethodField()
    class Meta:
        model = AuctionItem
        fields = [  'url' ,
                    'id' ,
                    'name',
                    'price',
                    'image',
                    'bid_set',
                ]
    def get_image(self, obj):
        try:
            image = obj.image.url
        except :
            image = None
        return image


    # def get_image(self, obj):
	#        return obj.productimage_set.first().image.url
class BidCreateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = [  'id',
                    'total_bids',
                    'amount',
                ]

class AuctionAppCreateSerializer(serializers.ModelSerializer):
    bids = BidCreateAppSerializer(many=True, read_only=True)

    image_uri = serializers.SerializerMethodField()
    class Meta:
        model = AuctionItem
        fields = [
                    'id' ,
                    'name',
                    'bids',
                    'image_uri',

                ]


    def create(self , validated_data):
        bids_data = validated_data.pop('bids')
        bid_model = Bid.objects.create( **bid_data)
        auctionItem = AuctionItem.objects.get_or_create(bids=auctionItem,**validated_data)
        return auctionItem
