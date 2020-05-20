#include<cstdio>
int main(){
    float f1 = 8765.4 , f2 = 8765.4 ;
    double d1 = 8765.4 , d2 = 8765.4 ;
    printf("%f\n%f\n",f1 * f2, d1 * d2) ;
}
/**
 * 输出结果可见float与double的精度完全不一样   前者一般是有效精度6-7位 后者是15-16位
76832248.000000
76832237.160000
*/