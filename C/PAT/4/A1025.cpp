#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std ;

struct Student
{
    char id[15] ;
    int sore ;
    int locoation_number ;
    int local_rank ;
}stu[30010] ;

bool cmp( Student a, Student b) {
    if( a.sore != b.sore ) return a.sore > b.sore ;
    else return strcmp( a.id, b.id) < 0 ; 
}
int main(){
    int n, k, num = 0 ;
    scanf("%d", &n) ;   //考场数量
    for (int i = 0; i < n; i++){
        scanf("%d", &k) ;   //考场人数
        for (int j = 0; j < k; j++){
            scanf("%s %d", stu[num].id, &stu[num].sore) ;
            stu[num].locoation_number = i ;
            num++ ;
        }
        sort( stu + num - k, stu + num, cmp) ;
        stu[num - k].local_rank = 1 ;
        for (int j = num - k + 1; j < num; j++){
            if(stu[j].sore == stu[j - 1].sore){
                stu[j].local_rank = stu[j - 1].local_rank ;
            }else{
                stu[j].local_rank = j + 1 - ( num - k ) ;
            }
        }
    }
    printf("%d\n", num) ;
    sort( stu, stu + num, cmp) ;
    int r = 1 ;
    for (int i = 0; i < num; i++){
        if(i > 0 && stu[i].sore != stu[i - 1].sore){
            r = i + 1 ;
        }
        printf("%s", stu[i].id) ;
        printf("%d %d %d\n", r, stu[i].locoation_number, stu[i].local_rank) ;
    }
    return 0 ;
}