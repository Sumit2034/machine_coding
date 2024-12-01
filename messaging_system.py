from typing import List, Dict
from datetime import datetime
from collections import deque

# User class
class User:
    def __init__(self, user_id: str, username: str, password: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        # Other user-related attributes

# Message class
class Message:
    def __init__(self, message_id: str, sender: User, receivers: List[User], content: str):
        self.message_id = message_id
        self.sender = sender
        self.receivers = receivers
        self.content = content
        self.timestamp = datetime.now()
        self.is_encrypted = False
        self.is_delivered = False
        self.is_read = False

    # Methods for marking message as delivered and read
    def mark_as_delivered(self):
        self.is_delivered = True

    def mark_as_read(self):
        self.is_read = True

# MessageManager class
class MessageManager:
    def __init__(self):
        self.sent_messages = []
        self.received_messages = []

    def send_message(self, message: Message):
        self.sent_messages.append(message)
        # Here, actual sending logic can be implemented

    def receive_message(self, message: Message):
        self.received_messages.append(message)
        # Notify observers about the new received message

# MessageSearchStrategy interface (Strategy)
class MessageSearchStrategy:
    def search_messages(self, messages: List[Message], keyword: str) -> List[Message]:
        raise NotImplementedError("Search strategy should implement search_messages method")

# KeywordSearchStrategy class (Strategy)
class KeywordSearchStrategy(MessageSearchStrategy):
    def search_messages(self, messages: List[Message], keyword: str) -> List[Message]:
        return [message for message in messages if keyword in message.content]

# SenderSearchStrategy class (Strategy)
class SenderSearchStrategy(MessageSearchStrategy):
    def search_messages(self, messages: List[Message], sender_username: str) -> List[Message]:
        return [message for message in messages if message.sender.username == sender_username]

# SearchManager class
class SearchManager:
    def __init__(self, search_strategy: MessageSearchStrategy = None):
        self.search_strategy = search_strategy

    def set_search_strategy(self, search_strategy: MessageSearchStrategy):
        self.search_strategy = search_strategy

    def search_messages(self, messages: List[Message], keyword: str) -> List[Message]:
        return self.search_strategy.search_messages(messages, keyword) if self.search_strategy else []

# PresenceObserver interface
class PresenceObserver:
    def on_presence_change(self, user: User, online: bool):
        raise NotImplementedError("Observer should implement on_presence_change method")

# PresenceManager class (Singleton)
class PresenceManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PresenceManager, cls).__new__(cls)
            cls._instance.presence_map = {}
            cls._instance.observers = []
        return cls._instance

    def set_presence(self, user: User, online: bool):
        self.presence_map[user] = online
        self.notify_observers(user, online)

    def add_observer(self, observer: PresenceObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: PresenceObserver):
        self.observers.remove(observer)

    def notify_observers(self, user: User, online: bool):
        for observer in self.observers:
            observer.on_presence_change(user, online)

# MessageEncryptionDecorator class (Decorator)
class MessageEncryptionDecorator(Message):
    def __init__(self, message: Message):
        super().__init__(message.message_id, message.sender, message.receivers, message.content)
        self.message = message
        self.is_encrypted = True

    def get_content(self):
        return f"Encrypted: {self.message.content}"

# MessageState interface (State)
class MessageState:
    def handle_message(self, message: Message):
        raise NotImplementedError("State should implement handle_message method")

# ComposingState class (State)
class ComposingState(MessageState):
    def handle_message(self, message: Message):
        print("Message is in composing state")

# SentState class (State)
class SentState(MessageState):
    def handle_message(self, message: Message):
        message.is_delivered = True
        print("Message sent and marked as delivered")

# ReceivedState class (State)
class ReceivedState(MessageState):
    def handle_message(self, message: Message):
        message.mark_as_read()
        print("Message received and marked as read")

# MessageStateContext class
class MessageStateContext:
    def __init__(self, state: MessageState = ComposingState()):
        self._current_state = state

    def set_state(self, state: MessageState):
        self._current_state = state

    def handle_message(self, message: Message):
        self._current_state.handle_message(message)

# Main simulation
if __name__ == "__main__":
    # Create users
    user1 = User("user1", "john.doe", "password1")
    user2 = User("user2", "alice.smith", "password2")

    # Create messages
    message1 = Message("msg1", user1, [user2], "Hi Alice, how are you?")
    message2 = Message("msg2", user2, [user1], "Hi John, I'm doing well.")

    # Message manager
    message_manager = MessageManager()
    message_manager.receive_message(message1)
    message_manager.receive_message(message2)

    # Search messages by keyword
    search_manager = SearchManager(KeywordSearchStrategy())
    search_results = search_manager.search_messages(message_manager.received_messages, "John")

    # Encrypted message
    encrypted_message = MessageEncryptionDecorator(message2)
    print(encrypted_message.get_content())
