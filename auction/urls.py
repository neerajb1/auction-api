"""auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from auctionApp.views import  AuctionItemListApiView , AuctionItemRetrieveApiView ,BidListApiView , BidRetrieveApiView, BidCreateApiView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/item/$', AuctionItemListApiView.as_view(), name='item_api'),
    url(r'^api/item/(?P<pk>\d+)$', AuctionItemRetrieveApiView.as_view(), name='item_detail_api'),
    url(r'^api/bid/$', BidListApiView.as_view(), name='bid_api'),
    url(r'^api/bid/create/$', BidCreateApiView.as_view(), name='bid_create_api'),
    url(r'^api/bid/(?P<pk>\d+)$', BidRetrieveApiView.as_view(), name='bid_detail_api'),
]
