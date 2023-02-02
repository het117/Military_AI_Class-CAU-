import numpy as np 
x = [i for i in range(100)]	# 0, 1, 2, 3, ... 99
y = [i ** 2 for i in range(100)]	# 0, 1, 4, 9, ... 99^2
z = [100 * np.sin(3.14 * i / 100) for i in range(100)]
result = np.corrcoef([x, y, z])
print(result)

# 0~99 x에 저장
# 0~99 제곱 값 y에 저장
# i가 0~99일때, sin 함수의 100배의 값 z에 저장
# 넘파이 corrcoef 함수를 활용하여 x, y, z의 상관관계를 출력