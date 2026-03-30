# -*- coding: utf-8 -*-

# 데이터 준비
from pathlib import Path
import numpy as np
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarbsall_path = path("datasets/housio")