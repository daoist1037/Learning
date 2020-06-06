#include<cstdio>
const int max = 100000;
int shool[max] = {0};
int main(){
    int n, schId, goal;
    int count = 0;
    scanf("%d",&n);
    for(int i = 0;i < n; i++){
        scanf("%d%d",&schId,&goal);
        shool[schId-1] += goal; 
    }
    count = schId;
    int tmp = 0, tmpT = 0;
    for(int i = 0;i <= count;i++ ){
        if(tmp <= shool[i]) { 
            tmp = shool[i];
            tmpT = i;
        }
    }
    printf("%d   %d",tmp,tmpT+1);
}