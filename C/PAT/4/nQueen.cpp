#include<cstdio>
#include<stdlib.h>
const int maxn = 11;
int n;
int P[maxn], hashTable[maxn] = {false} ;
int count = 0 ; 
void vsp( int p[]){
    printf("It is No.%d\n", count);
    for( int i = 1; i <= n; i++) {
        for( int j = 1; j < p[i]; j++)
            printf(" ");
        printf("*");
        printf("\n");
    }
    printf("\n");
}
void generateP( int index ) {
    if (index == n + 1){
        bool flag = true ;
        for (int i = 1; i <= n; i++){
            for (int j = i + 1; j <= n; j++){

                if( abs(i - j) == abs( P[i] - P[j] ) )
                    flag = false ;
            }
            
        }
        if(flag) {
            count++;
            vsp(P);
        }
        return ;
    }
        for(int x =1; x<= n; x++){
            if(hashTable[x] == false){
                P[index] = x;
                hashTable[x] = true ;
                generateP(index + 1);
                hashTable[x] = false;
            }
        }
}

int main(){
    n =8;
    generateP(1);
    system("pause");
    return 0;
    
}