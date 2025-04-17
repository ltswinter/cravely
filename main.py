print("Welcome to Cravely!")

class Craving:
    def __init__(self, name, healthy_swap, reason):
        self.name = name
        self.healthy_swap = healthy_swap
        self.reason = reason
        
    def display(self):
        return f'If you are craving {self.name}, you should try {self.healthy_swap} instead because {self.reason}!'
        
snack = Craving("chips", "popcorn", "it is lower in calories so you can eat more while feeling fuller due to the fiber")
print(snack.display())