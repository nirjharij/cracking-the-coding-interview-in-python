class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_best_line(points):
    slope_dict = {}
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1 = points[i].x
            y1 = points[i].y
            x2 = points[j].x
            y2 = points[j].y
            if x2-x1 == 0:
                slope = "infinite"
            else:
                slope = (y2 - y1) / (x2 - x1)
            if slope in slope_dict:
                slope_dict[slope].extend([(x1, y1), (x2, y2)])
            else:
                slope_dict[slope] = [(x1, y1), (x2, y2)]
    print(slope_dict)
    max_count = 0
    for item in slope_dict:
        count = len(set(slope_dict[item]))
        if count > max_count:
            max_count = count
            best_slope = item

    p1 = slope_dict[best_slope][0]
    y_intercept = p1[1] - best_slope * p1[0]
    best_line = str(best_slope) + 'x' + ' + ' + str(y_intercept)
    print(best_line)


find_best_line([Points(1, 2), Points(1, 1), Points(2, 3), Points(3, 4), Points(5, 6), Points(3, 3)])
