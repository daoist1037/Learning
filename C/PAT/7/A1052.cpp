#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int maxn = 10001;
struct Node{
    int address;
    int data;
    int next;
    bool flag;
}node[maxn];

bool cmp(Node a, Node b){
    if(a.flag == false || b.flag == false)
        return a.flag > b.flag;
    else{
        return a.data < b.data;
    }
}

int main()
{
    for(int i = 0; i < maxn; i ++){
        node[i].flag = false;
    }
    int n;
    int s;
    int address,data,next;
    scanf("%d %d", &n, &s);
    for(int i = 0; i < n; i++){
        scanf("%d %d %d", &address, &data, &next);
        node[address].address = address;
        node[address].data = data;
        node[address].next = next;
        
    }
    int count = 0;
    for(int i = s; i != -1; i = node[i].next){
        node[i].flag = true;
        count++;
    }
    if(count == 0)
        printf("0 -1");
    else
    {
        sort(node, node + maxn, cmp);
        printf("%d %05d", count, node[0].address);
        for(int i = 0; i < count; i++){
            if(i != count-1)
                printf("%05d %d %05d\n", node[i].address, node[i].data, node[i+1].address);
            else{
                printf("%05d %d -1\n", node[i].address, node[i].data);
            }
        }
    }
    
    
    printf("\n");
    system("pause");
    return 0;
}
