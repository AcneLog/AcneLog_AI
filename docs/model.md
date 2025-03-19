# 모델 개발

**3. 모델 학습 및 배포**

**(1) 모델 구조**

CNN(합성곱 신경망)을 기반으로 설계하며, ResNet이나 EfficientNet을 백본(Backbone)으로 사용 가능.

```
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model

base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = Flatten()(base_model.output)
x = Dense(128, activation='relu')(x)
x = Dense(3, activation='softmax')(x)  # 3개의 여드름 유형
model = Model(inputs=base_model.input, outputs=x)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

**(2) 학습 (Training)**

•	데이터셋을 학습 및 검증 데이터로 분리 (80:20)

•	조기 종료(Early Stopping) 및 모델 체크포인트 활용

•	GPU 가속 (CUDA 사용 가능)