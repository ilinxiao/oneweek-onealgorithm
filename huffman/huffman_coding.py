
"""
哈夫曼编码
也叫最优二叉树。
应用场景分析：
为了人与机器人实现对话，需要把人类的语言编码为机器能懂的形式。
为了提高通信效率，将根据人类语言中使用频率高的字母采用尽可能短的编码。
"""

class Node:
    def __init__(self, ch, weight, parent, lchild, rchild, index=-1):
        self.ch=ch
        self.weight=weight
        #parent/lchild/rchild 父子节点的坐标, -1表示为空
        self.parent=parent
        self.lchild,self.rchild=lchild, rchild
        #index用来显示当前节点在list中索引位置，帮助调试
        self.index = index
    
    def __repr__(self):
        return 'char:{},weight:{},parent:{},lchild:{},rchild:{},index:{}\n'.format(self.ch, self.weight, self.parent, self.lchild, self.rchild, self.index)
    
def select_min(nodes, num=2):
    """
     从指定列表当中选取num数量的权值最小节点，根据 Node的定义，权值不为None，父节点为-1才表示该节点未在树中
     return：num数量节点的索引位置
    """
    min_indexes = []
    for i in range(num):
        min_weight = float('inf')
        min_index = -1
        for f in range(len(nodes)):
            node = nodes[f]
            if node.weight and node.parent == -1:
                weight = node.weight
                if (min_weight > weight) and (f not in min_indexes):
                    min_weight = weight
                    min_index = f
        min_indexes.append(min_index)
    return min_indexes
    
def create_huffman_tree(T, W):
    """
    创建哈夫曼树
    """
    nodes = []
    n = len(T)
    m = 2*n-1
    for i in range(n):
        nodes.append(Node(T[i], W[i], -1, -1, -1, i))
   
    for i in range(n,m):
        #每次循环选取最小权值的两个节点组成新的节点
        lnode_index,rnode_index = select_min(nodes)
        # rnode_index,lnode_index = select_min(nodes)
        # print('left node index:%d' % lnode_index)
        #两个最小节点分别作为新节点的左右节点
        lnode = nodes[lnode_index]
        rnode = nodes[rnode_index]
        # print('left child weight:%s' % str(lnode.weight))
        #新的节点权值为左右节点的和
        new_weight = lnode.weight + rnode.weight
        #初始化新节点，并且父节点信息为-1，表示有可能在接下来的循环中与nodes中其他节点组成新的树
        new_node = Node(None, new_weight, -1, lnode_index, rnode_index, i)
        #更新左右节点的父节点信息
        lnode.parent = i
        rnode.parent = i
        
        #将新节点添加到队列
        nodes.append(new_node)
        
        # print('nodes length:%d' % len(nodes))
    return nodes
   
def find_node(nodes, ch):
    '''
    在哈夫曼树中查找节点
    return：节点位置
    '''
    for i in range(len(nodes)):
        if ch == nodes[i].ch:
            return i
    return -1
    
def huffman_coding(nodes, text):
    '''
    哈夫曼编码
    以哈夫曼树为基础，分别对文本的每个字符做编码。
    过程：查找字符在树中的位置作为编码起点，如果该节点为父节点的左子树，编码串累加0；如果该节点为父节点的右子树，编码串累加1。
    向上遍历，直至到根节点。
    注意点：
    1.编码串累加的方式是先遍历的节点路径编码值累加到尾部，以此所有节点的编码都是由根节点往下依次到叶节点。这样才能保证编码符合前缀码规则。
    2.非在编码树中的字符以及当文本中出现0,1时，如何处理比较妥当还待学习。
    return:(code, code_list)
                code:编码完成的字符串
                code_list:[{},{},...] 每个字符编码的详细情况，仅用于检查编码的正确性
    '''
    code = ''
    code_list = []
    for i in range(len(text)):
        ch = text[i]
        node_index = find_node(nodes, ch)
        # print('node index:%d, node:%s' % (node_index, ch))
        ch_code = ''
        code_detail = {} 
        if node_index == -1:
            ch_code += ch
        else:
            while True:
                node = nodes[node_index]
                parent_index = node.parent
                
                if parent_index == -1:
                    #翻转字符
                    # code_list = list(ch_code)
                    # for i in range(len(code_list)//2):
                        # c = code_list[i]
                        # code_list[i] = code_list[-i-1]
                        # code_list[-i-1] = c
                    # ch_code = ''.join(code_list)
                    break
                
                parent = nodes[parent_index]
                if parent.lchild == node.index:
                    ch_code = '0' + ch_code #累加的顺序很大程度上决定了编码的正确性
                else:
                    ch_code = '1' + ch_code
                    
                node_index = parent_index
        # print('char:%s==%s' % (ch, ch_code))
        code += ch_code
        code_detail[ch] = ch_code
        code_list.append(code_detail)
        # code[ch] = ch_code
    return code, code_list

