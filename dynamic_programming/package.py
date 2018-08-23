"""
动态规划学习一
背包问题
"""
import numpy

class DPPackage():
    
    def __init__(self, goods, capacity):
        """
        best:[
        [{goods1, goods2, ...}],
        [{goods1, ...}]
        ]
        """
        #初始化
        self.records = []
        for i in range(len(goods)):
            self.records.append([])
            for  j in range(capacity):
                self.records[i].append([])
        # print(self.records)
        
    def calc(self):
        """
            计算公式是：在 （当前物品的价值:value + 剩余最大价值:remainder_value）与 已计算该重量背包可装最大值:max_value 两者中取最大值
            value = current_goods.value if current_goods.weight < current_capacity else 0
            remainder_value  = self.records[current_goods.weight - current_capacity].value (索引为负返回0)
            max_value = self.records[current_row-1][current_column].value
            最佳背包方案是最后的取值
        """
        for i in range(len(goods)):
            tmp_goods = goods[:i+1]
            goods_name = [g['name'] for g in tmp_goods]
            row = i 
            print('当前可偷取物品：%s' % goods_name)
            current_goods = goods[row]
            name = current_goods['name']
            weight = current_goods['weight']
            value = current_goods['price']
            print('当前物品：%s' % name)
            for column in range(capacity):
                cap = column + 1
                print('当前背包负重:%dKg' % cap)
                max_package = self.get_package(row-1, column)
                # print('max package:%s' % max_package)
                max_value = self.get_package_value(max_package)
                print('>>该负重已记录最大值：%d' % max_value)
                
                new_value = value
                remainder_value = 0
                remainder_weight = cap - weight
                remainder = self.get_package(row-1, remainder_weight-1)
                if remainder:
                    for g in remainder:
                        if g == current_goods:
                            remainder = []
                            break
                    
                    # print('remainder package:%s' % remainder)
                    remainder_value = self.get_package_value(remainder)
                    print('>>当前剩余负重最大值：%d' % remainder_value)
                if remainder_weight < 0:
                    new_value = 0
                    
                new_package = []
                if new_value + remainder_value > max_value:
                    new_package.append(current_goods)
                    new_package.extend(remainder)
                else:   
                    new_package = max_package
                # print('new package:%s' % new_package)
                self.set_package_value(row, column, new_package)
                
        self.output()
        
    def output(self):
        for i in range(len(self.records)):
            row = self.records[i]
            for j in range(len(row)):
                package = row[j]
                names = ''
                for g in range(len(package)):   
                    if g > 0:
                        names += ','
                    goods = package[g]
                    names += goods['name']
                print(names, end='|')
            print('')
            
    def get_package_value(self, package):
        value = 0
        if package:
            for g in package:
                value += g['price']
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
    capacity = 5
    goods = []
    goods.append({'name': 'guitar', 'weight':1, 'price':1500})
    goods.append({'name': 'laptop', 'weight':3, 'price':2000})
    goods.append({'name': 'sound', 'weight':4, 'price':3000})
    goods.append({'name': 'iphone', 'weight':2, 'price':2500})
    test = DPPackage(goods, capacity)
    test.calc()