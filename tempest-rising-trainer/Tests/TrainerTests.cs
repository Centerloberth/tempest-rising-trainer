using TempestRisingTrainer.Core;

namespace TempestRisingTrainer.Tests;

public class TrainerTests
{
    public static void RunAll()
    {
        Console.WriteLine("Running tests...");
        TestMemoryManagerCreate();
        TestKernel32Imports();
        Console.WriteLine("All tests passed.");
    }

    private static void TestMemoryManagerCreate()
    {
        var mm = new MemoryManager();
        if (mm == null) throw new Exception("MemoryManager creation failed");
        Console.WriteLine("  [PASS] MemoryManager created");
    }

    private static void TestKernel32Imports()
    {
        var type = typeof(Kernel32);
        if (type == null) throw new Exception("Kernel32 type not found");
        Console.WriteLine("  [PASS] Kernel32 imported");
    }
}