import random
class dice:
    def roll(self):
        playerone = random.randint(1,6)
        playertwo = random.randint(1,6)
        return f"1st player has {playertwo} and 2nd player has {playertwo}"