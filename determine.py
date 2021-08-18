def findFeature(file1, file2):  #第一份檔案 : 左手圓極化; 第二份檔案 : 軸比
    import csv
    
    def intersectx(x1, y1, x2, y2, targety):
        return x1 + (x2 - x1)/ (y2 - y1) * (targety -y1)
    
    out = [] #左手圓極化 max / 3dB / localMax / localMin / Side Lobe Gain #軸比 3dB
    
    
    with open(file1, "r") as f1:
        ls = list(csv.reader(f1))
        ls1 = []
        for element in ls:
            ls1.append(float(element[0]))
        ls1 = ls1[0:268]
        main = max(ls1)
        out.append(main)
        k = ls1.index(main)
        m = k
        while ls1[k] > (main -3) :
            k -= 1
        L = intersectx(k-180, ls1[k], k-179, ls1[k+1], main-3)
       
        while ls1[m] > (main -3) :
            m += 1
        H = intersectx(m-180, ls1[m], m-181, ls1[m-1], main-3)
        out.append(H - L)
        
        localMax = []
        ind1 = []
        former = ls1[0]
        for i in range(1, 267):
            if ls1[i] > former and ls1[i] > ls1[i+1]:
                localMax.append(ls1[i])
                ind1.append(i)
            former= ls1[i]
        out.append(len(localMax))
        
        localMin = []
        ind2 = []
        former2 = ls1[0]
        for i in range(1, 267):
            if ls1[i] < former2 and ls1[i] < ls1[i+1]:
                localMin.append(ls1[i])
                ind2.append(i)
            former2= ls1[i]
        out.append(len(localMin))

        out.append(localMax[localMax.index(max(localMax))-1])
        
    with open(file2, 'r') as f2:
        l2 = list(csv.reader(f2))
        
        ls2 = []
        for element in l2:
            ls2.append(float(element[0]))
        center = ls2[len(ls2)//2]
        
        x = ls2.index(center)
        y = x
        while ls2[x] < center +3 :
            x -= 1
        l = intersectx(x-180, ls2[x], x-179, ls2[x+1], center+3)
       
        while ls2[y] < center +3 :
            y += 1
        h = intersectx(y-180, ls2[y], y-181, ls2[y-1], center+3)
        out.append(h - l)
        
    return out






