#include<cstdio>
#include<string.h>
/**
 * strlen  长度
 * strcmp(str1,str2)  比较
 * strcpy(str1,str2)  复制把字符数组2复制给字符数组1
 * strcat(str1,str2)  把字符数组2接到字符数组1后面
 * 
 * sscanf  sprintf
 * sscanf(str,"%*", &*);  把字符数组str中的内容以%*格式写到*中
 * sprintf(str,"%*", *);  把*以%*格式写到str字符数组中（还是从右往左）
 */
int main(){
    //strlen
    char str[10] ;
    gets(str) ;
    int len = strlen(str) ;
    printf("%d\n", len) ;

    //strcmp 比较原则 字典序
    char str1[50], str2[50] ;
    gets(str1) ;
    gets(str2) ;
    int cmp = strcmp(str1, str2) ;
    if(cmp > 0){
        printf("str1 < str2\n") ;
    }else if(cmp > 0){
        printf("str1 > str2") ;
    }else
    {
        printf("str1 == str2\n") ;
    }
    
    
    return 0 ;
}