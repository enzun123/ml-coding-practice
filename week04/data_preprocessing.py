# -*- coding: utf-8 -*-

# 데이터 준비
from pathlib import Path
import numpy as np
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarbsall_path = Path("datasets/housing.thgz")
    if not tarbsall_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarbsall_path)
        with tarfile.open(tarbsall_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()

# 테스트 새로 만들기
from sklearn.model_selection import train_test_split

housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])

start_train_set, start_test_set = train_test_split(
    housing, test_size=0.2, stratify=housing['income_cat'], random_state=42)

for set_ in (start_train_set, start_train_set):
    set_.drop("income_cat", axis=1, inplace=True)
    
"""
* 원본 훈련 세트로 복원하고 타깃을 분리
* 'start_'"""