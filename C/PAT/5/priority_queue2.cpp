#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <string>
using namespace std;

struct fruit
{
    string name;
    int price;
};
typedef  struct fruit f;
struct  cmp
{
    bool operator () (fruit f1, fruit f2){
        return f1.price > f2.price;
    }
};

int main()
{
    priority_queue<fruit, vector<fruit>, cmp >q;
    f f1,f2,f3;
    f1.name = "梨子";
    f1.price = 4;
    f2.name = "桃子";
    f2.price = 3;
    f3.name = "苹果";
    f3.price = 1;
    q.push(f1);
    q.push(f2);
    q.push(f3);
    printf("%d", q.top().price);
    printf("\n");
    system("pause");
    return 0;
}
