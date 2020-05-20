#include <stdio.h>
#include <stdlib.h>

struct Node{
    Node* right =NULL;
    Node* left = NULL;
    int data=0;
} a;


int main()
{
    struct Node b;
    b.data = 1;
    b.left = NULL;
    b.right = NULL;
    a.left = &b;
    printf("%d", a.left->data);
    printf("\b ");
    printf("heool");
    printf("\b \b \b ");
    printf("\n");
    system("pause");
    
    return 0;
}
