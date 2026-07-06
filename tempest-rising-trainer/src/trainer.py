import time
import pydirectinput
from src.memory_reader import MemoryReader
from src.hotkey_manager import HotkeyManager

class Trainer:
    def __init__(self):
        self.memory = MemoryReader()
        self.hotkeys = HotkeyManager()
        self.running = False
        self._setup_hotkeys()

    def _setup_hotkeys(self):
        self.hotkeys.register("F1", self.toggle_infinite_health)
        self.hotkeys.register("F2", self.toggle_infinite_mana)
        self.hotkeys.register("F3", self.activate_speed_hack)

    def toggle_infinite_health(self):
        current = self.memory.read_health()
        if current < 9999:
            self.memory.write_health(9999)
            print("[Trainer] Infinite Health: ON")
        else:
            self.memory.write_health(100)
            print("[Trainer] Infinite Health: OFF")

    def toggle_infinite_mana(self):
        current = self.memory.read_mana()
        if current < 9999:
            self.memory.write_mana(9999)
            print("[Trainer] Infinite Mana: ON")
        else:
            self.memory.write_mana(50)
            print("[Trainer] Infinite Mana: OFF")

    def activate_speed_hack(self):
        pydirectinput.press('shift')
        print("[Trainer] Speed Hack Toggled")

    def start(self):
        self.running = True
        print("[Trainer] Tempest Rising Trainer started. Press F1, F2, F3.")
        while self.running:
            self.hotkeys.process()
            time.sleep(0.05)

    def stop(self):
        self.running = False
        print("[Trainer] Stopped.")