import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        
def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        if "title" in video and "time" in video:
            print(f'{index}. {video["title"]}, Duration: {video["time"]}')
        else:
            print(f'{index}. Video details incomplete')
    print("\n")
    print("*"*50)
    
def add_video(videos):
    title = input('Enter the title of the video: ')
    time = input("Enter video time: ")
    videos.append({"title": title, "time": time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        title = input('Enter the title of the video: ')
        time = input("Enter video time: ")
        videos[index-1]["title"] = title
        videos[index-1]["time"] = time
        save_data_helper(videos)
    else:
        print("Invalid index")
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index-1)
        save_data_helper(videos)
        print(f'Deleted video: {deleted_video["title"]}, Duration: {deleted_video["time"]}')
    else:
        print("Invalid index")
    

def main():
    videos =load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube Videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        # print(videos)

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print("Thank you for using Youtube Manager")
                break
            case _:
                print("Invalid choice")

if __name__== "__main__":
    main()


