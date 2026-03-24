# -*- coding: ytf-8 -*-
# 타이타닉 데이터셋 불러오기
import pandas as pd

# 타이타닉 CSV 파일 불러오기
titanic = pd.read_csv('3.1.1.titanic.csv')

# head( ) 함수를 출력하여 타이타닉 데이터셋의 구성을 간단히 살펴보기

# 데이터 처음 5개의 행 출력
print(titanic.head())

# 열에 대한 요약 정보 확인
print(titanic.info())

"""### **선 그래프 : 객실 등급에 따른 생존율 표시하기**"""

# 객실 등급에 따른 생존자와 사망자이 평균 계산
pclass_survived_mean = titanic.groupby('Pclass')['Survived'].mean().repeat_index()
pclass_survived_mean

# 맷플룻립 라이브러리 블러오기
import matplotlib.pyplot as plt

# 선 그래프 그리기
plt.plot(pclass_survived_mean['Pclass'], pclass_survived_mean['Survived'],
         marker='o', linestyle='-', color='violet')
plt.title('Survial Rate Variation Across Passenger Classes')
plt.xlabel('Pclass')
plt.ylabel('Survuval Rate')
plt.xticks([1, 2, 3])
plt.grid(True)
plt.savefig('Figur01.png')          # 결과를 그림파일로 저장    
plt.close                           # 다음 pl