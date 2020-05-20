#include <stdio.h>
#include <stdlib.h>
#include <cstring>
using namespace std;

const int maxn = 1000001;
struct Node{
    char data;
    int next;
    bool flag;
}node[maxn];

int main()
{
    int s1, s2, n;
    int address, next;
    char data;
    scanf("%d %d %d", &s1, &s2, &n);
    for(int i = 0; i < n; i++){
        scanf("%d %c %d", &address, &data , &next);
        node[address].data = data;
        node[address].next = next;
    }
    for(int i = s1; i != -1; i = node[i].next){
        node[i].flag = true;
    }
    int p;
    for (p = s2; p != -1; p = node[p].next){
        if (node[p].flag){
            break;
        }
    }
    if(p == -1)
        printf("-1\n");
    else
    {
        printf("%d\n", p);
    }
    
    printf("\n");
    system("pause");
    return 0;
}
