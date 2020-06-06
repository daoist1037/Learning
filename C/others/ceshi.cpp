#include <iostream>
using namespace std;
/*
void swap(int *a, int *b) {
    int temp = *a ;
    *a = *b ;
    *b = temp ; 
}
*/

void swap(int *a, int *b)
{
    *a = 2;
    *b = 0;
}

int main()
{
    int a = 1, b = 2;
    int *p1 = &a, *p2 = &b;
    swap(p1, p2);
    printf("a = %d, b = %d 试试\n", *p1, *p2);
    printf("a = %d, b = %d 试试\n", a, b);
    system("pause");
    return 0;
}