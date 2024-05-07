
class JogoDatabase:
    def __init__(self, database):
        self.db = database

    def create_Player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_Match(self, name, Player_name):
        query = "MATCH (p:Player {name: $Player_name}) CREATE (:Partida {name: $name})<-[:JOGA]-(p)"
        parameters = {"name": name, "Player_name": Player_name}
        self.db.execute_query(query, parameters)

    def get_Player(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_Match(self):
        query = "MATCH (a:Match)<-[:JOGA]-(p:Player) RETURN a.name AS name, p.name AS Player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["Player_name"]) for result in results]

    def update_Player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def insert_Player_Match(self, Player_name, Match_name):
        query = "MATCH (a:Player {name: $Player_name}) MATCH (b:Match {name: $Match_name}) CREATE (a)-[:JOGA]->(b)"
        parameters = {"Player_name": Player_name, "Match_name": Match_name}
        self.db.execute_query(query, parameters)

    def set_winner(self, match_name, winner_name):
        query = "MATCH (m:Match {name: $match_name}) SET m.winner = $winner_name"
        parameters = {"match_name": match_name, "winner_name": winner_name}
        self.db.execute_query(query, parameters)

    def get_winner(self, match_name):
        query = "MATCH (m:Match {name: $match_name}) RETURN m.winner AS winner"
        parameters = {"match_name": match_name}
        result = self.db.execute_query(query, parameters)
        return result[0]["winner"] if result else None

    def delete_Player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_Match(self, name):
        query = "MATCH (a:Match {name: $name})<-[:JOGA]-(p:Player) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)