#include<cstdio>
/**
 * �ַ����黹����ͨ��ֱ�Ӹ�ֵ�ַ�����ʵ�ֳ�ʼ�����������ڳ�ʼ������������λ�ò���������ֱ�Ӹ�ֵ�����ַ�����
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