import math
import matplotlib.pyplot as plt
# math 및 matplotlib import

x = []
y = []
z = []
# 빈 리스트 x, y, z 초기화

for angle in range(360):
    x.append(angle) # x 리스트에 0 ~ 359 값 추가
    z.append(math.cos(math.radians(angle))) # z 리스트에 0 ~ 359 cos 값 추가
    y.append(math.sin(math.radians(angle))) # y 리스트에 0 ~ 359 sin 값 추가

plt.plot(x, y) # x, y 좌표 데이터 생성
plt.plot(x, z, 'r-') # x, z 좌표 데이터 생성 후 red 색상 지정
plt.title("SINE & COSINE WAVE") # 그래프 타이틀 SINE & COSINE WAVE 지정
plt.show() # 그래프 출력