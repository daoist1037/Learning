#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <map>
#include <string>
#include <iostream>
using namespace std;

struct node{
    double num;
    char op;
    bool flag;      //true表示数据，false表示操作符
};

string str;
stack<node> s;      //操作符栈
queue<node> q;      //后缀表达式
map<char,int> op;   //优先级

void change(){
    //double num;
    node temp;
    for(int i = 0; i < str.size(); ){
        if(str[i] >= '0' && str[i] <= '9'){
            temp.flag = true;
            temp.num = str[i] - '0';
            i++;
            while( i < str.size() && str[i] >= '0' && str[i] <= '9'){
                temp.num = temp.num * 10 + (str[i] - '0');
                i++;
            }
            q.push(temp);
        }else{
            temp.flag = false;
            temp.op = str[i];
            while( !s.empty() && op[temp.op] <= op[s.top().op]){
                q.push(s.top());
                s.pop();
            }
            s.push(temp);
            i++;
        }
    }
    while( !s.empty() ){
        q.push(s.top());
        s.pop();
    }
}

double Cal(){
    node temp ,cur;
    temp.flag = true;
    double temp1, temp2;
    while( !q.empty() ){
        cur = q.front();
        q.pop();
        if( cur.flag ){
            s.push(cur);

        }else{
            temp2 = s.top().num;
            s.pop();
            temp1 = s.top().num;
            s.pop();
            if( cur.op == '+' ) 
                temp.num = temp1 + temp2;
            if( cur.op == '-' ) 
                temp.num = temp1 - temp2;
            if( cur.op == '*' ) 
                temp.num = temp1 * temp2;
            if( cur.op == '/' ) 
                temp.num = temp1 / temp2;
            s.push(temp);
        }
    }
    return s.top().num;
}

int main()
{
    op['+']=op['-']=1;
    op['*']=op['/']=2;
    
    while( getline(cin,str) && str != "0"){
        for(string::iterator it = str.end(); it != str.begin(); it--){
            if( *it ==  ' ')
                str.erase(it);
        }
        while( !s.empty() )
            s.pop();
        change();
        printf("%.2f\n", Cal());
    }
    printf("\n");
    return 0;
}
