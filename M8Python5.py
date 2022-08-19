class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname


    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
    def checks(self,p):
        print("Checks function")
        task = input("What task the character are going to perform(Write,climb,cook)")
        
        # For cooking a dish
        if task == "cook":
            if p.weaknesses == "small":
                print("The character can not cook")
                
            elif ('pan' in p.weapons) and ('groceries' in p.weapons):
                print("The character can cook")     
                
            else:
             print("The character will not Cook")
                
                
        # for climbing a mountain        
        elif task == "climb":
            if p.weaknesses != "slow":
                print("The character can not climb the mountain")
                
            elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
                print("The character can climb")
                
            else:
                print("The character will not climb a mountain")
                
        # For writing a book
        elif task == "write":
            if p.weaknesses != "confusion":
                print("The character can not write a book")
                
            elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
                print("The character can a write a book")
                
            else:
                print("The character will not write a book")
        
        
        

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
    
player1.checks(player1)
