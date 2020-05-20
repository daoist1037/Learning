#include <stdio.h>
#include <stdlib.h>
#include <queue>
using namespace std;

int main()
{
    queue<int> q;
    for (int i = 0; i < 5; i++)
    {
        q.push(i);
    }
    printf("%d %d %d", q.front(), q.back(), q.size());
    printf("\n");
    system("pause");
    return 0;
}
