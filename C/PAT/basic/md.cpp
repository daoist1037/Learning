
#include<cstdio>
int main(){
    
    int  a = 123, b = 1234567 ;
    /**
     * %md
     * md可以使得不足m位的int型变量以m位进行右对齐输出，其中高位用空格补齐，变量超过m位，则保持原样
     */
    printf("%5d\n", a) ;
    printf("%5d\n", b) ;

    /**
     * %0md
     * 区别在于当变量不足m位时候，高位用0补齐  右补齐输出
     */
    printf("%05d\n", a) ;
    printf("%05d\n", b) ;

    /**
     *%.mf
     *可以让浮点数保留m位小数输出，这个保留采用的是精度的“四舍六入五成双”规则。
     如果是四舍五入，那么需要用到round函数
     */
    double d1 = 12.3456 ;
    printf("%.0f\n", d1) ;
    printf("%.1f\n", d1) ;
    printf("%.2f\n", d1) ;
    printf("%.3f\n", d1) ;
    printf("%.4f\n", d1) ;
    return 0 ;
}