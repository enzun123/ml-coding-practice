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
            getPostData(post, jsonResult, cnt)              # 
