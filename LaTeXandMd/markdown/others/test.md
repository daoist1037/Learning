<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>


```matlab
[x,y]=intprog(f,a,b,aeq,beq,[],[],option);
```
```matlab
clc clear
a=zeros(6);
a=[0 50 inf 40 25 10
50  0 15 20 inf 25
inf 15 0 10 20 inf
40 20 10 0 10  25
25 inf 20 10 0 55
10 25 inf 25 55 0
];
pb(1:length(a))=0;
% 记录被标号的点
pb(1)=1;
index1=1;index2=ones(1,length(a));
d(1:length(a))=inf;d(1)=0;temp=1;
%记录到各点的距离
while sum(pb)<length(a)
	tb=find(pb==0);
 d(tb)=min(d(tb),d(temp)+a(temp,tb));
 tmpb=find(d(tb)==min(d(tb)));
 temp=tb(tmpb(1));
 pb(temp)=1;
 index1=[index1,temp];
 temp2=find(d(index1)==d(temp)-a(temp,index1));
 index2(temp)=index1(temp2(1));
end
d, index1, index2
```



$$
\sum\limits_{1\leq i\leq j\leq n} x_{ij}
$$


| a   | a   |
| --- | --- |
| b   | b   |$$



$$
P-27(化为积分形式)\\
设x_n=\frac{1}{n^4}\prod_{i=1}^{2n}(n^2+i^2)^{\frac{1}{n}},求\lim_{n\to \infty}x_n
$$

$$
设f(x)在[0,1]上连续，且f(0)=f(1),证明：在[0,1]上至少存在一点\xi,使得f(\xi)=f(\xi+\frac{1}{n})
$$


$m\ddot{x}$

$$
P-46\\
y=\frac{x^n}{1+x}\quad求y^{(n)}\qquad
y=\frac{1+x}{\sqrt{1-x}}\quad求y^{(n)}
$$

$
一\\
SPL=20\mathrm{log}_{10}\frac{P_e}{P_{ref}}\\
(1)声压级SPL=0\mathrm{dB}\quad \\
参考声压值P_{ref}=20\mu Pa=2\times 10^{-5}\\
可得有效声压为P_e=P_{ref}=2\times 10^{-5}Pa\\
则声压幅值为P_a=\sqrt{2}P_e=2\sqrt{2}\times10^{-5}Pa\\
质点速度幅值为V_a=\frac{P_a}{\rho_0c_0}=6.8\times 10^{-5}Pa\\
L_p=20\mathrm{lg}(\frac{P}{P_{ref}})\\
质点位移幅值为\xi_a=\frac{v_a}{\omega}=1.08\times 10^{-11}m\\
平均能量密度为\bar{\varepsilon}=\frac{P_a^2}{2\rho_0c_0}=2.8\times 10^{-15}J/m^3\\
(2)声压级SPL=120\mathrm{dB}\quad \\
参考声压值P_{ref}=20\mu Pa=2\times 10^{-5}\\
可得有效声压为P_e=10^6\times P_{ref}=20Pa\\
则声压幅值为P_a=\sqrt{2}P_e=20\sqrt{2}Pa\\
质点速度幅值为V_a=\frac{P_a}{\rho_0c_0}=6.8\times 10^{-2}Pa\\
L_p=20\mathrm{lg}(\frac{P}{P_{ref}})\\
质点位移幅值为\xi_a=\frac{v_a}{\omega}=1.08\times 10^{-5}m\\
平均能量密度为\bar{\varepsilon}=\frac{P_a^2}{2\rho_0c_0}=2.8\times 10^{-3}J/m^3\\
(3)v_e=\frac{p_e}{\rho_0c_0}=c_0得到P_e=\rho_0c_0v_e=\rho_0c_0^2\approx 1.43\times 10^5Pa\\
所以SPL=20\mathrm{log}_{10}\frac{P_e}{P_{ref}}=197\mathrm{dB}\\
二\\
SPL=20\mathrm{log}_{10}\frac{P_e}{P_{ref}}=74\mathrm{dB},P_{ref}=1\times10^{-5}Pa\\
则有效声压P_e=10^{\frac{74}{20}}P_{ref}=0.1Pa\\
平均能量密度\bar{\xi}=\frac{P_e^2}{\rho_0c_0^2}=\frac{0.01}{1.21\times 344^2}=7.01\times 10^{-8}J/m^3\\
声强I=\bar{\xi}c_0=7\times 10^{-8}\times344=2.4\times10^{-5}W/m^3\\
三\\
空气中特性阻抗Z_1=\rho_1c_1=1.21\times344=416\mathrm{kg}/(m^2\cdot s)\\
水中特性阻抗Z_2=\rho_2c_2=1000\times1.5\times 10^3=1.5\times10^6\mathrm{kg}/(m^2\cdot s)\\
I=\frac{1}{2}\rho c u_A^2\\
则n=\frac{I_2}{I_1}=\frac{Z_2}{Z_1}=\frac{1.5\times 10^6}{416}=3605.77
$



$
y=ax(1-x)=ax-ax^2\\
N=x(1-x)\\
y^\prime=a-2ax\\
y^{\prime\prime}=-2a\\
R=(y^\prime)^2-y^2-2yx=a^2-4a^2x+4a^2x^2-ax+ax^2-2[ax-ax^2]x\\
=2ax^3+x^2(4a^2-a)+x(-4a^2-a)+a^2\\
a\\
b\\
$
$$
c\\
\delta y=N
$$


$$
L(OA)=10\mathrm{lg}\frac{P_e^2}{P_r^2}
=10\mathrm{lg}(10^{\frac{L_i}{10}+\frac{L_j}{10}})\\
设置L_i-L_j=\delta\\
L(OA)=10\mathrm{lg}(10^{\frac{L_i}{10}}\times (1+10^{\frac{\delta}{10}}))
=L_i+10\mathrm{lg}(1+10^{\frac{\delta}{10}})
=L_i+(L_c-L_i)
$$
$x^2y_2$

$$
\begin{pmatrix}
	1&1&\cdots&1\\
	\mu_{21}&\mu_{22}&\cdots&\mu_{2n}\\
	\vdots&\vdots&\ddots&\vdots\\
	\mu_{n1}&\mu_{n2}&\cdots&\mu_{nn}\\
\end{pmatrix}
$$

$$
\delta yy'|_{1}^{0}=0\\
\delta yy'|_{0}^{\frac{1}{3}}=0\\
\delta yy'|_{\frac{1}{3}}^{\frac{2}{3}}=0\\
\delta yy'|_{\frac{2}{3}}^{1}=0\\
$$




$$
假设速度均为右，且v_1>v_2\\
M_1\ddot{x_1}-(K_1 x_1+K_2(x_1-x_2))=0\\
M_2\ddot{x_2}-(K_3 x_2-K_2(x_1-x_2))=0\\
$$
$$
对于杆子上的M\\
杆子长度L\\
竖直：K\frac{L}{2}\frac{\sin\theta}{\cos\theta}\times \cos\theta+M\ddot{\theta}\times L\cos\theta+M\dot{x}+2Mg=0\\
水平：K\frac{L}{2}\frac{\sin\theta}{\cos\theta}\times \sin\theta+M\ddot{\theta}\times L\sin\theta+M\dot{y}=0\\
力矩方程：K\frac{L}{2}\frac{\sin\theta}{\cos\theta}\times \frac{L}{2}+M\ddot{\theta}L \times L+M\ddot{y}\times(L-x)+M\ddot{x}\times y=0
$$

