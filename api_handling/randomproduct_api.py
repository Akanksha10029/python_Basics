import requests

def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    main_data = response.json()
    print(main_data)
    
    if main_data["success"] and "data" in main_data:
        userdata = main_data["data"]
        title = userdata["title"]
        description = userdata["description"]
        images = userdata["images"]
        price = userdata["price"]
        stock = userdata["stock"]
        return title, description, price, stock, images
    else:
        return "No Data Found"
    
def main():
    try:
        title, description, price, stock, images = fetch_random_product()
        print(f"Product: {title}\nPrice: {price}\nDescription of the product: {description}\nStock available: {stock} \nFew Images: {images}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    