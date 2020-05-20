#include <stdio.h>
#include <math.h>

const int maxn = 11;
int n,p[maxn],hashTable[maxn] = {false};
int count=0;
void pp();
void generateP(int index);
void generateP(int index){
    if(index == n+1){
        count++;
        pp();
        return ;
    }
    for (int x = 1; x <= n; x++){
        if(hashTable[x] == false){
            bool temp = true;
            for (int pre = 1; pre < index; pre++){
                if( abs(x - p[pre]) == abs(index - pre))
                    temp = false;
            }
            if( temp ){
                hashTable[x] = true;
                p[index] = x;
                generateP(index + 1);
                hashTable[x] = false;
            }
        }
    }
}
void pp(){
    printf("It is No.%d\n",count);
    for( int i = 1; i <= n; i++){
        for (int j = 1; j < p[i] ; j++)
        {
            printf(" ");
        }
        printf("%d\n",p[i]);
    }
}

int main()
{
    n=8;
    generateP(1);
    printf("\n");
    system("pause");
    return 0;
}
