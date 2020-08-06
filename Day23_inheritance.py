class Player:
    online=True
    def __init__(self,name):
        self.name=name

    def sign_in(self):
        print('User logged in!')
    
class Archer(Player):
    def __init__(self,name,arrows):
        super().__init__(name)
        self.arrows=arrows
    
    def attack(self):
        print(f'using one of {self.arrows} arrows')
    
class Axe(Player):
    def __init__(self,name,axes):
        super().__init__(name)
        self.axe=axes

    def attack(self):
        print(f'Using one of {self.axe} axes')

    
if __name__ == '__main__':
    robin = Archer('robin',14)
    alex = Axe('axe',43)

    robin.sign_in()

    robin.attack()
    alex.attack()
