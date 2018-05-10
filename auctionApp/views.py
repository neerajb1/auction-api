from django.shortcuts import render
from django.contrib.auth.models import User
from .models import AuctionItem ,Bid
from .serializers import AuctionAppSerializer ,BidAppSerializer ,BidCreateAppSerializer
from rest_framework import generics
# Create your views here.
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,

    )

class AuctionItemListApiView(generics.ListAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionAppSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = (IsAdminUser,)

class AuctionItemRetrieveApiView(generics.RetrieveAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionAppSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class BidListApiView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidAppSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = (IsAdminUser,)

class BidRetrieveApiView(generics.RetrieveAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidAppSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BidCreateApiView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidCreateAppSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self , serializers):
        serializers.save(user=self.request.user)
