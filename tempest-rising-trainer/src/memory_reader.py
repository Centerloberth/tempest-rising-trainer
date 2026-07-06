import ctypes
import ctypes.wintypes
import struct

class MemoryReader:
    PROCESS_VM_READ = 0x0010
    PROCESS_VM_WRITE = 0x0020
    PROCESS_QUERY_INFORMATION = 0x0400

    def __init__(self, process_name="TempestRising.exe"):
        self.process_name = process_name
        self.handle = None
        self._open_process()

    def _open_process(self):
        kernel32 = ctypes.windll.kernel32
        self.PID = self._find_process_id(self.process_name)
        if self.PID == 0:
            raise RuntimeError(f"Process {self.process_name} not found.")
        self.handle = kernel32.OpenProcess(
            self.PROCESS_VM_READ | self.PROCESS_VM_WRITE | self.PROCESS_QUERY_INFORMATION,
            False, self.PID
        )

    def _find_process_id(self, name):
        # Simplified PID lookup (mock)
        return 1234  # In real code, use CreateToolhelp32Snapshot

    def read_health(self):
        buffer = ctypes.create_string_buffer(4)
        bytes_read = ctypes.c_size_t()
        ctypes.windll.kernel32.ReadProcessMemory(
            self.handle, 0x00A1B2C0, buffer, 4, ctypes.byref(bytes_read)
        )
        return struct.unpack('I', buffer.raw)[0]

    def write_health(self, value):
        buffer = struct.pack('I', value)
        bytes_written = ctypes.c_size_t()
        ctypes.windll.kernel32.WriteProcessMemory(
            self.handle, 0x00A1B2C0, buffer, 4, ctypes.byref(bytes_written)
        )

    def read_mana(self):
        buffer = ctypes.create_string_buffer(4)
        bytes_read = ctypes.c_size_t()
        ctypes.windll.kernel32.ReadProcessMemory(
            self.handle, 0x00A1B2D0, buffer, 4, ctypes.byref(bytes_read)
        )
        return struct.unpack('I', buffer.raw)[0]

    def write_mana(self, value):
        buffer = struct.pack('I', value)
        bytes_written = ctypes.c_size_t()
        ctypes.windll.kernel32.WriteProcessMemory(
            self.handle, 0x00A1B2D0, buffer, 4, ctypes.byref(bytes_written)
        )

    def close(self):
        if self.handle:
            ctypes.windll.kernel32.CloseHandle(self.handle)