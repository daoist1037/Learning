#include <stdio.h>
#include <stdlib.h>


struct node{
    int data;
    node *next;
};
node* creatNode(int a[]){
    node *head,*pre,*p;
    head = new node;
    head->next = NULL;
    pre = head;
    for(int i = 0; i < 5; i++ ){
        p = new node;
        p->data = a[i];
        p->next = NULL;
        pre->next = p;
        pre = p;
    }
    return head;
}
int main()
{
    int a[5] = {0,1,2,3,4};
    node *p;
    p = creatNode(a);
    for(int i = 0; i < 5; i++){
        p = p->next;
        printf("%d", p->data);
    }
    printf("\n");
    system("pause");
    return 0;
}
