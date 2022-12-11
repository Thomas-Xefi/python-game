from misc.generate_class import auto_generate_class
from models.categories.category import Category
import sqlite3

from models.features.feature import Feature


class Entity:
    db = sqlite3.connect('pdoGames.db')
    cursor = db.cursor()
    className = 'Entity'
    moduleName = 'models.entities.entity'

    def __init__(self):
        self.id = None
        self.name = None
        self.life = None
        self.maxLife = None
        self.exp = None
        self.maxExp = None
        self.level = None
        self.maxLevel = None
        self.category = None
        self.ability = None
        self.features = None

    def loadEntity(self, id):
        self.cursor.execute(
            """SELECT * FROM entities WHERE id = ?""", (id,))
        results = self.cursor.fetchall()
        entity = auto_generate_class(results, self.moduleName, self.className)
        entity[0].category = Category.loadCategory(Category(), entity[0].category)
        entity[0].features = Feature.getFeaturesByEntityId(Feature(), entity[0].id)
        return entity[0]
