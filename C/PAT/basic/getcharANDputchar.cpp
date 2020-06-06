#include<cstdio>
int main(){
    char c1, c2, c3 ;
    c1 = getchar() ;
    getchar() ;
    c2 = getchar() ;
    c3 = getchar() ;
    /**
     * 此处第一个字符'a'被c1接收；第二个字符虽然被吸收，但是并没有将它存储在某个变量里面
     * 
     */
    putchar(c1) ;
    putchar(c2) ;
    putchar(c3) ;
    /**
    * 输入abcd。输出acd
    */

   char c4, c5, c6 ;
   c4 = getchar() ;
   c5 = getchar() ;
   c6 = getchar() ; 
   putchar(c4) ;
   putchar(c5) ;
   putchar(c6) ;

    return 0 ;
}
