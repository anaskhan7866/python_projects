import json



def load_data():
    try:
        with open('youtube.txt','r') as file:
            j_file = json.load(file)
            return j_file
        
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        # print("\n")
        print("-"*50)
        print(f"{index}. Video_Name: {video['name']}, Duration: {video['time']}") 
        # print("\n")
        print("-"*50)


def add_video(videos): 
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number which you want to update: "))
    if 1<=index<=len(videos):
        name = input("Enter new Name: ")
        time = input("Enter new Time: ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)

    else:
        print("Invalid index selected")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        print("\n")
        print(f"Video number {index} is deleted.")
        save_data_helper(videos)

    else:
        print("Enter the Index")




def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add youtube video")
        print("3. Update youtube video")
        print("4. Delete youtube video")
        print("5. Exit")

        choice = input("Enter the choice: ")

        # print(videos)


        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)

            case '5':
                print("Thanks use it again")
                break

            case _:
                print("\n Enter the valid choice!!!!!")


if __name__ == '__main__':
    main()