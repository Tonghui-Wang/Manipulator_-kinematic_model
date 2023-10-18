# 运动学正解推算
# @Time:2021/7/29 17:30
# @Auther:Tonghui Wang
# @File:fkine.py
# @software:IDLE

import sympy as sy

# 定义可能用到的符号变量
d1,d4,d6,a2=sy.symbols('d1 d4 d6 a2')
q1,q2,q3,q4,q5,q6=sy.symbols('q1 q2 q3 q4 q5 q6')

'''
|_i_|_theta_|_d_|_a_|_alpha_|_q_|
| 1 |   0   |d1 | 0 |   0   |ql |
| 2 |   0   | 0 | 0 |   0   |q2 |
| 3 |  -90  | 0 |a2 |   0   |q3 |
| 4 |  -90  |d4 | 0 |  -90  |q4 |
| 5 |  -90  | 0 | 0 |  -90  |q5 |
| 6 |   0   |d6 | 0 |   90  |q6 |
'''

# 定义DH参数
theta=[0, 0, -sy.pi/2, -sy.pi/2, -sy.pi/2, 0]
d=[d1, 0, 0, d4, 0, d6]
a=[0, 0, a2, 0, 0, 0]
alpha=[0, 0, 0, -sy.pi/2, -sy.pi/2, sy.pi/2]
# 运行轨迹时各轴相对零位的实际角位移
q=[q1, q2, q3, q4, q5, q6]

# 定义A矩阵的计算函数(MDH方法)
def mdh_matrix(alpha, a, d, theta):
    matrix = sy.eye(4)
    matrix[0,0] = sy.cos(theta)
    matrix[0,1] = -sy.sin(theta)
    matrix[0,2] = 0
    matrix[0,3] = a
    matrix[1,0] = sy.sin(theta)*sy.cos(alpha)
    matrix[1,1] = sy.cos(theta)*sy.cos(alpha)
    matrix[1,2] = -sy.sin(alpha)
    matrix[1,3] = -sy.sin(alpha)*d
    matrix[2,0] = sy.sin(theta)*sy.sin(alpha)
    matrix[2,1] = sy.cos(theta)*sy.sin(alpha)
    matrix[2,2] = sy.cos(alpha)
    matrix[2,3] = sy.cos(alpha)*d
    matrix[3,0] = 0
    matrix[3,1] = 0
    matrix[3,2] = 0
    matrix[3,3] = 1
    return matrix

# 根据T计算[x,y,z,a,b,c]
def tform2pos(T):
    temp=sy.sqrt(T[0,0]**2+T[1,0]**2)
    if temp<1e-6:
        a=sy.atan2(-T[1,2],T[1,1])
        b=sy.atan2(-T[2,0],temp)
        c=0
    else:
        a=sy.atan2(T[2,1],T[2,2])
        b=sy.atan2(-T[2,0],temp)
        c=sy.atan2(T[1,0],T[0,0])

    x=T[0,3]
    y=T[1,3]
    z=T[2,3]
    a=a/sy.pi*180
    b=b/sy.pi*180
    c=c/sy.pi*180
    
    return sy.Matrix([x, y, z, a, b, c])

# 计算基座与末端的T矩阵
T=sy.eye(4)

for i in range(6):
    if i==1:
        A=mdh_matrix(alpha[i], a[i], d[i]+q[i], theta[i])
    else:
        A=mdh_matrix(alpha[i], a[i], d[i], theta[i]+q[i])

    # sy.pprint(sy.simplify(A))
    T=T*A
    
T=sy.simplify(T)

s1,s3,s4,s5,s6,s13=sy.symbols('s1 s3 s4 s5 s6 s13')
c1,c3,c4,c5,c6,c13=sy.symbols('c1 c3 c4 c5 c6 c13')
T=T.subs([(sy.sin(q1),s1),(sy.sin(q3),s3),(sy.sin(q4),s4),(sy.sin(q5),s5), \
          (sy.sin(q6),s6),(sy.sin(q1+q3),s13), \
          (sy.cos(q1),c1),(sy.cos(q3),c3),(sy.cos(q4),c4),(sy.cos(q5),c5), \
          (sy.cos(q6),c6),(sy.cos(q1+q3),c13)])

for i in range(3):
    for j in range(4):
        print(T[i,j])


'''
# 带入DH参数，并设置角位移为[0,0,0,0,0,0]
temp=T.subs([(a1,145),(a2,870),(a3,170),(d1,530),(d4,1039),(d6,225), \
             (q1,0),(q2,0),(q3,0),(q4,0),(q5,0),(q6,0)])
sy.pprint(temp)
print('_'*20)

# 带入DH参数，并设置角位移为[-45,0,0,0,0,90]
temp=T.subs([(a1,145),(a2,870),(a3,170),(d1,530),(d4,1039),(d6,225), \
             (q1,-np.pi/4),(q2,0),(q3,0),(q4,0),(q5,0),(q6,np.pi/2)])
sy.pprint(temp)
print('_'*20)

# 带入DH参数，并设置角位移为[0,180,-90,45,30,0]
temp=T.subs([(a1,145),(a2,870),(a3,170),(d1,530),(d4,1039),(d6,225), \
             (q1,0),(q2,np.pi),(q3,-np.pi/2),(q4,np.pi/4),(q5,np.pi/6),(q6,0)])
sy.pprint(temp)
print('_'*20)

# 带入DH参数，并设置角位移为[-10,18,-60,45,80,-90]
temp=T.subs([(a1,145),(a2,870),(a3,170),(d1,530),(d4,1039),(d6,225), \
             (q1,-np.pi/18),(q2,np.pi/10),(q3,-np.pi/3),(q4,np.pi/4),(q5,np.pi/9*4),(q6,-np.pi/2)])
sy.pprint(temp)
print('_'*20)
'''
