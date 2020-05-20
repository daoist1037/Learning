#include<cstdio>
#include<stdlib.h>
 const int maxn = 11 ;
 int n, p[maxn], hashTable[maxn] = {false} ;
 void gererateP(int index){
     if(index == n + 1) {
         for(int i = 1; i <= n; i++){
             printf("%d", p[i]) ;
         }
         printf("\n") ;
         return ;
     }
     for(int x = 1; x <= n; x++){
         if(hashTable[x] == false){
             p[index] = x ;
             hashTable[x] = true ;
             gererateP(index + 1) ;
             hashTable[x] = false ;
         }
     }
 }
 int main(){
     n = 3 ;
     gererateP(1) ;
     system("pause") ;
     return 0 ;
 }