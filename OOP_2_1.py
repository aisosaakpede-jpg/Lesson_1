

class Playlist:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print("Playlist created successfully")
    def add(self,song):
        self.songs.append(song)
        print("Songs added")
    def remove(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print("Song removed")
        else:
            print("Song not found")
    def display(self):
        print("Song name: ",self.name)
        print("Song genre: ",self.genre)
        if len(self.songs) == 0:
            print("No songs available")
        else:
            print("Songs: ")
            for song in self.songs:
                print(song)
    def __del__(self):
        print("Playlist deleted")

user_input = input("Enter playlist name: ")
user_genre = input("Enter genre: ")
p1 = Playlist(user_input,user_genre)
while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        song = input("Enter song name: ")
        p1.add(song)
    elif choice == 2:
        song = input("Enter song name: ")
        p1.remove(song)
    elif choice == 3:
            p1.display()
    elif choice == 4:
        print("Exit program")
        break
    else:
        print("Invalid choice")
del p1