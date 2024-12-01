class GameController:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize only if the instance is being created for the first time
        if not hasattr(self, '_initialized'):
            # Your initialization code here
            self._initialized = True  # Mark the instance as initialized
