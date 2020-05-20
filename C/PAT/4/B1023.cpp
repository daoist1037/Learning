#include<cstdio>
#include<algorithm>
using namespace std ;
int main() {
    int count[10] ;
    int Input[250] ;
    int k = 0 ;
    for(int i = 0; i < 10 ; i++) {
        scanf("%d", &count[i]) ;
        for (int j = 0 ; j < count[i]; j++) {
            Input[k] = i ;
            k++ ;
        }      
    }
    if(Input[0] != 0) {
        for(int i= 0; i < k; i++) {
            printf("%d", Input[i]) ;
        }
    }
    else {
        printf("%d", Input[count[0]]) ;
        for( int i = 0; i < count[i]; i++) {
            printf("%d", Input[i]) ;
        }
        for(int i = count[i]+1; i < k; i++) {
            printf("%d", Input[i]) ;
        }
    }
    return 0 ;
}