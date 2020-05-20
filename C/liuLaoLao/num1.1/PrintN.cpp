#include<iostream>
using namespace std;
void PrintN(int N)
{
    if(N)
    {
        PrintN(N-1);
        printf("%d\n",N);
    }
    return ;
}
void PrintN2(int N)
{
    int i;
    for (i = 1; i <= N; i++)
    {
        printf("%d\n",i);
    }
    
    return ;
}
int main()
{
    int N;
    scanf("%d",&N);
    PrintN2(N);
    return 0;
}