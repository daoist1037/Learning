#include <stdio.h>
#include <math.h>
const int maxn=1000001;
int pNum=0,prime[maxn];
bool is_prime(int n){
    int x=(int)sqrt(1.0*n);
    for (int i = 2; i <= x; i++)
    {
        if(n % i == 0)
            return false;
    }
    return true;
}
void Find_Prime(){
    for (int i = 2; i < maxn; i++)
    {
        if( is_prime(i) )
            prime[pNum++]=i;
    }
}
struct factor
{
    int x;
    int cnt;
}fac[10];


int main()
{
    Find_Prime();
    int m;
    int num=0;
    scanf("%d",&m);
    int mm=m;
    if( m == 1)
        printf("1=1x1");
    else
    {
        for (int i = 0; i < pNum; i++)
        {
            if( m % prime[i] == 0){
                fac[num].x = prime[i];
                fac[num].cnt = 0;
 
                while (m % prime[i] == 0){
                    fac[num].cnt++;
                    m /= prime[i];
                }
                num++;
            }
            if( m == 1)
                 break;
        }
        if( m > (int)sqrt(1.0*mm))
            printf("%d=%dx1",mm,mm);
        else
        {
            printf("%d=",mm);
            for (int i = 0; i < num; i++)
            {
                if( i < num-1){
                        printf("%d^%dx",fac[i].x,fac[i].cnt);
                }
                else
                {
                    printf("%d^%d",fac[i].x,fac[i].cnt);
                }
            }
        }
            

    }

    
    printf("\n");
    system("pause");
    return 0;
}
