/**
 * scanf printf    两种格式
 * %c用来输入单个字符  %s用来输入一个字符并存在字符数组里；
 * %c格式能够识别空格跟换行并将其输入 而%s通过空格或换行来识别一个字符串的结果
 * 
 * getchar putchar用来输入和输出单个字符
 * 
 * gets  puts
 * gets用来输入一行字符串（注意：gets识别换行符\n作为输入结束，因此scanf完一个整数后，如果要使用gets，需要使用getchar接收整数后的换行符），并将其存放于一维数组（或者二维数组的一维）中；而puts用来输出一行字符串，即将一维数组（或二维数组的一维）在界面上输出，并紧跟一个换行
 */
#include<cstdio>
int main(){
    /*
    char str[10] ;
    scanf("%s",str) ;
    printf("%s",str) ;
    */

    char sstr1[20] ;
    char sstr2[5][10] ;
    gets(sstr1) ;
    for (int i = 0; i < 3; i++)
    {
        gets(sstr2[i]) ;
    }
    puts(sstr1) ;
    for (int  i = 0; i < 3; i++)
    {
        puts(sstr2[i]) ;
    }
    
    return 0 ;
}