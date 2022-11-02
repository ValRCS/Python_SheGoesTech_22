# we will store our data in a database
# we will use sqlite3
# we will need to come up with migration strategy
# that means we need to create table or alter table or drop table

import sqlite3

# create a connection to the database
# if the database does not exist, it will be created

class DB:
    # constructor
    def __init__(self, db_name="nim.db"):
        self.conn = sqlite3.connect(db_name) # this will create a file if it does not exist
        self.cursor = self.conn.cursor()
        self.create_tables() # TODO
        print(f"connected to the database {db_name}")

    # destructor - good practice but not required for short running programs
    def __del__(self):
        print("closing the connection")
        self.conn.close()

    # create players table
    def _create_players_table(self):
        # create table
        # create table if not exists
        # create table if not exists nim (id integer primary key autoincrement, name text, age integer)
        # name should be unique

        self.cursor.execute("""create table if not exists nim_players 
            (id integer primary key autoincrement, 
            name text UNIQUE, 
            age integer)
            """)
        self.conn.commit()

    # create games table
    def _create_games_table(self):
        # create table
        # create table if not exists
        # create table if not exists nim (id integer primary key autoincrement, name text, age integer)
        self.cursor.execute("""create table if not exists nim_games 
            (id integer primary key autoincrement, 
            player_a_id integer, 
            player_b_id integer,
            game_type text, 
            game_result text, 
            game_date text)
            """)
        self.conn.commit()

    # create tables
    def create_tables(self):
        self._create_players_table()
        self._create_games_table()
        print("tables created if they did not exist - migration complete")

    # insert player if not exists with name
    def insert_player(self, name, age=0):
        print(f"inserting player {name}")
        # insert into nim_players (name, age) values ('John', 20)
        # insert into nim_players (name, age) values ('John', 20) on conflict do nothing
        # parametaized query
        self.cursor.execute("""insert into nim_players (name, age) values (?, ?) 
            on conflict do nothing""", (name, age))
        # alternative would have been to read the data first and then insert if not exists
        # self.cursor.execute("select * from nim_players where name = ?", (name,))
        # data = self.cursor.fetchone()
        # if data is None:
        #     self.cursor.execute("insert into nim_players (name, age) values (?, ?)", (name, age))
        # in any case UNIQUE constraint is a good idea to use on conflict do nothing
        self.conn.commit()

    # get player id by name
    def get_player_id(self, name):
        print(f"getting player id for {name}")
        self.cursor.execute("select id from nim_players where name = ?", (name,))
        data = self.cursor.fetchone() # we know of course that there will be only one row
        # because of the UNIQUE constraint
        if data is None:
            return None # we could return -1 or 0 or raise an exception
        else:
            return data[0]

    # insert game
    def insert_game(self, player_a_id, player_b_id, game_type, game_result, game_date):
        print(f"inserting game {game_type}")
        # insert into nim_players (name, age) values ('John', 20)
        # insert into nim_players (name, age) values ('John', 20) on conflict do nothing
        # parametaized query
        self.cursor.execute("""insert into nim_games (player_a_id, player_b_id, game_type, game_result, game_date) 
            values (?, ?, ?, ?, ?)""", (player_a_id, player_b_id, game_type, game_result, game_date))
        # TODO insert datetime from SQL function
        
        self.conn.commit()

    