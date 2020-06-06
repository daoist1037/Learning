#include<cstdio>
/*#define ADD(a,b) ((a)+(b))  /*输出为7 */ 
#define ADD(a,b) (a+b) /*输出为7 */
#define add(x) (x*2+1)
int main(){
    int num1 = 3 , num2 = 4 ;
    printf("%d\n",ADD(num1,num2)) ;
    printf("%d",add(num2+1)) ;      
    /**
     * 这里本质上define是直接将替换的部分原封不动的替换进去，导致add(num2+1)  替换成了（num*2+1*2+1)
     */
    return 0 ;
}