import numpy as np 
from sklearn import linear_model 
 
regr = linear_model.LinearRegression() # 선형회귀 모델 분류기 생성
# 남자는 0, 여자는 1
X = [[164, 1], [167, 1], [165, 0], [170, 0], [179, 0], [163, 1], [159, 0], [166, 1]] # 키, 성별 데이터 정의
y = [43, 48, 47, 66, 67, 50, 52, 44] # 몸무게 데이터 정의
regr.fit(X, y)         # 학습 
print('계수 :', regr.coef_ ) # 모델 계수 출력
print('절편 :', regr.intercept_) # 모델 절편 출력
print('점수 :', regr.score(X, y)) # X, y 데이터에 대한 모델 점수 출력
print('은지와 동민이의 추정 몸무게 :', regr.predict([[166, 1], [166, 0]]))
# 새로운 데이터에 대한 추정 결과 출력