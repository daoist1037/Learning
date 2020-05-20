#include <stdio.h>
#include <math.h>


int main()
{
    int* p;
    int a=4;
    int b;
    p=&a;
    printf("%d",*p);
    *p=5;
    printf("%d",*p);
    printf("%d",a);
    printf("\n");
    system("pause");
    return 0;
}
