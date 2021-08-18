def sol1(width):  #LHCP Main Lobe 3dB 1.00~3.00
    print('Regression using sol1.')
    return (width - 28.494819578847398) / (-0.9386429844375036)

def sol2(width): #LHCP Main Lobe 3dB 5.00~6.00
    print('Regression using sol2.')
    return (width - 32.35635517335582) / (-1.5042113618496489)

def sol3(gain): #LHCP Side Lobe Gain 3.60~5.00
    print('Regression using sol3.')
    return (gain - 7.35078294293288) / (-1.988773569941961)

def sol4(width): # AR 3dB Width 2.75~3.80
    print('Regression using sol4.')
    return (width - 71.45141730769) / (-10.422655001119526)

