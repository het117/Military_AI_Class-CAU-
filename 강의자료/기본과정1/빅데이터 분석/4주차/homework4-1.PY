import numpy as np
import matplotlib.pyplot as plt
# numpy 및 matplotlib import

data1 = np.random.randn(100, 10) # 100개 데이터를 포함한 클래스 10개 랜덤데이터 생성

plt.boxplot(data1) # 10개 클래스별 박스 플랏 그레프 생성

plt.show() # 그래프 출력