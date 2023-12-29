import requests
import json

# Replace 'your_api_link' with the actual API link
api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(api_url)
data = json.loads(response.text)

# Extract the 'products' dictionary from the data
products_data = data.get('products', {})

# Sort the data by popularity in descending order
# sorted_data = sorted(products_data.values(), key=lambda item: int(item.get('popularity', 0)), reverse=True)
sorted_data = sorted(products_data.values(), key=lambda item: int(item.get('popularity', 0)), reverse=True)


# Print the sorted data
print("Title\t\t\t\t\tPrice\t\tPopularity")
print("-" * 80)
for item in sorted_data:
    title = item.get('title', '')
    price = item.get('price', '')
    popularity = item.get('popularity', '')
    print(f"{title[:30]:<50}\t${price}\t{popularity}")
