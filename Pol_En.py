
class Cricket:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print("Cricket player: ",self.__player)
        print("Score: ",self.__score)
    def play(self):
        print(self.__player," is playing cricket")
    def set_score(self,score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid score")

class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print("Football player: ",self.__player)
        print("Score: ",self.__score)
    def play(self):
        print(self.__player," is playing football")
    def set_score(self,score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid score")

cric = Cricket("Claude",5)
foot = Football("Messi",10)

sports = [cric,foot]
for i in sports:
    i.info()
    i.play()
    print()

cric.__score = -20
print("After direct change attempt: ")
cric.info()

cric.set_score(120)
print("After setter update")
cric.info()