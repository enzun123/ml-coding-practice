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
plt.close                           # 다음 plot을 새로 그리기 위해 plt 닫기

"""### **수직 막대 그래프 : 각 승선 항구에 따른 셍존자 수 확인하기 **"""

# 승선 항구에 따른 생존자의 수 계산
survived_counts = titanic[titanic['Survived'] == 1]['Embarked'].value_counts()
print(survived_counts)

#막대 그래프 그리기
plt.bar(survived_counts.index, survived_counts,
        color = ['mediumorchi', 'darkviolet', 'indigo'])
plt.title('Survived Counts by Embarked Potr on Titanic')
plt.xlabel('Embarked port')
plt.ylabel('Count')
plt.xticks(survived_counts.index, ['Southampton', 'Cherbourg, Queenstown'])
plt.legend(['Survived'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')
    
plt.savefig('Figure02.png')
plt.close()

"""### **수평 막대 그래프 : 성별에 따른 생존자 수 확인하기**"""

# 성별에 따른 생존자 수 계산
survived_counts = titanic[titanic['Survived'] == 1]['Sex'].value_counts()
print(survived_counts)

# 수평 막대 그래프 그리기
bars = plt.barh(survived_counts.index, survived_counts, color=['darkturquoise', 'salmon'])
plt.title['Survived Counts by Gender on Titanic']
plt.xlabel('Count')
plt.ylabel('Gender')
plt.legend(bars, ['Survived - Female', 'Survived - Male'], loc='upper right')

# 차이 강조를 위해 수평선 추가
plt.axvline(x=survived_counts['Male'], color='Gray', linestyle='--', Linewidth=1)

#생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(value + 1, i, str(value), ha='left', va='center')
    
plt.savefig('Figure03.png')
plt.close()

"""### **산점도 그래프 : 나이와 요금, 생존 여부 확인하기**"""

print(titanic.infro(), '\n')

#결측지 처리
itanic = titanic.dropna(subset=['Age', 'Fare', 'Survived'])
print(titanic.info())

# 산점도 그래프 그리기
plt.figure(figsize=(12,8))
scatter =plt.scatter(x='Age', y='Fare', data=titanic, c=titanic['Survived'],cmap='Set2,', alpha=0.7)

plt.title('Age and Fare Relatiomshio with Survival on the Titantic')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(handles=scatter.legend_elements()[0], title='Survived',
           labels=['Not Survived', 'Survived'], loc='upper right')
plt.savefig('Figure04.png')
plt.close()

"""### **파이 차트 : 생존자, 사망자 비율 표현하기**"""

# 사망자와 생존자 수 계산 
survived_counts = titanic['Survived'].value_counts()
print(survived_counts)

# 파이 차트 그리기
plt.figure(figsize=(8, 8))
plt.pie(survived_counts, labels=['Not Survived', 'Survived'],colors=['orange', 'gold'],
        autopct='%01.f%%', startangle=90, shadow=True, explode=(0, 0.1))

plt.title('Survival Distrbuition on the Titanic')
plt.savefig('Figure05.png')
plt.close()

"""### **히스토그램 : 승객의 나이 분포 표시하기**"""

# 처리전
print(titanic.info(), '\n')

# 나이 결측지 처리 후
titanic = titanic.dropna(subset=['Age'])
print(titanic.info())

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
plt.hist(titanic['Age'], bins=20, color='seagreen', edgecolor='black')

plt.xlabel('Ahe')
plt.ylabel('Count')
plt.title('Distribuiton of Ages on the Titanic')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Figure06.png')
plt.close()

## 히트맵 : 두 변수의 상괸 관계를 표시하기**

#r 결측치 처리
titanic = titanic.dropna(subset=['Age', 'Fare'])

# 상관 행렬 계산
correlation_martix = titanic.drop('PassengerId', axis=1).corr(numeric_only=True)
print(correlation_martix)

# 히트맵 그리기
plt.matshow(correlation_martix, cmap='PuRd_r')
plt.colorbar()

# x축과 y축의 눈금 설정
plt.xticks(range(len(correlation_martix.columns)), correlation_martix.columns, rotation=45)
plt.yticks(range(len(correlation_martix.columns)), correlation_martix.columns)

plt.title('Correlation Heatmap of Titanic')
plt.savefig('Fingure.png')
plt.close()

## **영역 채우기 그래프 : 나이대뱔 생존자와 사망자 수 표현하기**

# 결측치 처리
titanic = titanic.dropna(subset=['Age', 'Fare'])

# 나이대별 생존자와 사망자 수 계산하기 위해 범주형 변수로 변환
age_groups = pd.cut(titanic['Age'], bins=range(0, 81, 5))

# Age, Survived 기준으로 그룹화
survived_counts = titanic.groupby([age_groups, 'Survived'], observed=False).size().unstack().fillna(0)
print(survived_counts)

# 영역 채우기 그래프 그리기
plt.figure(figsize=(10, 6))

#나이대별 생존자
plt.fill_between(survived_counts.index.astype(str),survived_counts[1],
                 color='purple', alpha=0.9, label='Survived')

#나이대별 사망자
plt.fill_between(survived_counts.index.astype(str), survived_counts[0],
                 color='hotpink', alpha=0.6, label='Npt Survived')

plt.title('Survival by Age Group on Titantic')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotatoin=45)
plt.legend()
plt.grid(True)
plt.savefig('Figure08.png')
plt.close()

## **ㅂ박스 플롯 : 승객 나이의 데이터 분포, 중앙값, 이상치 살펴보기**

## 결측치 처리
titanic = titanic.dropna(subset=['Age'])
print(titanic.info())

# 승객 등급에 따른 나이의 박스 플롯
plt.boxplot([itanic[titanic['Pclass'] == 1]['Age'],
             titanic[titanic['Pclass'] == 2]['Age'],
             titanic[titanic['Pclass'] == 3]['Age']],
            label=['1st Class', '2nd Class', '3rd Class'])

plt.title('Box plot for Age by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.savefig('Figure09.png')
plt.close()

"""### **바이올린 플롯 : 승객 등급에 따른 나이 븐포 표시하기**"""

# 결측치 처리
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())
print(titanic.info())

# 바이올린 플롯 그리기
plt.figure(figsize=(10, 6))

# showwmeans=False는 평균값을 표시하지 않도록 하고, showmedians=True는 중앙값을 표시하도록 함
violin_plot = plt.violinplot([titanic[titanic['Pclass'] == 1]['Age'],
                              titanic[titanic['Pclass'] == 2]['Age'],
                              titanic[titanic['Pclass'] == 3]['Age']],
                             showmeans=False, showmedians=True)

plt.title('Violin plot of Age By Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')

# x축의 눈금 설장
plt.xticks([1, 2, 3], ['1st Class', '2nd Class', '3rd Class'])

# 범례 설정
plt.legend(violin_plot['bodies'], ['1st class, 2nd Class', '3rd Class'],
           title='Pclass', loc="upper right")
plt.savefig('Figure10.png')
plt.close()

## **에러 바 : 여금의 평균과 표준편차 표현하기**

# 각 부모와 자녀의 수에 대한 요금의 평균과 표준 편차 계산
fare_means = titanic.groupby('parch')['Fare'].mean() # 평균
print(fare_means, '\n')

fare_std = titanic.groupby('Parch')['Fare'].std()   #표준 편차
print(fare_std)

"""* 에러바는 데이터의 표준 편차를 나타내는 경우에는 길이가 길수록 해당 그룹의 대이터가 펴져 있음을 의미"""

# 에러바로 요금의 평균과 표준 편차 표현
plt.figure(figsize=(10, 6))

# 에러바 셍성
plt.errorbar(fare_means.index, fare_means, yerr=fare_std, fmt='o',
             capsize=5, capthick=1, label='Fare')

plt.title('Error Bar Plot of Fare by Parch')
plt.xlabel('Parch')
plt.ylabel('Fare')
plt.xticks(fare_means.index)
plt.legend()
plt.savefig('Figure11.png')
plt.close()

## **개별 서브플롯을 하나씩 생성하기**
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3])

