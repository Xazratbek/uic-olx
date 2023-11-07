# Delete

# import requests

# url = "http://127.0.0.1:8000/api/v1/ads/delete/6"  # Replace 1 with the actual ID
# response = requests.delete(url)

# if response.status_code == 204:
#     print("Successfully deleted the resource.")
# else:
#     print("Failed to delete the resource. Status code:", response.status_code)

# Create
# import requests

# # Define the URL where you want to create a new ad
# url = "http://127.0.0.1:8000/api/v1/ads/create/"

# # Define the data for the new ad (adjust this data according to your model)
# data = {
#     "title": "New Ad Title",
#     "image": None,  # Adjust to the image path
#     "price": 1000,
#     "content": "This is the content of the new ad.",
#     "sub_category": 1,  # Use the actual subcategory ID
#     "district": 1,  # Use the actual district ID
#     "is_top": True,
#     "is_vip": False,
#     "address": "123 Main Street",  # Adjust the address
#     "depth": 2,  # Adjust the depth value as needed
# }

# # Send a POST request to create the new ad
# response = requests.post(url, json=data)

# # Check the response status code
# if response.status_code == 201:
#     print("Ad created successfully.")
# else:
#     print("Failed to create ad. Status code:", response.status_code)
#     print("Response content:", response.text)

# Update

# import requests

# # Define the URL for updating an existing ad, replace <ad_id> with the actual ad ID
# ad_id = 1  # Replace with the ID of the ad you want to update
# url = f"http://127.0.0.1:8000/api/v1/ads/update/7/"

# # Define the updated data for the ad (adjust this data according to your model)
# data = {
#     "title": "Updated Ad Title",
#     "price": 1200,
#     "content": "This is the updated content of the ad.",
#     "sub_category": 1,  # Use the actual subcategory ID
#     "district": 1,
#     "is_top": False,
#     "is_vip": True,
#     "address": "456 Elm Street",  # Adjust the address
#     "depth": 3,  # Adjust the depth value as needed
# }

# # Send a PUT request to update the ad
# response = requests.put(url, json=data)

# # Check the response status code
# if response.status_code == 200:
#     print("Ad updated successfully.")
# else:
#     print("Failed to update ad. Status code:", response.status_code)
#     print("Response content:", response.text)

# import requests

# res = requests.get("https://064f-82-215-102-4.ngrok-free.app/api/v1/ads/1")
# r = res.json()
# print(r)
