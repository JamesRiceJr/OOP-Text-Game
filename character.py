class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
        
class Enemy(Character):
    
    def __init__(self, char_name,char_description):
      
      super().__init__(char_name,char_description)
      self.weakness = None
      
    def set_weakness(self, new_weakness):
        self.weakness = new_weakness
        
    def get_weakness(self):
        return self.weakness
        
    def fight(self, combat_item):
      if combat_item == self.weakness:
        print("You fend " + self.name + " off with the " + combat_item )
        return True
      else:
        print(self.name + " crushes you, puny adventurer")
        return False
        
    def bribe(self, money):
      if money >= 10 :
        print(self.name + " leaves you alone thanks for your bribe")
        return True
      else:
        print("That's not enough. How insulting!")
        self.fight("None")
        return False
    
class Friend(Character):
    
    def __init__(self, char_name,char_description):
      
      super().__init__(char_name,char_description)
      self.favorites = None
      
    def gift(self, item):
      if item in self.favorites:
        print("Thank you! This is great!")
        return True
      else:
        print("Uh...interesting choice. No thanks...")
        return False