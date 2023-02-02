from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 

iris = load_iris() # 사이킷런 아이리스 데이터 셋 로드
X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target,
                                                test_size=0.2)
# data와 label을 train, test 데이터 8:2로 분리

from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

for i in [1, 3, 5, 10, 20, 30]: # 반복문을 통해 파라미터별 결과 출력
    num_neigh = i
    knn = KNeighborsClassifier(n_neighbors = num_neigh) # 분류기 생성
    knn.fit(X_train, y_train) # knn 모델 학습
    y_pred = knn.predict(X_test) # test 데이터 예측
    scores = metrics.accuracy_score(y_test, y_pred) # test data 정확도 저장
    print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores)) # 결과 출력