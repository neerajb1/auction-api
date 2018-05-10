from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings


class AuctionItem(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(default=datetime.now )
    end_time = models.DateTimeField(default=datetime.now )
    price = models.DecimalField(decimal_places=2, max_digits=20,null=True, blank=True)
    image = models.ImageField(upload_to = "auctionItem/")

    def __str__(self):
	       return self.name
    
class UserDetail(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	email = models.EmailField(unique=True)
	full_name = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.email

class Bid(models.Model):
    auct = models.ForeignKey(AuctionItem , null=True, blank=True)
    user = models.ForeignKey(UserDetail, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    total_bids = models.IntegerField(default=0)

    def __str__(self):
	       return self.user.full_name
