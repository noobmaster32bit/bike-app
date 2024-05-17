from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile_pictures", default="profile_picture.png")

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)
    year=models.PositiveIntegerField()
    km_driven=models.PositiveIntegerField()
    description=models.TextField(null=True)
    price=models.PositiveIntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    cat_options=(
        ("petrol_engine","petrol_engine"),
        ("diesel_engine","diesel_engine"),
        ("ev","ev")
    )
    category=models.CharField(max_length=200,choices=cat_options,null=True,blank=True,default=None)
    image=models.ImageField(upload_to="vehicle_images",default="vehicle.png",null=True,blank=True)
    is_sold=models.BooleanField(default=False)
    location=models.CharField(max_length=200,null=True,blank=True)
    ow_options=(
        ("first","first"),
        ("second","second"),
        ("third","third"),
        ("others","others")
    )
    owner_types=models.CharField(max_length=200,choices=ow_options,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

class Wishlist(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="wishlist")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

class WishListItem(models.Model):
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)
    wishlist_object=models.ForeignKey(Wishlist,on_delete=models.CASCADE,related_name="wishlistitem")
    vehicle_object=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

class Review(models.Model):
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_object=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    review_field=models.TextField(null=True,blank=True)
    rating=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

class Enquiry(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender_msg")
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver_msg")
    vehicle_object=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    message=models.TextField(null=True)
    is_read=models.BooleanField(default=False,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return 

def create_wishlist(sender,instance,created,**kwargs):
    if created:
        Wishlist.objects.create(owner=instance)
post_save.connect(create_wishlist,sender=User)


def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(name=instance)
post_save.connect(create_user_profile,sender=User)