import requests

def fetch_random_books(page, limit):
    url = "https://api.freeapi.app/api/v1/public/books"
    
    params = {
        "page": page,
        "limit": limit
    }
    response = requests.get(url, params = params)
    main_data = response.json()
    print(main_data)
    
    if main_data["success"] and "data" in main_data:
        book_data = main_data["data"]
        page = book_data["page"]
        limit = book_data["limit"]
        return book_data, page, limit
    else:
        return "No data Found"

def main():
    page = int(input("Enter the page number: "))
    limit = int(input("Enter the limit: "))    
    
    try:
        book_data, page, limit = fetch_random_books(page, limit)
        if book_data != "No data found":
            print(f"Page: {page}\nLimit: {limit}")
            for book in book_data["data"]:
                print(f"Kind: {book.get('kind', 'N/A')}")
                print(f"ID: {book.get('id', 'N/A')}")
                print(f"Etag: {book.get('etag', 'N/A')}")
                volume_info = book.get('volumeInfo', {})
                print(f"Title: {volume_info.get('title', 'No title available')}")
                print(f"Authors: {', '.join(volume_info.get('authors', []))}")
                print(f"Publisher: {volume_info.get('publisher', 'publisher data is not available')}")
                print(f"Published data: {volume_info.get('publishedDate', 'N/A')}")
                print(f"Description: {volume_info.get('description', 'No description available')}")
                
        else:
            print("Failed to fetch books data.")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()              