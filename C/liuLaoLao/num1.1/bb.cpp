int Max3(int A, int B. int C)
{
    return A>B?A>C?A:C:B>C?B:C;
}
//分而治之
int DivideAndConquer( int List[], int left, int right )
{
    int MaxLeftSum, MaxRightSum; /* 存放左右子问题的解 */
    int MaxLeftBorderSum, MaxRightBorderSum; /*存放跨分界线的结果*/

    int LeftBorderSum, RightBorderSum;
    int center, i;

    if (left == right)
    {
        if (List[left] < 0)
            return 0;
        else
            return List[left];
    }

    center=(left + right) / 2;
    MaxLeftSum = DivideAndConquer( int List[], int left, int center);
    MaxRightSum = DivideAndConquer( int List[], int center+1, int right);

    MaxLeftBorderSum=0;
    LeftBorderSum=0;
    for (int i = center; i >= left; i--)
    {
        LeftBorderSum += List[i];
        if (LeftBorderSum > MaxLeftBorderSum)
            MaxLeftBorderSum = LeftBorderSum;
    }

    MaxRightBorderSum=0;
    RightBorderSum=0;
    for (int i = center+1; i <= right; i++)
    {
        RightBorderSum += List[i];
        if (RightBorderSum > MaxRightBorderSum)
            MaxRightBorderSum = RightBorderSum;
    }

    return Max3(MaxLeftSum,MaxRightSum,MaxLeftBorderSum + MaxRightBorderSum);
    
}