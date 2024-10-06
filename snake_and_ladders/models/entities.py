class Entities:
    _instance = None
    
    def __init__(self) -> None:
        self.players = {}
        self.snakes = {}
        self.ladders = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def set_snake(self, start, end):
        self.snakes[start] = end
    
    def get_snakes(self):
        return self.snakes
    
    def set_ladders(self, start, end):
        self.ladders[start] = end

    def get_ladders(self):
        return self.ladders
    
    def set_player(self, id, name):
        self.players[id] = name

    def get_players(self):
        return self.players