def decoding(nodes, code):
    '''
    哈夫曼解码
    过程：以哈夫曼树为基础，从根节点遍历编码串，当编码串字符为0，则往该节点的左子树遍历；为1，则往该节点的右子树遍历，直到到达叶节点，重置遍历的起点为根节点。
    当编码串字符不存在树中直接返回该字符不处理，重置遍历的起点为根节点。
    '''
    root = nodes[len(nodes)-1]
    node = root
    text = ''
    for i in range(len(code)):
    
        c = code[i]            
        if c != '0' and c != '1':
            text += c #不在编码字符列表内的字符直接返回
            node = root
        else:
            # print('node: ch is %s, lchild is :%d, rchild is %d.' % (node.ch, node.lchild, node.rchild))
            if c == '0':
                node = nodes[node.lchild]
            else:
                node = nodes[node.rchild]
                
            if node.ch is not None and node.lchild == -1 and node.rchild == -1:
                text += node.ch
                node = root
                
    return text
    
if __name__ == '__main__':
    #示例字母
    # T = ['A', 'C', 'D', 'K', 'J', 'Z']
    #根据总量大概100000个单词的英文小说统计各字母出现的频率分布
    Probability = {"q":1448, "j":1630, "x":2108, "z":3410, "w":7062, 
     "k":7550, "v":7900, "f":10556, "y":12457, "b":15303, 
     "h":18143, "m":21179, "p":21777, "g":23047, "u":25806,
      "d":29423, "c":31145, "l":41195, "o":47311, 
     "t":51649, "n":55550, "r":56424, "a":60670, "i":67014,
      "s":67506, "e":88677}

    T = []
    W = []
    for key, value in Probability.items():
        T.append(key)
        
        w = value / 100000
        W.append(w)
    print(T)
    print(W)
    
    # if len(set(W)) != len(W) or len(set(T)) != len(T):
        # raise RuntimeError('相同的字符或概率值。')
    
    # 初始化哈夫曼树
    nodes = create_huffman_tree(T, W)
    # text = ''.join(sorted(T))
    text = 'linxiwrwquroquroqao'
    # T1 = ['a', 'b', 'c', 'd', 'e']
    # W1 = [0.30, 0.25, 0.15, 0.22, 0.08]
    # nodes = create_huffman_tree(T1, W1)
    # print(nodes)
    # text = 'hello,world!'
    # text = ''.join(sorted(T1))+',e'
    # text = 'a'
    print('编码文本：%s' % text)
    text_code, code_detail = huffman_coding(nodes, text)
    print('编码结果: %s ' % text_code)

    #检查编码的正确性
    check_code = True
    for i in range(len(code_detail)):
        obj = code_detail[i]
        key = list(obj.keys())[0]
        value = list(obj.values())[0]
        # print('%d. %s = %s' % (i, key, value))
        for j in range(len(code_detail)):
            obj2 = code_detail[j]
            char = list(obj2.keys())[0]
            code = list(obj2.values())[0]
            if i != j and key != char:
                result = code.startswith(value)
                if result:
                    check_code = False
                    print('char:%s, code:%s' % (key, value))
                    print('char:%s, code:%s' % (char,code))
    
    if not check_code:
        print('编码不通过。')
    else:
        print('编码通过。')
        
    decode_text = decoding(nodes, text_code)
    print('解码测试：%s' % decode_text)
    if decode_text == text:
        print('解码通过。')
    else:
        print('解码失败。')
    