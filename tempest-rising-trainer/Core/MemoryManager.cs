using System.Diagnostics;

namespace TempestRisingTrainer.Core;

public class MemoryManager
{
    private Process? _process;
    private IntPtr _handle;

    public bool AttachToProcess(string processName)
    {
        var processes = Process.GetProcessesByName(processName);
        if (processes.Length == 0)
        {
            Console.WriteLine($"Process '{processName}' not found.");
            return false;
        }

        _process = processes[0];
        _handle = _process.Handle;
        Console.WriteLine($"Attached to {_process.ProcessName} (PID: {_process.Id})");
        return true;
    }

    public void WriteFloat(IntPtr address, float value)
    {
        if (_process == null) return;
        var bytes = BitConverter.GetBytes(value);
        WriteBytes(address, bytes);
    }

    public void WriteInt32(IntPtr address, int value)
    {
        if (_process == null) return;
        var bytes = BitConverter.GetBytes(value);
        WriteBytes(address, bytes);
    }

    private void WriteBytes(IntPtr address, byte[] bytes)
    {
        if (_process == null) return;
        Kernel32.WriteProcessMemory(_handle, address, bytes, bytes.Length, out _);
    }
}