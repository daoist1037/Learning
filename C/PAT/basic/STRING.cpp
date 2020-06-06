#include<cstdio>
/**
 * 字符数组还可以通过直接赋值字符串来实现初始化（但仅限于初始化，程序其他位置不允许这样直接赋值整个字符串）
 */
int main(){
    char str[15] = {'g','o','o','d', ' ','s','t','o','r','y','!'} ;
    for (int  i = 0; i < 11; i++)
    {
        printf("%c",str[i]) ;
    }
    char sstr[15] = "good story!" ;
    for (int  i = 0; i < 11; i++)
    {
        printf("%c",sstr[i]) ;
    }
    return 0 ;
}