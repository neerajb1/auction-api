from django.contrib import admin

# Register your models here.
from .models import AuctionItem ,  Bid , UserDetail

admin.site.register(AuctionItem)
# admin.site.register(AuctionImage)
admin.site.register(Bid)
admin.site.register(UserDetail)
