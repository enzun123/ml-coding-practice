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
        urllib