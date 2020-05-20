#include <stdio.h>
#include <stdlib.h>
#include <queue>
using namespace std;

int main()
{
    priority_queue<int, vector<int>, greater<int> >q;
    q.push(3);
    q.push(4);
    q.push(1);
    printf("%d", q.top());
    printf("\n");
    system("pause");
    return 0;
}
