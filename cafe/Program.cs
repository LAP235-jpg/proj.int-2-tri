using System;

namespace Cafe;

public class Program
{
    public static void Main(string[] args)
    {
        var app = new CafeApp();
        app.Run();
    }
}

public class CafeApp
{
    public void Run()
    {
        Console.WriteLine("Welcome to the Cafe!");
        Console.WriteLine("This is a basic C# console app structure.");
    }
}

