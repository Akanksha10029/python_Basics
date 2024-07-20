import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute(''' 
    create table if not exists videos (
        id integer primary key,
        name text not null,
        time text not null
    )            
''')

def list_videos():
    cursor.execute("select * from videos")
    return cursor.fetchall()
        
def add_videos(name, time):
    cursor.execute("insert into videos (name, time) values (?, ?)", (name, time))
    conn.commit()

def update_videos(video_id,new_name, new_time):
    cursor.execute("update videos set name = ? , time = ? where id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("delete from videos where id = ? ", (video_id,))
    conn.commit()

def main():
    print("Welcome to the Youtube Video Database")
    while True:
        
        print("1. List videos")
        print("2. Add Videos")
        print("3. Update videos")
        print("4. Delete Video")
        print("5. Exit the App")
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_vid = list_videos()
                if not list_vid:
                    print("No videos in the database")
                else:
                    print("Videos in the database are: \n")
                    for video in list_vid:
                        print(f"ID: {video[0]}, Name: {video[1]}, Time:{video[2]}")
                
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_videos(name, time)
                
            case "3":
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_videos(video_id,name, time)
            
            case "4":
                video_id = input("Enter the video id to delete: ")
                delete_videos(video_id)
                
            case "5":
                print("Thank you for using Youtube Manager")
                break
            
            case _:
                print("Invalid choice")
    conn.close()

if __name__ == "__main__":
    main()