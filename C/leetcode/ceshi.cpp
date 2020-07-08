#include <stdio.h>

int main(){
    int a[10000] = {0};
    for (int i = 0; i < 1000; i++){
        printf("%d", a[i]);
    }
    return 0;
}
