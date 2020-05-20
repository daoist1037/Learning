/**
 * 散列：将元素通过一个函数转换为一个整数，使得该整数可以尽量唯一地代表这个元素
 * 常有的散列函数有  直接定地法、平方取中法、除留余数法
 * 直接定址法 就是直接把 key作为数组下标或者进行线性变换（ H(key) = a * key + b ）  
 * 平方取中法 取key的平方的中间若干位作为hash值
 * 除留余数法 H(key) = key % mod
 * 
 * 
 * 当有多个key的 H(key)相同时，会产生冲突
 * 有三种方法解决冲突
 * 线性探查法 平方探查法 链地址法（拉链法）
 */


/**
 * 字符串hash初步
 * 如果字符串仅由A~Z 26个字母作基底，则可将一个字符串转换为 26进制的数n，并将hashTable[n] = 1 ;//出现一次就加一
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