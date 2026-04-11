# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "1e274d34339735d4a3485ee5aed58c21abf015f79b9b6e5cfe05b84001007baa"

"""### [CODE 0]"""

def main():
    jsonResult = []
    result = []
    
    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) :')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E"
    
    jsonResult, result, natName, dateEND = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)  #[CODE 3]
     
    #파일저장 : csv 파일
    columns = ["입극자국가", "국가코드", "입국연월", "입국자 수"]
    result_df = pd.DataFrame(result, columns = columns)
    result_df.to_csv('./%s_%s_%s_%s.csv' % (natName, ed_cd, nStartYear, dataEND), index = False, encoding = 'cp949')
    
"""### [CODE 3]"""

def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []
    
    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = "{}"