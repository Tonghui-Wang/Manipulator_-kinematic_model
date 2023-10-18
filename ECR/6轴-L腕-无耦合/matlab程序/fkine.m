function [p]=fkine(q)

% a1=100;
% a2=100;
% a3=100;
% d1=100;
% d5=100;
% d6=100;

a1=105;
a2=350;
a3=350;
d1=393;
d5=165;
d6=100;

s1=sind(q(1));
s2=sind(q(2));
s23=sind(q(2)+q(3));
s234=sind(q(2)+q(3)+q(4));
s5=sind(q(5));
s6=sind(q(6));

c1=cosd(q(1));
c2=cosd(q(2));
c23=cosd(q(2)+q(3));
c234=cosd(q(2)+q(3)+q(4));
c5=cosd(q(5));
c6=cosd(q(6));

T(1,1)=c1*c234*c6 + s6*(c1*s234*s5 + c5*s1);
T(1,2)=-c1*c234*s6 + c6*(c1*s234*s5 + c5*s1);
T(1,3)=c1*c5*s234 - s1*s5;
T(1,4)=c1*(a1 - a2*s2 + a3*c23 + c234*d5) - d6*(-c1*c5*s234 + s1*s5);
T(2,1)=c234*c6*s1 + s6*(-c1*c5 + s1*s234*s5);
T(2,2)=-c234*s1*s6 + c6*(-c1*c5 + s1*s234*s5);
T(2,3)=c1*s5 + c5*s1*s234;
T(2,4)=d6*(c1*s5 + c5*s1*s234) + s1*(a1 - a2*s2 + a3*c23 + c234*d5);
T(3,1)=-c234*s5*s6 + c6*s234;
T(3,2)=-c234*c6*s5 - s234*s6;
T(3,3)=-c234*c5;
T(3,4)=a2*c2 + a3*s23 - c234*c5*d6 + d1 + d5*s234;
T(4,1)=0;
T(4,2)=0;
T(4,3)=0;
T(4,4)=1;

p=[T(1:3,4)',rad2deg(tform2eul(T,'ZYX'))];
end