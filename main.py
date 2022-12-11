from models.categories.category import Category
from models.entities.entity import Entity

category = Category()
entity = Entity()
monsters = category.getMonsters()
heroes = category.getHeroes()

test = entity.loadEntity(1)
