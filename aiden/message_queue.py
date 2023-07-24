```python
import queue

class MessageQueue:
    def __init__(self):
        self.message_queue = queue.Queue()

    def send_message(self, message):
        self.message_queue.put(message)

    def receive_message(self):
        if not self.message_queue.empty():
            return self.message_queue.get()
        else:
            return None
```