import sqlite3

oConnection = sqlite3.connect('pdoGames.db')
oCurseur = oConnection.cursor()

# region Drop table
oCurseur.execute('''Drop table IF EXISTS categories''')
oCurseur.execute('''Drop table IF EXISTS weapons''')
oCurseur.execute('''Drop table IF EXISTS spells''')
oCurseur.execute('''Drop table IF EXISTS features''')
oCurseur.execute('''Drop table IF EXISTS entities''')
oCurseur.execute('''Drop table IF EXISTS abilities''')
oCurseur.execute('''Drop table IF EXISTS entity_feature''')
oCurseur.execute('''Drop table IF EXISTS category_weapon''')
oCurseur.execute('''Drop table IF EXISTS ability_entity''')
# endregion

# region Create table
oCurseur.execute('''CREATE TABLE categories(
   /* définition des champs */
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name VARCHAR(50) NOT NULL,
   is_monster boolean not null
)''')
oCurseur.execute('''CREATE TABLE weapons(
   /* définition des champs */
   id INTEGER  PRIMARY KEY autoincrement,
   name VARCHAR(50) NOT NULL,
   damage INTEGER NOT NULL
)''')
oCurseur.execute('''CREATE TABLE spells(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   name VARCHAR(50) NOT NULL,
   damage INTEGER default 0,
   learn_level integer default 0,
   category_id integer default null,
   /* déclaration des clés étrangères et primaires */
   foreign key (category_id) references categories(id)
)''')
oCurseur.execute('''CREATE TABLE features(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   name VARCHAR(50) NOT NULL
)''')
oCurseur.execute('''CREATE TABLE abilities(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   name VARCHAR(50) NOT NULL
)''')
oCurseur.execute('''CREATE TABLE entities(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   name VARCHAR(50) NOT NULL,
   life integer not null,
   max_life integer default 10,
   exp integer default 0,
   max_exp integer default null,
   level integer default 0,
   max_level integer default 20,
   category_id integer not null,
   ability_id integer default null,
   /* déclaration des clés étrangères et primaires */
   foreign key (category_id) references categories(id),
   foreign key (ability_id) references abilities(id)
)''')
oCurseur.execute('''CREATE TABLE entity_feature(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   entity_id INTEGER NOT NULL,
   feature_id INTEGER NOT NULL,
   bonus INTEGER default 0,
   /* déclaration des clés étrangères et primaires */
   foreign key (entity_id) references entities(id),
   foreign key (feature_id) references features(id)
)''')
oCurseur.execute('''CREATE TABLE category_weapon(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   category_id INTEGER NOT NULL,
   weapon_id INTEGER NOT NULL,
   /* déclaration des clés étrangères et primaires */
   foreign key (category_id) references categories(id),
   foreign key (weapon_id) references weapons(id)
)''')
oCurseur.execute('''CREATE TABLE ability_entity(
   /* définition des champs */
   id INTEGER PRIMARY KEY autoincrement,
   entity_id INTEGER NOT NULL,
   ability_id INTEGER NOT NULL,
   level integer default 1,
   bonus integer not null,
   /* déclaration des clés étrangères et primaires */
   foreign key (entity_id) references abilities(id),
   foreign key (ability_id) references entities(id)
)''')
# endregion

# region Insert table

# region Table categories
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Guerrier", 0))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Paladin", 0))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Mage de feu", 0))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Mage de glace", 0))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Mage de foudre", 0))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Clerc", 0))

oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Gobelin", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Gobelin mage", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Gobelin élite", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Gobelin à sarbacane", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Boss gobelin", 1))

oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Loup féroce", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Loup blanc", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Loup sanguinaire", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Loup-garou", 1))

oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Chauve-souris", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Vampire", 1))
oCurseur.execute("""INSERT INTO categories (name, is_monster) VALUES(?, ?)""", ("Démon", 1))
# endregion

# region Table features
oCurseur.execute("""INSERT INTO features (name) VALUES(?)""", ("Force",))
oCurseur.execute("""INSERT INTO features (name) VALUES(?)""", ("Sagesse",))
oCurseur.execute("""INSERT INTO features (name) VALUES(?)""", ("Robustesse",))
oCurseur.execute("""INSERT INTO features (name) VALUES(?)""", ("Vitesse",))
# endregion

# region Table spells
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Feu", 2, 1, 3))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Flamme", 6, 7, 3))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Incendie", 10, 14, 3))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Glace", 2, 1, 4))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Glace", 6, 7, 4))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Glace", 10, 14, 4))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Eclair", 2, 1, 5))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Tonnerre", 6, 7, 5))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Foudre", 10, 14, 5))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins", -3, 1, 6))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins avancés", -9, 7, 6))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins primordiaux", -20, 14, 6))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins noirs", -3, 1, 8))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins ténèbreux", -9, 7, 8))
oCurseur.execute("""INSERT INTO spells (name, damage, learn_level, category_id) VALUES(?, ?, ?, ?)""", ("Soins des enfers", -20, 14, 8))
# endregion

# region Table weapons
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Dague", 2))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Epée", 3))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Hallebarde", 5))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Sarbacane", 2))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Lance", 3))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Marteau", 5))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Griffes", 4))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Baguette", 1))
oCurseur.execute("""INSERT INTO weapons (name, damage) VALUES(?, ?)""", ("Bâton", 2))
# endregion

# region Table abilities
oCurseur.execute("""INSERT INTO abilities (name) VALUES(?)""", ("Agilité",))
oCurseur.execute("""INSERT INTO abilities (name) VALUES(?)""", ("Vampirisme",))
oCurseur.execute("""INSERT INTO abilities (name) VALUES(?)""", ("Esquive",))
# endregion

# region Table category_weapon
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (1, 2))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (2, 6))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (3, 9))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (4, 9))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (5, 9))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (6, 8))

oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (7, 1))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (8, 8))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (9, 5))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (10, 4))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (11, 3))

oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (14, 7))
oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (15, 7))

oCurseur.execute("""INSERT INTO category_weapon (category_id, weapon_id) VALUES(?, ?)""", (18, 7))
# endregion

# endregion

oConnection.commit()

oCurseur.close()
oConnection.close()
