import random
class Intelligence(): 

    drawnCardsHistory = []

    """Initialize Ai player object"""
    def __init__(self, intelligence):
        self.intelligence = intelligence
        

    """ Easy mode: randomize surrender decision"""
    def decideSurrenderEasyMode():
        surrender = False
        surrender = random.choice([True, False])
        return surrender
    
    

    

        



            
    
