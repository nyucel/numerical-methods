#include <stdio.h>
#include <stdlib.h>
#include <math.h>


float f(double x)
{
	return pow(x,2)+2.0;
}


int main(int argc, char *argv[]) {
	double a=2;
	int i=0;
	int j=0;
	double b=3;
	int n=1024;
	double h = (b - a) / n;
	double integral = f(a) + f(b);
	for(i=1;i<n;i+=2)
	{
		integral += 4 * f(a + i * h);
	}
    	
	for(j=2;j<n-1;j+=2)
	{
		integral += 2 * f(a + j * h);
	}
    	
	
	printf("%.20lf",integral*h/3);
}
