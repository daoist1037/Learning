#include <stdio.h>
#include <stdlib.h>


int main()
{
    int *p = new int(4) ;
    *(p+1)=5;
    printf("%d", *(p+1));
    delete (p);
    printf("\n");
    system("pause");
    return 0;
}
