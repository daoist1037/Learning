#include<cstdio>

int fun(int a[][],int b[][]) 
{
    return sums ;
}

int main() 
{
    int n = 4 ;
    int  sum = 0 ;
    scanf("please input Matrix") ;
    printf("\n") ;
    int a[n][n] ;
    int b[n][n] ;
    for( int i = 0; i<= n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", a[i][j]) ;
        }
    }
    sum = fun( a, b) ;
    for( int i = 0; i < n; i++) {
        for(int j=0 ; j<n; j++){
            printf("%d  ", a[i][j]);
        }
        printf("\n") ;
    }
    return 0 ;
}