from database import Database
from jogo_database import JogoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.93.217.36:7687", "neo4j", "ships-wood-distribution")
db.drop_all()

# Criando uma instância da classe JogoDatabase para interagir com o banco de dados
jogo_db = JogoDatabase(db)

# Criando alguns Playeres
jogo_db.create_Player("João")
jogo_db.create_Player("Maria")
jogo_db.create_Player("José")

# Criando algumas Matchs e suas relações com os Playeres
jogo_db.create_Match("Partida 1", "João")
jogo_db.create_Match("Partida 2", "Maria")
jogo_db.create_Match("Partida 3", "José")

# Atualizando o nome de um Player
jogo_db.update_Player("João", "Pedro")

jogo_db.insert_Player_Match("Ana", "Partida 2")
jogo_db.insert_Player_Match("Ana", "Partida 3")
jogo_db.insert_Player_Match("Carlos", "Partida 1")
jogo_db.insert_Player_Match("Beatriz", "Partida 1")

jogo_db.insert_Player_Match("Maria", "Partida 3")
jogo_db.insert_Player_Match("José", "Partida 2")
jogo_db.insert_Player_Match("José", "Partida 3")

jogo_db.set_winner("Partida 1", "Carlos")

print("Winner of Partida 1:", jogo_db.get_winner("Partida 1"))

# Deletando um Player e uma Match
jogo_db.delete_Match("História")

# Imprimindo todas as informações do banco de dados
print("Players:")
print(jogo_db.get_Player())
print("Matchs:")
print(jogo_db.get_Match())

# Fechando a conexão com o banco de dados
db.close()