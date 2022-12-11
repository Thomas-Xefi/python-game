import sqlite3
from misc.generate_class import auto_generate_class


class Category:
    db = sqlite3.connect('pdoGames.db')
    cursor = db.cursor()
    className = 'Category'
    moduleName = 'models.categories.category'

    def __init__(self):
        self.id = None
        self.name = None
        self.isMonster = None
        self.spells = None
        self.weapon = None

    def getMonsters(self):
        self.cursor.execute("""SELECT * FROM categories where is_monster = ?""", (1,))
        monsters = self.cursor.fetchall()
        return monsters

    def getHeroes(self):
        self.cursor.execute("""SELECT * FROM categories where is_monster = ?""", (0,))
        heroes = self.cursor.fetchall()
        return heroes

    def loadCategory(self, id):
        self.cursor.execute("""SELECT * FROM categories where id = ?""", (id,))
        result = self.cursor.fetchone()
        category = auto_generate_class([result], self.moduleName, self.className)
        category[0].spells = self.getSpells(category[0].id)
        category[0].weapon = self.getWeapons(category[0].id)
        return category[0]

    def getSpells(self, id):
        self.cursor.execute(
            """SELECT spells.* FROM categories
             JOIN spells ON spells.category_id = categories.id
             where spells.category_id = ?""", (id,))
        results = self.cursor.fetchall()
        spells = auto_generate_class(results, 'models.spells.spell', 'Spell')
        return spells

    def getWeapons(self, id):
        self.cursor.execute(
            """SELECT cw.* FROM categories
             LEFT JOIN category_weapon as cw ON cw.category_id = categories.id
             where cw.category_id = ?""", (id,))
        weaponJoin = self.cursor.fetchall()
        self.cursor.execute(
            """SELECT weapons.* FROM weapons
             LEFT JOIN category_weapon as cw ON cw.weapon_id = weapons.id
             where cw.weapon_id = ?""", (weaponJoin[0][2],))
        results = self.cursor.fetchall()
        weapon = auto_generate_class(results, 'models.weapons.weapon', 'Weapon')
        return weapon[0]
