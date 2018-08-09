"""
Dijkstra's Algorithm
狄克斯特拉算法
适用条件：
有向无环正加权图最快路径搜索
"""
from collections import deque

data = dict()
data['A'] = {'B': 4, 'C': 10}
data['B'] = {'D': 21}
data['C'] = {'E': 5, 'F': 8}
data['D'] = {'G': 4}
data['E'] = {'D': 5}
data['F'] = {'D': 12}
data['G'] = None

start = 'A'
end = 'G'

def dijkstra_search(data, start, end):
    #记录最佳的开销
    best_cost={}
    #循环队列，存储的是每个节点的名称
    #队列的选择条件：有序、FIFO
    search_queue = deque()
    search_queue.append(start)
    
    #第一部分 根据权值查找并更新最优路径
    while search_queue:
        parent_node_name = search_queue.popleft()
        print('searching node is :%s' % parent_node_name)
            
        nodes = data[parent_node_name]
        nodes_cp = nodes.copy() if nodes else []                
        while len(nodes_cp) > 0:
            #累加前面节点的消费
            base_cost = 0
            for key,value in best_cost.items():
                if key[1] == parent_node_name:
                    base_cost += best_cost[key]
                    print('check base cost plus. key is :%s, current cost:%d, base cost:%d' % (key, best_cost[key], base_cost))
                    
            #按照权值由小到大遍历节点
            min_node_name,min_cost = get_min_node(nodes_cp)
            print('sub node:%s, base_cost:%d, cost:%d' %(min_node_name, base_cost, min_cost))
            min_cost += base_cost
            
            min_edge = get_edge(parent_node_name, min_node_name)
            #更新最佳消费 代码的写法非常依赖数据存储的方式
            exists_sign = False
            for tkey in best_cost.keys():
                if tkey[1] == min_node_name:
                    exists_sign = True
                    break
            if not exists_sign:
                best_cost[min_edge] = min_cost
            else:    
                best_cost_cp = best_cost.copy()
                for key,value in best_cost_cp.items():
                    if key[1] == min_node_name:
                        if best_cost[key] > min_cost:
                            best_cost[min_edge] = min_cost
                            best_cost.pop(key)
            
            #保证不重复搜索       
            nodes_cp.pop(min_node_name)
            
            if parent_node_name != end:
                # 到达终点后停止添加子节点
                search_queue.append(min_node_name)
    print('best cost table:%s' % best_cost)
    
    #第二部分 输出最优路径
    def find_path(node_name):
        exists_sign = False
        key = ''
        for tkey in best_cost.keys():
            if tkey[1] == node_name:
                exists_sign = True
                key = tkey
                break
        if not exists_sign:
            return node_name
        else:
            return find_path(tkey[0]) + node_name
            
    print('best cost path:%s' %(find_path(end)))
    
def get_min_node(nodes):
    min_cost = 0
    min_node_name = ''
    
    for node_name,cost in nodes.items():
        if min_cost == 0:
            min_cost = cost
            min_node_name = node_name
            
        if min_cost > cost:
            min_cost = cost
            min_node_name = node_name
    # print('current min node is :%s -- (min node check,)' % min_node_name)        
    return min_node_name, min_cost
    
def get_edge(start, to):
    return start+to
        
dijkstra_search(data, start, end)