/******************************************
>	FileName:	c.cpp
>	Author:	daoist
>	Email:	1748624858@qq.com
>	Creat:	2020:05:11:14:41
******************************************/
#include <cstdio>
#include<string.h>

void pr(int a){
    switch (a)
    {
    case 0:
        printf("ling");
        break;
    case 1:
        printf("yi");
        break;
    case 2:
        printf("er");
        break;
    case 3:
        printf("san");
        break;
    case 4:
        printf("si");
        break;
    case 5:
        printf("wu");
        break;
    case 6:
        printf("liu");
        break;
    case 7:
        printf("qi");
        break;
    case 8:
        printf("ba");
        break;
    case 9:
        printf("jiu");
        break;
    }
}
int main()
{
    int sum = 0;
    char s[1001];
    int a = 0;
    scanf("%s", s);
    for (int i = 0; i <= strlen(s) - 1;i++)
        sum += (s[i] - '0');
    a = sum / 100;
    sum = sum % 100;
    int i = 0;
    if (a != 0)
    {
        i++;
        pr(a);
        printf(" ");
    }
    a = sum / 10;
    sum = sum % 10;
    if(i!=1&&a!=0 || i==1){
        pr(a);
        printf(" ");
    }
    a = sum ;
    pr(a);
		printf("\n");
    return 0;
}
