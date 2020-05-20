#include <stdio.h>
#include <stdlib.h>
#include <stack>
using namespace std;
int ans =0;


int main()
{
    stack<char> q;
    char c;
    while (scanf("%c", &c)!=EOF)
    {
        q.push(c);
        if(q.top() == '\n')
            q.pop();
    }
    printf("%d", q.size());
    
    
    printf("\n");
    system("pause");
    return 0;
}
