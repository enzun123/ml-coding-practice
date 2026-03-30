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
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url=, tarbsall_path)
        with tarfile.open(tarbsall_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()

#