from random import randint

class Die():

    def __init__(self,num_slides=6):
        """骰子的面数默认为6"""
        self.num_slides = num_slides

    def roll(self):
        """返回一个面的面数"""
        return randint(1, self.num_slides)