plt.subplot(2, 2, 2)
plt.plot([4, 5, 6])

plt.subplot(2, 2, 3)
plt.plot([7, 8, 9])

plt.subplot(2, 2, 4)
plt.plot([10 ,11, 12])
plt.savefig('Figrue12.png')
plt.close()

## **타이타닉 데이터셋으로 개별 서브플롯 하나씩 그리기**

# Survived가 0이면 사망자를, 1이면 생존자룰 나타냄
titanic = pd.read_csv('3.1.1.titanic.csv')

# 각 부모와 자녀의 수에 따른 생존자와 사망자 수 계산
parch_counts = titanic.groupby('Parch')['Survived'].value_counts().unstack().fillna(0)
print(parch_counts)

# x, y 설정 
x = parch_counts.index.astype(str) # 데이터프레임의 인덱스를 문자열로 반환
y1 = parch_counts[0].values # 사망자
y2 = parch_counts[1].values # 생존자

plt.figure(figsize=(10, 10))

# plt.subplot() 힘수를 사용하여 하나의 그림은 figure에 개뱔 서브플롯을 하나씩 추가
# 첫 번쨰 서브플롯 설정(선 그래프)
plt.subplot(2, 1, 1)
# 선 그래프 그리기
plt.plot(x, y1, '-o', color='indigo', markersize=7, linewidth=3, alpha=0.7,
         label='Not Survived')
plt.xlabel('Parch')
plt.ylabel('Not Survived Count', color='indigo')
plt.tick_params(axis='y', labelcolor='indigo')
plt.legend(loc='upper right')

