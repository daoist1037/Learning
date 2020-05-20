#include <cstdio>
#include <cmath>

int Max3( int A, int B, int C )

{ /* 返回3个整数中的最大值 */
    return A > B ? A > C ? A : C : B > C ? B : C;
}
int main()
{
    int A,B,C;
    A=6;
    B=8;
    C=11;
    int d;
    d=Max3(A,B,C);
    printf("%d\n",d);
    system("pause");
    return 0;
}

