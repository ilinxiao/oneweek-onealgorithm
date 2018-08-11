from collections import deque
"""
最短路径搜索:breadth-first search BFS 广度优先搜索
代码场景：想认识某人在联系人及其联系人列表中查找，输出最短结交路径。
实现要点：
1.体现关系的层级关系
    递归展现层级的关系偏向是一个整体。
"""
class BFS():

    def __init__(self):
        self.data = {}
        self.init_data()
    
    def init_data(self):
        contact_list = {}
        contact_list['coco'] = ['linxiao']
        contact_list['linxiao'] = ['xiaoming', 'xiaolong', 'xiaogui'] #一度关系 如果单度关系再分级，就按照条件进行排序。跟dikjstra一样了。
        contact_list['xiaoming'] = ['kitty', 'talasuo', 'jack'] #二度关系
        contact_list['xiaogui'] = ['superman', 'orangeman', 'linxiao'] #二度关系
        contact_list['superman'] = [ 'hellokitty']
        contact_list['hellokitty'] = ['linxiao', 'yiyang', 'jony']
        contact_list['yiyang'] = ['mango']
        self.data = contact_list

    def search(self, my_name, who):
        print('hello, %s! i can help you find \'%s\' in you friends and they friends with most quickly way.'  % (my_name, who))
        search_queue = deque()
        search_queue.append(my_name)
        searched = []
        path = {}
        found = False
        while search_queue:
            
            name = search_queue.popleft()
            if name not in searched:
                print('searching %s\'s friends.' % name)
            
                if name not in self.data.keys():
                    continue
                
                path[name] = []
                friends = self.data[name]
                
                for friend in friends:
                    path[name].append(friend)
                    if friend.find(who) >= 0:
                        print('found man is :%s' % name)
                        found = True
                        break
                
                if found:
                    break
                 
                searched.append(name)
                
                if name in self.data.keys():
                    search_queue += self.data[name]
                
        if found:        
            print(path)   
            print(self.print_path(who, path))
        else:
            print('oops! not found the man called: %s.' % who)
                               
    def print_path(self, friend, path):
        """
            path存储两层级关系
        """         
        found = False
        
        for key, names in path.items():
            for name in names:
                if name.find(friend) >=0:
                    #避免重复
                    path.pop(key)
                    return self.print_path(key, path) + ' > ' + friend
        
        #到达起点
        if not found:
            return friend
            
            
if __name__ == '__main__':
    bfs = BFS()
    # print(bfs.data)
    bfs.search('linxiao', 'mango')
    # print(bfs.print_path('mango', bfs.data))
    '''
        单从这段代码的结果和联系人存储方式上来看search之后调用print_path和直接调用print_path结果一样。
        但print_path目的只是用于打印，未曾考虑起点情况，虽然加入起点判断效果又趋于一致，但在实际应用中
        也许会有其他更多需要考虑的因素时，两者结合应该会更灵活。
    '''