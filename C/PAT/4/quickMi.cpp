//a^b%m 
typedef long long LL ;
LL binaryPow( LL a, LL b, LL m) {
    if(b == 0) return 1 ;
    //b为奇数，转换为B-1
    if(b % 2 == 1) return a*binaryPow(a,b-1,m) %m ;
    else { ///b为偶数，转换为b/2
        LL mul = binaryPow(a,b/2,m) ;
        return mul * mul  % m ;
    }
}


LL binaryPow( LL a, LL b, LL m) {
    LL ans = 1 ;
    if(b & 1) ans = ans * a % m ; //如果b的二进制末尾为1
    else { ///b为偶数，转换为b/2
        a = a * a % m ;
        b >> = 1 ; //b 的二进制右移
    }
    return ans ;
}
