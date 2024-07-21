import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    main_data = response.json()
    print(main_data)
    
    if main_data["success"] and "data" in main_data:
        user_data = main_data["data"]
        user_name = user_data["login"]["username"]
        # print(f"username: {user_name}")
        country_name = user_data["location"]["country"]
        # print(f"country: {country_name}")
        return user_name,country_name
        
    else:
        print("Error")
    
def main():
    try:
        username, usercountry = fetch_random_user()
        print(f"Username: {username}\nCountry: {usercountry}")
            
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
        