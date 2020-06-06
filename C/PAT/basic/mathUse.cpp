#include<cstdio>
#include<cmath>
int main(){
    /**
     * fabs(double x)  用于对double型变量取绝对值
     */
    double a = -12.56 ;
    printf("%.2f\n", fabs(a)) ;
    
    /**
     * floor(double x)  ceil(double x) 分别用于double变量的向下取整和向上取整
     */
    double d1 = -5.2, d2 = 5.2 ;
    printf("%0.f %0.f\n",floor(d1), ceil(d1)) ;
    printf("%0.f %0.f\n",floor(d2), ceil(d2)) ;
    /**
     * pow(double r, double p)用于返回  r^p  要求 r与p  double
     */

    /**
     * sqrt(double x)返回double类型变量的算术平方根
     */

    /**
     * log(doubel x)返回double变量的以自然数为底的对数
     * C语言中没有对任意底数求对数的函数，因此必须使用换底公式转换
     * log a b = log e b / log e a
     */

    /**
     * sin(double x)  cos tan
     */
    /**
     * asin(double x)  acos  atan 反三角函数
     */

    /**
     * round(double x)四舍五入 返回类型也是double 型 ，需进行取整
     */
    double dd = round(3.40) ;
    printf("%d",(int)dd) ;
    return 0 ;
}