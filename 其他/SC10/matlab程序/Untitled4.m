syms a1 a3 d1 d3 q1 l2 q3 q4;
pi=sym(pi);

% DH参数
a=[0,a1,0,a3];
d=[d1,0,d3,0];
alpha=[0,0,0,pi];
theta=[0,0,pi,pi];

axis=[q1,l2,q3,q4];

T=sym(eye(4));
for i=1:4
    if i==2
        A=mdh_matrix(a(i),alpha(i),d(i)+axis(i),theta(i));
        T=T*A;
    else
        A=mdh_matrix(a(i),alpha(i),d(i),theta(i)+axis(i));
        T=T*A;
    end
end

T=simplify(T);
disp(T);

% A矩阵的计算函数(MDH方法)
function [A]=mdh_matrix(a,alpha,d,theta)
A=sym(eye(4));
A(1,1)=cos(theta);
A(1,2)=-sin(theta);
A(1,3)=0;
A(1,4)=a;

A(2,1)=sin(theta)*cos(alpha);
A(2,2)=cos(theta)*cos(alpha);
A(2,3)=-sin(alpha);
A(2,4)=-sin(alpha)*d;

A(3,1)=sin(theta)*sin(alpha);
A(3,2)=cos(theta)*sin(alpha);
A(3,3)=cos(alpha);
A(3,4)=cos(alpha)*d;

A(4,1)=0;
A(4,2)=0;
A(4,3)=0;
A(4,4)=1;
end
