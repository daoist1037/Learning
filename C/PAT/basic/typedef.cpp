/**
 * typedef能给浮渣的数据类型起个别名，用别名代替原来的写法
 */
#include<cstdio>
typedef long long LL ;
int main(){
    LL a = 123456789012345, b = 234567890123456 ; 
    printf("%lld\n", a+b) ;
    return 0 ;
}