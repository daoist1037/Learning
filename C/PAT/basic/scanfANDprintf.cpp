#include<cstdio>
/**
 * scanf��˫�����ڵ�������ʵ�����������룬ֻ����������ת�������Ƕ�Ӧ�ĸ�ʽ�����ѱ����ĵ�ַ������д�ں������
 * int  %d
 * long long %lld
 * float %f
 * double %lf   ���������ʽΪ%f    �м�
 * char %c
 * �ַ�����char���飩 %s    ����:   scanf("%s",str);  ����str���ǵ�ַ
 */
int main(){

    int hh , mm , ss ;
    scanf("%d:%d:%d",&hh,&mm,&ss) ;
    printf("%d:%d:%d",hh,mm,ss) ;

    /**
     * ����%c�⣬scanf��������ʽ������%d�����������Կհ׷����ո�Tab��Ϊ�����жϱ�־�ģ���˳���ʹ��%c�ѿո����ַ����룬������������Զ������ո�
     * ����%s�ַ�����ĵĶ������Կո�ͻ�����Ϊ��������ı�־
     */

    int a ;
    double b ;
    char c ;
    scanf("%d%lf%c",&a,&b,&c) ;
    printf("%d,%f,%c",a,b,c) ;
    printf("%f",b) ;
    return 0 ;
}