def countPoints(points,queries):

    result = []

    def insideCircle(p,cir):
        dist =(((p[0] - cir[0]) ** 2) + ((p[1] - cir[1]) ** 2)) ** 0.5
        return dist <= cir[2]
    
    for cir in queries:
        c = 0

        for p in points:
            if insideCircle(p,cir):
                c += 1
        result.append(c)

    return result



# print(countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))
print(countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]],[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))
