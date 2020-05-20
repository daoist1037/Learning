#include <stdio.h>
#include <math.h>


int main()
{
    int a,b;
    double c;
    char str[50]="12003:50:13.45";
    printf("12003:50:13.45\n");
    scanf("%lf",&c);
    sscanf(str,"%d:%d:%lf",&a,&b,&c);
    printf("%d:%d:%.2f",a,b,c);
    printf("\n");
    system("pause");
    return 0;
}

