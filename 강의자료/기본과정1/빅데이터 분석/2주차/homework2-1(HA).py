import pandas as pd

table1 ={
    '이름':['철수', '영희', '은정', '윤아', '은희'],
    '키':[187, 165, 170, 172, 160],
    '나이':[40, 32, 33, 27, 29]
}

table2 ={
    '이름':['철수', '영희', '은정', '윤아', '은희'],
    '사는 곳':['강북구', '동작구', '수원', '인천', '종로구']
}

tf1=pd.DataFrame(table1)
tf2=pd.DataFrame(table2)

result = pd.concat([tf1, tf2], axis=1)

print(result)