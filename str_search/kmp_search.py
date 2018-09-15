
def get_next(P):
    """
        KMP模式匹配第二部分：求解模式串P的next数组。该函数也叫失配函数。
        next数组表示模式串P中每一个字符的前面有最大长度的相同前缀后缀值。
        next数组的理解，应该先从P的每个字符最大长度前缀后缀表开始。
        假设P='LINXILO'，最大长度前缀后缀表为：[0,0,0,0,0,1,0]，也就是说只有在第五个位置'L'上才出现一个长度为1的相同前缀后缀。
        next数组就是最大长度前缀后缀表整体上往前移一位。
        所以，当P='LINXILO'时，next数组为：[-1,0,0,0,0,0,1]
                    
        当P='LINXILO'时，函数运行步骤（>是逻辑判断，一行一次循环）：
        i=0,j=-1 > j==-1 > i=1,j=0,next[1]=0
        i=1,j=0 > 'I' != 'L' > j = next[j] = next[0] = -1
        i=1,j=-1 > i=2,j=0,next[2]=0
        i=2,j=0 > 'N' != 'L' > j=next[j]=-1 
        i=2,j=-1 > j=0,i=3,next[3]=0
        i=3,j=0 > 'X' != 'L' > j=next[j]=-1 
        i=3,j=-1 > i=4,j=0,next[4]=0
        i=4,j=0 > 'I' != 'L' > j=next[j]=-1
        i=4,j=-1 > i=5,j=0,next[5]=0
        i=5,j=0 > 'L' == 'L' > i=6,j=1,next[6]=1
        i=6,j=1 > 'O' != 'I' > j=next[1]=-1
        i=6,j=-1 > i=7,j=0,next[7]=0
        break
        
        j,i分别是模式串前缀后缀起始位置
        当前缀后缀失配时，递归next数组当中前缀位置j对应的值与后缀位置i进行比较。
        以上个人粗浅的总结，感觉并没有很准确的描述next数组的求解过程。
        更详细的解析过程请参考这篇文章：https://blog.csdn.net/v_july_v/article/details/7041827
    """
    i=0
    j=-1
    plen = len(P)
    next = [-1 for x in range(plen)]
    
    while(i<plen):
    
        if j==-1 or P[i] == P[j]:
            i+=1
            j+=1
            if i<plen:
                next[i] = j
        else:
            j = next[j]
    return next
    
P = 'LINXILO'
# P = "ABCDABCE"
# P = 'ABCDABDE'
next = get_next(P)
print(next)

def kmp_search(S,P,start):
    """
        KMP模式匹配
        使用KMP算法实现在文本串S当中,从start位置开始搜索P第一次出现的位置。未找到返回-1。
    """
    i=start
    j=0
    slen=len(S)
    plen=len(P)
    next = get_next(P)
    
    while (i<slen and j<plen):
        
        if j==-1 or S[i] == P[j]:
            i+=1
            j+=1
        else:
            j = next[j]
    '''
    ACBCD
          BC
    '''
    if j - plen == 0:
        return i - j
    return -1
    
    
# S = "I'M LINXIAO,NOT LINXILO"
S = "NOT LINXILO"
print(kmp_search(S,P,5))
print(kmp_search(S,P,0))