class NameSpace:
    
    def __init__(self) -> None:
        self.entities = {}
    
    def register_namespace(self, name):
        self.entities[name] = []
        return self.entities


