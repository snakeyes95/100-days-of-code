class PlayerClass():
    membership_fees=True #class attribute object
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def practice_game(self):
        if (PlayerClass.membership_fees):
            print('Practicing')
    
    @classmethod
    def add_scores(cls,score1,score2):
        return cls('Andy',score1+score2)
    
    @staticmethod
    def add_scores2(score1,score2):
        return (score1+score2)






if __name__ == '__main__':
    Player1=PlayerClass('Alex',50)
    Player1.practice_game()

    Player2=PlayerClass.add_scores(30,50)
    Player2.practice_game()

    print(PlayerClass.add_scores2(30,70))
