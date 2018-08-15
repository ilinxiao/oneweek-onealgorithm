import math

"""
旅行最佳出发点问题
假设你要去以下几个城市旅游，利用贪婪算法计算近似最优解来规划你的行程。
假设所有城市在一个刻度单位为1的坐标系内，每个城市的位置用坐标(x,y)来表示。
"""

cities = ['马林', '旧金山', '伯克利', '傅里蒙特', '帕洛阿尔托']

data = {}
data['马林'] = (2,5)
data['旧金山'] = (4,4)
data['伯克利'] = (2,3)
data['傅里蒙特'] =(6,2)
data['帕洛阿尔托'] = (7,5)

def get_distance(start, end):
    """
    计算各点之间的直线距离，即xy坐标值之差的绝对值组成的直角三角形的斜边长度
    """
    radio = 100
    point_a = data[start]
    point_b = data[end]
    x = abs(point_a[0] - point_b[0])
    y = abs(point_a[1] - point_b[1])
    dist =  math.ceil(math.sqrt(x ** 2 + y ** 2) * radio)   
    
    # print('%d ** 2 + %d ** 2 = %f ** 2 * %d = %f' % (x, y, math.sqrt(x ** 2 + y ** 2), radio, dist))
    # print('%s →  %s : %d km' % (start, end, dist))
    return dist
    
distances = {} 
print("生成所有城市相互之间的距离表")
for city in data.keys():
    distances[city] = {}
    for key, point in data.items():
        if key != city:
            distances[city][key] = get_distance(city, key)

print(distances)
            
    
def trip_plan(start, to_cities, trip_records=[]):
    
    if not trip_records:
        trip_records.append({start:0})
        to_cities.remove(start)
        
    if not to_cities:
        return trip_records
        
    near_distance = float('inf')
    near_city = None
    for end in to_cities:
        if start != end:
            repeat = False
            for record in trip_records:
                if end in record.keys():
                    repeat = True
                    break
           
            if not repeat:
                distance = distances[start][end]
                if distance < near_distance:
                    near_distance = distance
                    near_city = end
                
    trip_records.append({near_city: near_distance})
    # print(to_cities)
    # print(near_city)
    to_cities.remove(near_city)            
    return trip_plan(near_city, to_cities, trip_records)
    
if True:
    print('分别计算从每一个城市出发，最后的总行程数：')
    for start in cities:
        
        to_cities = cities.copy()
        trip_records = trip_plan(start, to_cities, [])
        # print(trip_records)
        total_distance = 0
        for i in range(len(trip_records)):
            step = trip_records[i]
            total_distance += list(step.values())[0]
            print(list(step.keys())[0], end='')
            if i < len(trip_records)-1:
                print('→', end='')
            
        print('\t total:%d' % total_distance)
# print(trip_plan('马林', cities.copy())) 