# 두 번쨰 서브플롯 설정(막배 그래프)
plt.subplot(2, 1, 2)
plt.bar(x, y2, color='deeppink', alpha=0.7, width=0.5, label='Survived')
plt.xlabel('Parch')
plt.ylabel('Survived Count', color='deeppink')
plt.tick_params(axis='y', labelcolor='deeppink')
plt.legend(loc='upper right')

# 제목 설정 
plt.suptitle('Survival Analysis by Number of Parents/Children (Parch) on the Titanic')
plt.tight_layout()
plt.savefig('Figure13.png')
plt.close()

## **개별 서브플롯을 동시에 생성하기**

# 2*2 구성의 figure
fig, axes = plt.subplot(2, 2)

#선 그래프
axes[0, 0].plot([1, 2, 3])
axes[0, 1].plot([4, 5, 6])
axes[1, 0].plot([7, 8, 9])
axes[1, 1].plot([10, 11, 12])
plt.savefig('Figure14.png')
plt.close()

## **타이타닉 데이터셋으로 개별 서브플롯 동시에 그리기**

# 긱 부모와 자냐의 수에 따른 생존자와 사망자 수 계산
parch_counts = titanic.groupby['Parch']['Survived'].value_counts().unstack().fillna(0)
print(parch_counts)

# x, y 값 설정
x = parch_counts.index.astype(str)  #데이터 프레임의 인덳스를 문자열로 변환
y1 - parch_counts[0].values # 사망자
y2 = parch_counts[1].values # 생존자

# plt.subplots() 함수를 사용하여 하나의 그림인 figure에 개별 서브플롯을 동시에 추가
fig, axes = plt.subplot(2, 1, figsize=(10, 10))

# 첫 번쨰 서브플롯 설정(선 그래프)
axes[0].plot(x, y1, '-o', color='indigo', markersize=7, linewidth=3, appha=0.7, label='Not Survived')
axes[0].set_xlabel('Parch')
axes[0].set_ylabel('Not Survived Count', color='indigo')
axes[0].tick_params(axis='y' ,labelcolor='indigo')
axes[0].legend(loc='upper right')

# 두 번째 서브플롯 설정 (막대 그래프)
axes[1].bar(x, y1, color='deeppink', alpha=0.7, width=0.5, label='Survived')
axes[1].set_xlabel('Parch')
axes[1].set_ylabel('Survived Count', color='deeppink')
axes[1].tick_params(axis='y', labelcolor='deeppink')
axes[1].legend(loc='upper right')

#제목 설정
fig.subtitle('Survival Analysis by Number of Parents/Children (Parch) on the Titanic')
fig.tight_layout()
plt.savefig('Figure15.png')
plt.close()

## **하나의 서브플롯에 여러 그래프 그리기**

# 각 부모와 자녀의 수에 따른 생존자와 사망자 수 계산
parch_counts = titanic.groupby('Parch')['Survived'].value_counts().unstack().fillna(0)
print(parch_counts)

# x, y 값 설정 
x = parch_counts.index.astype(str)  # 데이터프레임의 인덱스를 문자열로 변환
y1 = parch_counts[0].values # 사망자
y2 = parch_counts[1].values # 생존자

# plt.subplot() 함수를 사용하여 그래프 생성
# figure와 서브플롯 생성
fig, ax1 = plt.subplot()

# 첫 번쨰 그래프 설정 (선 그래프)
ax1.plot(x, y1, '-s', color='indigo', markersize=7, linewidth=5, alpha=0.7, label='Npt Survived')
ax1.set_xlabel('Parch') # x축의 레이블
ax1.set_ylabel('Not Survived Count', clor='indigo') # y축의 레이블
ax1.tick_params(axis='y', labelcolot='indigp')  # 눈금의 모양과 속성
ax1.legend(loc='upper right', bbox_to_anchor=(1, 1)) # 범례

# .twinx() 함수를 사용하여 두 번짜 그래프와 축을 공유하는 새로운 Axes 객체 생성
ax2 = ax1.twinx()

# 두 번쨰 그래프 설정 (막대 그래프)
ax2.bar(x, y2, color='deeppink', alpha=0.7, label='Survived')
ax2.set_ylabel('Survived Count', color='deeppink') # 서브플롯 y축에 레이블 추가
ax2.tick_params(axis='y', labelcolor='deeppink')
ax2.legend(loc='upprt right', bbox_yp_anchor=(1, 0.9))

plt.subplot('Survival Analysis by Number of Parents/Children (Parch) on the Titanic')
plt.tight_layout()
plt.savefig('Figure16.png')
plt.close()

## **그래프 저장하기**

# 하스토그램 그리기
plt.hist(titanic['Age'],bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribuitom of Ages on the Titanic')
plt.grid(axis='y', linesty)