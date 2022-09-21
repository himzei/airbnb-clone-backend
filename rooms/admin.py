from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_amdin, request, rooms):
  for room in rooms.all(): 
    room.price = 0 
    room.save()
  

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin): 
  actions = (reset_prices,)
  list_display = ("name", "price", "kind", "total_amenities", "rating", "owner", "created_at")
  list_filter = ("country", "city", "price", "rooms", "toilets", "pet_friendly", "kind", "amenities")
  search_fields = ("owner__username",)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin): 
  list_display = ("pk", "name", "description", "created_at", "updated_at" )
  readonly_fields = ("created_at", "updated_at")
