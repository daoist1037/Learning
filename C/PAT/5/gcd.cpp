#include <stdio.h>
#include <math.h>

int gcd(int a,int b){
    if(b == 0)
        return a;
    return gcd(b,a%b);
}
int lcd(int a,int b){
    int d;
    d = gcd(a,b);
    return a*(b/d);
}
int main()
{
    int a,b;
    a=24;
    b=32;
    int c,d;
    c=gcd(a,b);
    d=lcd(a,b);
    printf("\n");
    system("pause");
    return 0;
}
