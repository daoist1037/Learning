//a^b%m 
typedef long long LL ;
LL binaryPow( LL a, LL b, LL m) {
    if(b == 0) return 1 ;
    //bΪ������ת��ΪB-1
    if(b % 2 == 1) return a*binaryPow(a,b-1,m) %m ;
    else { ///bΪż����ת��Ϊb/2
        LL mul = binaryPow(a,b/2,m) ;
        return mul * mul  % m ;
    }
}


LL binaryPow( LL a, LL b, LL m) {
    LL ans = 1 ;
    if(b & 1) ans = ans * a % m ; //���b�Ķ�����ĩβΪ1
    else { ///bΪż����ת��Ϊb/2
        a = a * a % m ;
        b >> = 1 ; //b �Ķ���������
    }
    return ans ;
}
