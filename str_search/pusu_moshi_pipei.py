'''
朴素的模式匹配
'''


def index(S, T, pos):
    #查找并返回T在S中从pos位置开始的位置，若T不是S的子串，则返回-1
    i, j , slen, tlen = (pos, 0, len(S), len(T))
    while (i<slen and j<tlen):
        if (S[i] == T[j]):
            i+=1
            j+=1
        else:
            print('i:%d\tj:%d' % (i,j))
            i = (i - j) + 1
            j =0
    if (j >= tlen):
        #只有当匹配成功 j的值才有可能增加到tlen
        return i - tlen
    return -1
    
S = 'linxiao'
T = 'ii'
'''
1:i=0,j=0 l!=i > i=(i-j)+1=1 j=0
2:i=1,j=0 i==i > i=2 j=1
3:i=2,j=1 n!=i > i=(i-1)+1=2 j=0
4:i=2,j=0 n!=i > i=(i-0)+1=3 j=0
5:i=3,j=0 x!=i > i=(i-0)+1=4 j=0
6:i=4,j=0 i==i > i=5 j=1 
7:i=5,j=1 a!=i > i=(5-1)+1=5 j=0
8:i=5,j=1 a!=i > i=(5-0)+1=6 j=0
9:i=6,j=0 o!=i > i=(6-0)+1=7 j=0
i == len(S) > break
if j == tlen : print('match sucess.')

print(index(S, T , 0))