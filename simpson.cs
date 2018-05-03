using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApp2
{
    class Program
    {
        public static double f(double x)
        {
            return Math.Pow(x, 2)+2;
        }
        static void Main(string[] args)
        {
            double a = 2;
            int i = 0;
            int j = 0;
            double b = 3;
            int n = 1024;
            double h = (b - a) / n;
            double integral = f(a) + f(b);
            for (i = 1; i < n; i += 2)
            {
                integral += 4 * f(a + i * h);
            }

            for (j = 2; j < n - 1; j += 2)
            {
                integral += 2 * f(a + j * h);
            }


            Console.WriteLine(integral * h / 3);
            Console.ReadKey();
        }
    }
}
