#include<cstdio>
int main(){
    int a = 12 , b = 3 ;
    a /= b+1 ;      
    /**
     * 等价于 a=a/(b+1)   切勿写成  a /= (b+1)
     */
    printf("%d",a) ;
}