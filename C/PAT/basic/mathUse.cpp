#include<cstdio>
#include<cmath>
int main(){
    /**
     * fabs(double x)  ���ڶ�double�ͱ���ȡ����ֵ
     */
    double a = -12.56 ;
    printf("%.2f\n", fabs(a)) ;
    
    /**
     * floor(double x)  ceil(double x) �ֱ�����double����������ȡ��������ȡ��
     */
    double d1 = -5.2, d2 = 5.2 ;
    printf("%0.f %0.f\n",floor(d1), ceil(d1)) ;
    printf("%0.f %0.f\n",floor(d2), ceil(d2)) ;
    /**
     * pow(double r, double p)���ڷ���  r^p  Ҫ�� r��p  double
     */

    /**
     * sqrt(double x)����double���ͱ���������ƽ����
     */

    /**
     * log(doubel x)����double����������Ȼ��Ϊ�׵Ķ���
     * C������û�ж��������������ĺ�������˱���ʹ�û��׹�ʽת��
     * log a b = log e b / log e a
     */

    /**
     * sin(double x)  cos tan
     */
    /**
     * asin(double x)  acos  atan �����Ǻ���
     */

    /**
     * round(double x)�������� ��������Ҳ��double �� �������ȡ��
     */
    double dd = round(3.40) ;
    printf("%d",(int)dd) ;
    return 0 ;
}