#include <stdio.h>
#include <stdlib.h>
#include <map>
using namespace std;


int main()
{
    map<char, int> mp;
    mp['m'] = 20;
    mp['b'] = 30;
    mp['a'] = 40;
    map<char , int>::iterator it;
    it=mp.begin();
    for (; it != mp.end(); it++)
    {
        printf("%c=%d",it->first,it->second);
    }
    
    printf("\n");
    system("pause");
    return 0;
}
