import random

from models.entity.entity import Entity
from models.feature.feature import Feature


class Character(Entity):
    def __init__(self, category, name, life, level, pos):
        super().__init__(name, life, level, pos)
        self.maxLevel = 20
        self.maxLife = 10
        self.currentExp = 0
        self.maxExp = 10
        self.pos = pos
        self.category = category
        self.features = self.associateFeature()

    def updateMaxLife(self):
        self.maxLife += random.randint(0, 5)

    def levelUp(self, exp):
        self.currentExp += exp
        if self.currentExp >= self.maxExp:
            self.level += 1
            self.currentExp -= self.maxExp
            self.updateMaxExp()

    def updateMaxExp(self):
        self.maxExp += round(self.maxExp * 0.3 + self.level, 0)

    @staticmethod
    def associateFeature():
        features = {}
        for feature in Feature:
            features.__setitem__(feature.name, 0)
        return features
