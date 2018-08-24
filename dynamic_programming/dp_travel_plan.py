"""
景点游览问题
"""
import numpy

class DPTravelPlan():
    
    def __init__(self, attractions, time, particle=1):
        #初始化
        self.records = []
        self.attractions = attractions
        self.time = time
        self.particle = particle
        
    def calc(self):
    
        for row in range(len(self.attractions)):
            self.records.append([])
            tmp_attractions = self.attractions[:row+1]
            attractions_name = [g['name'] for g in tmp_attractions]
            # print('当前可去的景点：%s' % attractions_name)
            current_attractions = self.attractions[row]
            name = current_attractions['name']
            time = current_attractions['time']
            score = current_attractions['score']
            # print('当前景点：%s' % name)
            for cap in numpy.linspace(self.particle, self.time, self.time//self.particle):
                self.records[row].append([])
                
                column = int(cap//self.particle) -1
                # print('row:%s&column:%s&cap:%s' % (row, str(column), str(cap)))
                # print('当前可用时间:%.1f天' % cap)
                max_package = self.get_package(row-1, column)
                # print('max package:%s' % max_package)
                max_score = self.get_package_value(max_package)
                # print('>>该时间内最佳游览景点指数：%d' % max_score)
                
                new_score = score
                remainder_score = 0
                remainder_time = cap - time
                # print('remainder_time:%s' % str(remainder_time))
                remainder = self.get_package(row-1, int(remainder_time//self.particle)-1)
                if remainder:
                    for g in remainder:
                        if g == current_attractions:
                            remainder = []
                            break
                    
                    # print('remainder package:%s' % remainder)
                    remainder_score = self.get_package_value(remainder)
                    # print('>>剩余时间最佳游览指数：%d' % remainder_score)
                if remainder_time < 0:
                    new_score = 0
                    
                new_package = []
                if new_score + remainder_score > max_score:
                    new_package.append(current_attractions)
                    new_package.extend(remainder)
                else:   
                    new_package = max_package
                # print('new package:%s' % new_package)
                self.set_package_value(row, column, new_package)
                
        self.output()
        
    def output(self):
        best_plan = ''
        best_score = 0
        for i in range(len(self.records)):
            row = self.records[i]
            for j in range(len(row)):
                package = row[j]
                names = ''
                total_value = 0
                for g in range(len(package)):   
                    if g > 0:
                        names += ','
                    names += package[g]['name']
                    total_value += package[g]['score']
                if total_value > best_score:
                    best_score = total_value
                    best_plan = names
                # print('(%d)' % total_value, end='')
                # print(names, end='|')
            # print('')
        print("最佳方案：%s,游览指数:%d" % (best_plan, best_score))
            
    def get_package_value(self, package):
        value = 0
        if package:
            for g in package:
                value += g['score']
        return value
        
    def get_package(self, row, column):
        try:
            if row < 0 or column < 0:
                raise Exception('错误的索引值.')
            package = self.records[row][column]
        except Exception as e:
            # print('exception in get_package:%s' % e)
            return []
        return package
        
    def set_package_value(self, row, column, package):
        self.records[row][column] = package
            
if __name__ == '__main__':
    time = 2
    attractions = []
    particle = 0.5
    attractions.append({'name': '威斯敏斯特教堂', 'time':0.5, 'score':7})
    attractions.append({'name': '环球剧场', 'time':0.5, 'score':6})
    attractions.append({'name': '英国国家美术馆', 'time':1, 'score':9})
    attractions.append({'name': '大英博物馆', 'time':2, 'score':9})
    attractions.append({'name': '圣保罗大教堂', 'time':0.5, 'score':8})
    test = DPTravelPlan(attractions, time, particle=particle)
    test.calc()