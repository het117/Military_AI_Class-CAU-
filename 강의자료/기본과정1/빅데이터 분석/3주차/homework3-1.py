import numpy as np 

players = [[170, 76.4], 
           [183, 86.2], 
           [181, 78.5], 
           [176, 80.1]] 

np_players = np.array(players) 

print('몸무게가 80 이상인 선수 정보');
print(np_players[ np_players[:, 1] >= 80.0 ])

print('키가 180 이상인 선수 정보');
print(np_players[ np_players[:, 0] >= 180.0 ])

# 4명의 선수의 키를 1열, 몸무게를 2열로 하는 players 리스트 생성
# playears 리스트를 넘파이 배열로 변환
# 전체 행 중 1열의 정보다 80 이상인 선수 정보 출력
# 전체 행 중 0열의 정보다 180 이상인 선수 정보 출력