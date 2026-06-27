name = input("What is your name?: ")
mood = input("What is your mood?(happy,sad,neutral): ")
level = input("What is your energy level?(High,Medium,Low): ")

if mood.lower() == "happy" and level.lower() == "high": #
    print("You should " + "play tag with friends," + name)
elif mood.lower() == "happy" and level.lower() == "medium":
    print("You should " + "hang out with buddies," + name)
elif mood.lower() == "happy" and level.lower() == "low": #
    print("You should " + "read a book," + name)
elif mood.lower() == "sad" and level.lower() == "high":
    print("You should " + "make a dance," + name)  
elif mood.lower() == "sad" and level.lower() == "medium": #
    print("You should " + "write a poem," + name)
elif mood.lower() == "sad" and level.lower() == "low": #
    print("You should " + "watch the stars, " + name)
elif mood.lower() == "neutral" and level.lower() == "high": #
    print("You should" + " do whatever you feel like," + name)
elif mood.lower() == "neutral" and level.lower() == "medium": #
    print("You should" + " chat with old friends" + name)
elif mood.lower() == "neutral" and level.lower() == "low": #
    print("You should" + " sleep," + name)
