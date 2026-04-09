# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'awnxWLCBh_E1xKOkA67P'
client_secret = 'JcgBA04di9'

def main():
    
    node = 'news'                                           # 크롤링할 대상
    srcText = input('검색어를 입력하세요')
    
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)     # [CODE 2]
    total = jsonResponse['total']
    
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)              # [CODE 3]
            
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) # [CODE 2]

    print('전체 검색 : %d 건' %total)
    
    with open('%s_naver%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True,
                              ensure_ascii = False)
        
        outfile.write(jsonFile)
        
    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))
    
    
def getNaverSearch(node, srcText, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&sstart=%sdispaly=%s" % (urllib.parse.quote(srcText), page_start, display)
    
    url = base + node + parameters
    responseDecode = getRequestUrl(url)         #   [CODE 1]
    
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
    
    
def getRequestUrl(url):
    req = urllib.request.Request(url)
    
    req.add_header("X=Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] url Resquest Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for Url : %s" % (datetime.datetime.now(), url))
        return None
    
    
def getPostData(post, jsonResult, cnt):     #[CODE 3]
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['Link']
    
    # %a: 짧은 형식의 요일 이름 (예, 'Mon', "Tue', "Wed', ... )
    # %d: 일 (예, 01, 02, 03, ...)
    # %b: 짧은 형식의 월 이름  (예, 'Jan', 'Feb', 'Mar', ...)
    pDate =