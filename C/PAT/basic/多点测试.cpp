/**while ... EOF型
 * scanf函数也是有返回值的，它的返回值就是其成功读入的参数的个数
 * 如：在读取文件到达文件末尾导致的无法读取现象，会产生读入失败，scanf函数会返回-1
 * C语言中使用EOF（即End of File) 来代表-1
 * 
 * 控制台上需要输入<ctrl+z>组合键
 * 
 */
#include<cstdio>
int main(){
    int a, b ;
    while ( scanf("%d%d" ,a, b) != EOF )
    {
        printf("%dn", a+b) ;
    }
    return 0 ;
}

/**
 * while...break
 */
while (scanf("%d%d", &a, &b), a || b)
{
    printf("%d\n", a+b) ;
}


/**
 * while(T--)
 */
while(n--){
    //循环体内容
}