import java.lang.Math;

public class simpson{

    public static double f(double x)
    {
        return x*x+2.0;
    }
        
    public static void main(String []args){
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

        System.out.println(integral*h/3);
     }
}

