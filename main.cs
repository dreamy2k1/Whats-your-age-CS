using System;

namespace WhatsYourAge
{
    class Program
    {
        static void Main(string[] args)
        {
            string yourAge;
            int age;

            Console.WriteLine("What is your age?");

            // Ensure input is a number and no more than 3 digits
            while (true)
            {
                yourAge = Console.ReadLine();

                // Check if the input is a number and within the valid range
                if (int.TryParse(yourAge, out age) && age >= 0 && age <= 999)
                {
                    break;  // Valid input, exit the loop
                }
                else
                {
                    Console.WriteLine("Please enter a valid age (a number with up to 3 digits).");
                }
            }

            Console.WriteLine("Your age is {0}", yourAge);
        }
    }
}

