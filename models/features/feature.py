import sqlite3
from misc.generate_class import auto_generate_class


class Feature:
    db = sqlite3.connect('pdoGames.db')
    cursor = db.cursor()
    className = 'Feature'
    moduleName = 'models.features.feature'

    def __init__(self):
        self.id = None
        self.name = None
        self.statsFeatures = None

    def getFeaturesByEntityId(self, id):
        features = self.getFeatures()
        for feature in features:
            self.cursor.execute(
                """SELECT ef.* FROM features
                 JOIN entity_feature ef on features.id = ef.feature_id
                 WHERE ef.entity_id = ? AND ef.feature_id = ?""", (id, feature.id))
            result = self.cursor.fetchone()
            feature.statsFeatures = {'Bonus': result[3]}
        return features

    def getFeatures(self):
        self.cursor.execute(
            """SELECT * FROM features""")
        results = self.cursor.fetchall()
        features = auto_generate_class(results, self.moduleName, self.className)
        return features
