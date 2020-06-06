/**
 * memset(数组名,值,sizeof(数组名));
 * 对数组中所有元素赋相同的值
 * 需要头文件string.h  只建议初学者使用-1或0
 * 因为memset是按字节赋值，即对每个字节赋相同的值，这样组成int的四个字节就会被赋成相同等待值。
 * 而由于0的补码为全0，-1的补码为全1，不容易弄错
 * 如果要赋其他值，使用fill函数，但是memset函数的执行速度更快
 */
#include<cstdio>
#include<string.h>
int main(){
    int a[10] = {} ;
    for (int i = 0; i < 11; i++)
    {
        printf("%d",a[i]) ;
    }
    printf("\n") ;
    int b[5] = { 1, 2, 3, 4, 5} ;
    memset(b, 0, sizeof(b)) ;
    for (int i = 0; i < 5; i++)
    {
        printf("%d",b[i]) ;
    }
    printf("\n") ;
    memset(b,-1,sizeof(b)) ;
    for (int  i = 0; i < 5; i++)
    {
        printf("%d",b[i]) ;
    }
    printf("\n") ;
    return 0 ;
}
/**
 * 特别提醒，如果数组大小较大（大概10^6级别），则需要将其定义在主函数外面，否则会使程序异常退出，原因是函数内部申请的局部变量来自系统栈，允许申请的空间较小；而函数外面申请的全局变量来自静态存储区，允许申请的空间较大
 */