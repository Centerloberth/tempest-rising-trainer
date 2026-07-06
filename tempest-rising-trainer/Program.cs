using TempestRisingTrainer.Core;

namespace TempestRisingTrainer;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Tempest Rising Trainer v1.0");
        Console.WriteLine("---------------------------");
        Console.WriteLine("Commands: health, resources, speed, exit");

        var memory = new MemoryManager();
        memory.AttachToProcess("TempestRising");

        while (true)
        {
            Console.Write("> ");
            var input = Console.ReadLine()?.Trim().ToLower();
            if (input == "exit") break;

            switch (input)
            {
                case "health":
                    memory.WriteFloat(0x004A2B10, 9999f);
                    Console.WriteLine("Health set to 9999");
                    break;
                case "resources":
                    memory.WriteInt32(0x004A2B14, 50000);
                    Console.WriteLine("Resources set to 50000");
                    break;
                case "speed":
                    memory.WriteFloat(0x004A2B18, 2.5f);
                    Console.WriteLine("Game speed 2.5x");
                    break;
                default:
                    Console.WriteLine("Unknown command");
                    break;
            }
        }
    }
}