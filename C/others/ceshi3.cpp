#include <stdio.h>
#include <math.h>

void swap(int* x,int* y){
    int *temp;;
    temp = x;
    x = y;
    y = temp;
    *x = 2;
}
int main()
{
    int a,b;
    a=1;
    b=0;
    swap(&a,&b);
    printf("%d %d",a,b);
    printf("\n");
    system("pause");
    return 0;
}
