# Dk-Analysis
Material Measurements Algorithm
## 設計理念
從複雜的、高維度的input data 中篩選、歸納，找到"那些重要的特徵對Dk變化是敏感的"，將這些特徵做出規律、運用基礎的數學技巧取代過去複雜機制才能達成的任務，並克服過去硬體技術上的限制

## 設計天線
![image](https://user-images.githubusercontent.com/55400183/131245081-04208068-a469-4bae-afdc-0205c0a589bd.png)<br>
在下方的圓極化陣列結構中加入障礙物，觀察障礙物Dk從1到6浮動時造成的漸進式變化，歸納、算出回歸方程，藉以預測更多未知待測物的材料電性

## 目標(宇集)
1. 單變數演算法 : 分析範圍Dk = 1.00 ~ 6.00, linear step = 0.01
2. 雙變數演算法 : 加入分析Df = 0.00 ~ 0.05, linear step = 0.002
3. 三變數演算法(未來展望) : 加入待測物厚度 1.0mm ~ 4.0mm, linear step = 0.1mm

## 關鍵資料
### 左手圓極化(LHCP) Gain Plot
從Main Lobe最大增益、3dB寬度與Local Max / Local Min觀察變化<br>
![image](https://user-images.githubusercontent.com/55400183/131245554-43fb52b5-0c63-4fc2-bffe-ddff257e9b35.png)
### 軸比(AR) Plot
從中心3dB寬度分析，也考慮Local Max / Min改變<br>
![image](https://user-images.githubusercontent.com/55400183/131245604-2ef86e1f-b590-417c-97c3-e5a5267f3e30.png)

## 實驗結果
1. 確保每個回歸的相關係數是夠強的<br>
2. 確保每個回歸的斜率是夠顯著的<br>
3. 確保存在一種分配，使得演算法得以涵蓋宇集<br>
![image](https://user-images.githubusercontent.com/55400183/131257257-9c7d10be-f997-4473-a9e2-fda0edc756bf.png)
<br>對於不同變數(Df、Size Consideration)將在Decision Tree有相應之調整

## 操作工具
main.ipynb -- 輸入兩筆data後做出預測之Dk<br>
![image](https://user-images.githubusercontent.com/55400183/131245829-6cf7dcd7-b467-44c4-9376-bf17beda3e49.png)

## 額外的分析結果 -- 軸比的中心曲率運算 & Df Consideration
要怎麼在Df不是0時做出補償呢? 我們根據軸比數據做出一系列的運算，可以做出下部分之初步歸納:<br>
https://hackmd.io/IV7xLYAGRHOYziyKad6oJw?view&fbclid=IwAR1H63cE8HQOluJ0pFwEyhm8PfzyguvH_cjwIh5pYG_VHRrBCU8E9HpzaO4#%E5%8B%95%E6%A9%9F
<br>我們進一步做出更密集的運算結果，歸納出了同時預測Dk和Df的演算法:
<br>https://hackmd.io/tTJzYGnSTdulDGT5-8eknA?view
<br>![image](https://user-images.githubusercontent.com/55400183/131246226-60eda4d6-14b8-4320-ba14-f0f3f2c5b549.png)

## 額外的分析結果 -- Size Consideration
做出 Gain 與 Beamwidth之波動與起伏，將來收集更大量之數據以實現更廣泛的運算框架

