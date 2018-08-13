

class Dijkstra2:
    
    def __init__(self, start, end, data):
        self.start = start
        self.end = end
        self.data = data
        
        self.costs = {}
        self.parents = {}
        self.processed  = []
    def search(self):
        
        self.costs['A'] = 6
        self.costs['B'] = 2
        self.costs['end'] = float('inf')
        self.parents['A'] = 'start'
        self.parents['B'] = 'start'
        self.parents['end'] = None
        
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.data[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
                    
            self.processed.append(node)
            node = self.find_lowest_cost_node()
        return self.parents
    
    def find_lowest_cost_node(self):
        lower_cost = float('inf')
        lower_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lower_cost and node not in self.processed:
                lower_cost = cost
                lower_cost_node = node
        return lower_cost_node
        
if __name__ == '__main__':

    data = {}
    data['start'] = {'A':6, 'B':2}
    data['A'] = {'end':1}
    data['B'] = {'A':3, 'end':5}
    data['end'] = {}
    
    start = 'start'
    end = 'end'
    d = Dijkstra2(start, end, data)
    result = d.search()
    print(result)
    print(d.costs)
        