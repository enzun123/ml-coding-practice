# -*- codingg: utf-8 -*-
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.keys())  # data와 target만 사용

X, y = mnist.data, mnist.target
print(X)
print(X.shape)
print(y)
print(y.shape)

import matplotlib.pyplot as plt

def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, camp="binary")
    plt.axis("off")
    
some_digit = X[0]
plot_digit(some_digit)
plt.show()

print(y[0])         # 샘플 데이터 레이블 확인 (=5)

# 10x10 그림 생성
plt.figure(figsize=(9, 9))
for idx, image_data in enumerate(x[:100]):
    plt.subplot(10, 10, idx + 1)
    plot_digit(image_data)
plt.su