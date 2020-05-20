/**
 * ɢ�У���Ԫ��ͨ��һ������ת��Ϊһ��������ʹ�ø��������Ծ���Ψһ�ش������Ԫ��
 * ���е�ɢ�к�����  ֱ�Ӷ��ط���ƽ��ȡ�з�������������
 * ֱ�Ӷ�ַ�� ����ֱ�Ӱ� key��Ϊ�����±���߽������Ա任�� H(key) = a * key + b ��  
 * ƽ��ȡ�з� ȡkey��ƽ�����м�����λ��Ϊhashֵ
 * ���������� H(key) = key % mod
 * 
 * 
 * ���ж��key�� H(key)��ͬʱ���������ͻ
 * �����ַ��������ͻ
 * ����̽�鷨 ƽ��̽�鷨 ����ַ������������
 */


/**
 * �ַ���hash����
 * ����ַ�������A~Z 26����ĸ�����ף���ɽ�һ���ַ���ת��Ϊ 26���Ƶ���n������hashTable[n] = 1 ;//����һ�ξͼ�һ
 */
#include<cstdio>
const int maxn = 100 ;
int hashTable[25*26*26 + 25*26 + 25] = {} ;
int hashFunc(char a[]){
    int hash = 0 ;
    for(int i = 0; i < 3; i++){
        hash = hash *26 + (a[i] - 'A') ;
    }
    return hash ;
}
int main(){
    int n, m ;
    int c = 0 ;
    char a[3] ;
    for(int i = 0; i < n; i++){
        scanf("%s", a) ;
       c = hashFunc(a) ;
       hashTable[c] = 1 ;
    }
    for(int i = 0; i < m; i++){
        scanf("%s," a) ;
        c = hashFunc(a) ;
        hashTable[c]++ ;
        printf("%d\n", hashTable[c] - 1) ;
    }
}