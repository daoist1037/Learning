#include<cstdio>
/*#define ADD(a,b) ((a)+(b))  /*���Ϊ7 */ 
#define ADD(a,b) (a+b) /*���Ϊ7 */
#define add(x) (x*2+1)
int main(){
    int num1 = 3 , num2 = 4 ;
    printf("%d\n",ADD(num1,num2)) ;
    printf("%d",add(num2+1)) ;      
    /**
     * ���ﱾ����define��ֱ�ӽ��滻�Ĳ���ԭ�ⲻ�����滻��ȥ������add(num2+1)  �滻���ˣ�num*2+1*2+1)
     */
    return 0 ;
}