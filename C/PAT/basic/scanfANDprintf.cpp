#include<cstdio>
/**
 * scanf的双引号内的内容其实就是整个输入，只不过把数据转换成他们对应的格式符并把变量的地址按次序写在后面而已
 * int  %d
 * long long %lld
 * float %f
 * double %lf   它的输出格式为%f    切记
 * char %c
 * 字符串（char数组） %s    例外:   scanf("%s",str);  这里str就是地址
 */
int main(){

    int hh , mm , ss ;
    scanf("%d:%d:%d",&hh,&mm,&ss) ;
    printf("%d:%d:%d",hh,mm,ss) ;

    /**
     * 除了%c外，scanf对其他格式符（如%d）的输入是以空白符（空格、Tab）为结束判断标志的，因此除非使用%c把空格按照字符读入，其他情况都会自动跳过空格
     * 另外%s字符数组的的读入是以空格和换行行为读入结束的标志
     */

    int a ;
    double b ;
    char c ;
    scanf("%d%lf%c",&a,&b,&c) ;
    printf("%d,%f,%c",a,b,c) ;
    printf("%f",b) ;
    return 0 ;
}