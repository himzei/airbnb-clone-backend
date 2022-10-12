from rest_framework.test import APITestCase
from users.models import User
from . import models


# class TestAmenities(APITestCase):

#     NAME = "Amenity Test"
#     DESC = "Amenity Desc"
#     URL = "/api/v1/rooms/amenities/"

#     def setUp(self):
#         models.Amenity.objects.create(
#             name=self.NAME,
#             description=self.DESC
#         )

#     def test_all_amenities(self):

#         response = self.client.get(self.URL)
#         data = response.json()

#         self.assertEqual(response.status_code, 200, "Status code isn't 200")

#         self.assertIsInstance(data, list)
#         self.assertEqual(len(data), 1)
#         self.assertEqual(data[0]["name"], self.NAME)
#         self.assertEqual(data[0]["description"], self.DESC)

#     def test_create_amenity(self):

#         new_amenity_name = "New Amenity"
#         new_amenity_desc = "New Amenity Desc."

#         response = self.client.post(
#             self.URL, data={"name": new_amenity_name, "description": new_amenity_desc})
#         data = response.json()

#         self.assertEqual(response.status_code, 200, "Not 200 status code")

#         self.assertEqual(data["name"], new_amenity_name)
#         self.assertEqual(data["description"], new_amenity_desc)

#         response = self.client.post(self.URL)
#         self.assertEqual(response.status_code, 200)

#         self.assertIn("name", data)


class TestRooms(APITestCase):

    def test_get_room(self):

        response = self.client.get("/api/v1/rooms/")

        print(response.json())
