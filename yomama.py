from adjs import adjective
from nouns import noun
#YO MAMA GENERATOR - really never makes sense but oh well

class Yomama:
    """Yomama object with joke inside"""
    def __init__(self):
        self.adj = adjective()
        self.noun_one = noun()
        self.noun_two = noun()

    def new_adj(self):
        self.adj = adjective()

    def new_nouns(self):
        self.noun_one = noun()
        self.noun_two = noun()

    def create_joke(self):
        return f'Yo Mama so {self.adj}, she thought {self.noun_one} was {self.noun_two}'
