import unittest
from unittest.mock import patch, MagicMock
from src.trainer import Trainer

class TestTrainer(unittest.TestCase):
    @patch('src.trainer.MemoryReader')
    @patch('src.trainer.HotkeyManager')
    def test_toggle_infinite_health_on(self, mock_hotkey, mock_memory):
        mock_memory_instance = MagicMock()
        mock_memory_instance.read_health.return_value = 500
        mock_memory.return_value = mock_memory_instance

        trainer = Trainer()
        trainer.toggle_infinite_health()

        mock_memory_instance.write_health.assert_called_with(9999)

    @patch('src.trainer.MemoryReader')
    @patch('src.trainer.HotkeyManager')
    def test_toggle_infinite_health_off(self, mock_hotkey, mock_memory):
        mock_memory_instance = MagicMock()
        mock_memory_instance.read_health.return_value = 10000
        mock_memory.return_value = mock_memory_instance

        trainer = Trainer()
        trainer.toggle_infinite_health()

        mock_memory_instance.write_health.assert_called_with(100)

    @patch('src.trainer.MemoryReader')
    @patch('src.trainer.HotkeyManager')
    def test_activate_speed_hack(self, mock_hotkey, mock_memory):
        with patch('src.trainer.pydirectinput.press') as mock_press:
            trainer = Trainer()
            trainer.activate_speed_hack()
            mock_press.assert_called_with('shift')

if __name__ == '__main__':
    unittest.main()