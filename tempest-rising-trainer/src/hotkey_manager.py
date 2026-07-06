import keyboard

class HotkeyManager:
    def __init__(self):
        self._handlers = {}

    def register(self, key, callback):
        self._handlers[key] = callback
        keyboard.add_hotkey(key, callback)

    def unregister(self, key):
        if key in self._handlers:
            keyboard.remove_hotkey(key)
            del self._handlers[key]

    def process(self):
        # keyboard handles callbacks automatically
        pass

    def clear_all(self):
        for key in list(self._handlers.keys()):
            self.unregister(key)