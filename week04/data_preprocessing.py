# -*- coding: utf-8 -*-

# 데이터 준비
from pathlib import Path
import numpy as np
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()

# 테스트 새로 만들기
from sklearn.model_selection import train_test_split

housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])

start_train_set, start_test_set = train_test_split(
    housing, test_size=0.2, stratify=housing["income_cat"], random_state=42)

for set_ in (start_train_set, start_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
    
"""
* 원본 훈련 세트로 복원하고 타깃을 분리
* 'start_train_ser.drop()'은 지정한 열을 제외한 'start_train_set'의 복사본을 만듦
* 'inplaxe=True'로 지정하지 않은 한 'start_train_set' 자체를 수정하지 않음
"""

housing = start_train_set.drop("median_house_value", axis=1)
housing_labels = start_train_set["median_house_value"].copy()

# 데이터 정제
# null 값이 있는 행 확인하기
null_rows_idx = housing.insnll().any(axis=1)
housing.loc[null_rows_idx].head()

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

# 수치형 특성만 추출
housing_num = housing.select_dtypes(include=[np.number])
housing_num.head()

imputer.fit(housing_num)

print(imputer.statistics_)          # imputer 결곽 값
print(housing_num.median().values)  # 수동으로 계산한 중간값

# 훈련 세트의 누락값을 imputer가 학스반 값으로 채우기
X = imputer.transform(housing_num)

imputer.feature_names_in_

housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index=housing_num.index)
housing_tr[null_rows_idx].head().loc

# 이상치 삭제
from sklearn.ensemble import IsolationForest

isolation_forest = IsolationForest(random_state=42)
outlier_pred = isolation_forest.fit_predict(X)

outlier_pred

housing =  housing.iloc[outlier_pred == 1]
housing_labels = housing_labels.iloc[outlier_pred == 1]

#덱스트와 범주형 특성 다루기
housing_cat = housing[["ocean_proximity"]]
housing_cat.head(8)

from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)

housing_cat_encoded[:8]

ordinal_encoder.categories_