#include<cstdio>
#include<string.h>
/**
 * strlen  ����
 * strcmp(str1,str2)  �Ƚ�
 * strcpy(str1,str2)  ���ư��ַ�����2���Ƹ��ַ�����1
 * strcat(str1,str2)  ���ַ�����2�ӵ��ַ�����1����
 * 
 * sscanf  sprintf
 * sscanf(str,"%*", &*);  ���ַ�����str�е�������%*��ʽд��*��
 * sprintf(str,"%*", *);  ��*��%*��ʽд��str�ַ������У����Ǵ�������
 */
int main(){
    //strlen
    char str[10] ;
    gets(str) ;
    int len = strlen(str) ;
    printf("%d\n", len) ;

    //strcmp �Ƚ�ԭ�� �ֵ���
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