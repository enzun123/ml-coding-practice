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
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getTourismStatsService(yyyymm, nat_cd, ed_cd)        #[CODE 2]
            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                #데이터기 없는 마지막 항목인 경우 ----------------------------
                if jsonData['response']['body']['items'] == '':
                    dataEND = "{0}{1:0>2}".format(str(year), str(month-1))
                    print("데이터없음... \n제공되는 통계 데이터는 %s년 %s 월까지 입니다." % (str(year), str(month-1)))
                    break
                #jsonData를 출력하여 확인............................................
                print(json.dumps(jsonData, indent = 4, sort_keys = True, ensure_ascii = False))
                
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                print('[ %s_%s : %s ]' % (natName, yyyymm, num))
                print('------------------------------------------------------')
                jsonResult.append({'nat_name': natName, 'nat_cd': nat_cd, 'yyyymm': yyyymm, 'visit_cnt': num})
                result.append([natName, nat_cd, yyyymm, num])
                
    return (jsonResult, result, natName, ed)

"""### [CODE 2]"""

def getTourismStatsItem(yyyymm, nat_cd, en_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters =  "?_type=json&serviceKey=" + ServiceKey        #인증키
    parameters += "&YM=" + yyyymm 
    parameters += "&NAT_CD=" + nat_cd
    parameters += "ED_CD="