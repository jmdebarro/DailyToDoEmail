import random
class Goals:
    """Class that contains all the goals for the current day"""


    def fitnessActivities(self):
        act = ["Stretch", "Workout", "PT"]
        act.pop(random.randint(0,2))
        act.pop(random.randint(0,1))  
        return act[0]
    
    def mentalActivities(self):
        act = ["Meditate", "Read", "Research diet", "Study", "Personal project", "Research random"]
        act.pop(random.randint(0,5))
        act.pop(random.randint(0,4))
        act.pop(random.randint(0,3))
        act.pop(random.randint(0,2))
        self.three = act[0]
        self.four = act[1]
        return act
    
    def __init__(self):
        self.one = "walk"
        self.two = self.fitnessActivities()
        self.three = None
        self.four = None
        self.mentalActivities()
