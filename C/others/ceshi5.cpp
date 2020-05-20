#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand((unsigned)time(NULL));
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n",rand()%2);
    }
    
    printf("\n");
    system("pause");
    return 0;
}
