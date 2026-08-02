class Art_Gallery:
    def __init__(self,name,founder):
        self.name = name
        self.founder = founder
        self.paintings = []
        print("Gallery created")
    def add(self,painting):
        self.paintings.append(painting)
        print("Painting added")
    def remove(self,painting):
        if painting in self.paintings:
            self.paintings.remove(painting)
            print("Painting removed")
        else:
            print("Painting not owned")
    def display(self):
        print("Gallery name: ",self.name)
        if len(self.paintings) == 0:
            print("Empty Gallery")
        else:
            print("Paintings: ")
            for painting in self.paintings:
                print(painting)
    def __del__(self):
        print("Gallery deleted")

#User's playlist creation
user_input = input("Enter Gallery name: ")
user_name = input("Enter Gallery founder: ")
a1 = Art_Gallery(user_input,user_name)

#Menu
while True: 
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Leave")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        painting = input("Enter painting name: ")
        a1.add(painting)
    elif choice == 2:
        painting = input("Enter painting name: ")
        a1.remove(painting)
    elif choice == 3:
            a1.display()
    elif choice == 4:
        print("Left Gallery")
        break
    else:
        print("Invalid choice")
del a1