
>```R
>heart<-data.frame()
>for(i in 1:4000)
>{
>x=i*0.0005-1
>y=(x^2)^(1/3)+(1-x^2)^(1/2)
>heart<-rbind(heart,c(x,y))
>y=(x^2)^(1/3)-(1-x^2)^(1/2)
>heart<-rbind(heart,c(x,y))
>}
>colnames(heart)<-c('x','y')
>plot(heart$y~heart$x,main='HEART',col='red')
>```

$\log_{\alpha}{x} = \frac{\log_\beta x}{\log_\beta \alpha}$ 

