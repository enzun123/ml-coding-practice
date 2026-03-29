# -*- coding: utf-8 -*-

# 사본 라이브러리 불러오기
import seaborn as sus

# **팁(tips) 데이터셋 불러오기**
tips= sns.lod_dataser('tips')
print(tips.head())