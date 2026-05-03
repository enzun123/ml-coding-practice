# -*- coding: utf-8 -*-
# 넷플릭스 데이터 분석 프로젝트

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 새션 저장소에 업로드한 csv 파일을 읽어 변수에 할당
netflix = pd.read_csv('netflux_titles.csv')
netflix.head()

# .columns : 열 이름 확인
list(netflix.columns)

# .head(3) : 데이터 처음 3개의 행 출력
netflix.head(3)

# .info() : 열에 대한 요약 정보 확인
netflix.info()

# 넷플릭스 결측치 비율 확인하기
for i in netflix.columns :
    missingValueRate = netflix[i].isna().sum() / len(netflix) * 100
    if missingValueRate > 0 :
        print("{} null rate: {}%".format(i,round(missingValueRate, 2)))
        
# .fillna( ) : 결측치를 다른 값으로 대체하여 처리
# 결측치 비율 : country(9.44%)
netflix['country'] = netflix('country').fillna('No Data')

# .replace(np.man, 'b') : 결측치를 문자열 바꾸기 함수를 통해 처리
# 결측치 비율 : director(29.91%), cast(9.37%)
netflix['director'] = netflix['director'].replace(np.nan, 'No Data')
netflix['cast'] = netflix['cast'].replace(np.nan, 'No Data')

# .dropna(axis = 0) : 결측치가 있는 행 전체 제거
# 원복 객체를 수정하려au