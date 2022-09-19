
from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel): 

  class RoomKindChoices(models.TextChoices): 
    ENTIRE_PLACE = ("entire_place", "Entire Place")
    PRIVATE_ROOM = ("private_room", "Private Room")
    SHARED_ROOM = "shared_room", "Shared Room"

  # Room Mode Definition
  name = models.CharField(max_length=180, default="")
  country = models.CharField(max_length=50, default="한국",)
  city = models.CharField(max_length=80, default="대구",)
  price = models.PositiveIntegerField()
  toilets = models.PositiveIntegerField()
  rooms = models.PositiveIntegerField()
  descriptions = models.TextField()
  address = models.CharField(max_length=200), 
  pet_friendly = models.BooleanField(default=False,)
  kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
  owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")
  amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
  category = models.ForeignKey("categories.Category",null=True,  on_delete=models.SET_NULL, related_name="rooms")

  def __str__(self): 
    return self.name
    
  def total_amenities(room): 
    return room.amenities.count()

  def rating(room): 
    count = room.reviews.count()
    if count == 0:
      return "No Reviews"
    else: 
      total_rating = 0 
      for review in room.reviews.all():
        total_rating += review.rating 
        return round(total_rating / count, 2)

 

class Amenity(CommonModel): 
  name = models.CharField(max_length=150, null=True)
  description = models.CharField(max_length=150, null=True, blank=True)

  def __str__(self): 
    return self.name

  class Meta: 
    verbose_name_plural = "Amenities"
  

