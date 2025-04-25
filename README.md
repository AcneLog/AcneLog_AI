# AcneLog_AI
Develop AI Model

**AI 모델 개발 (2025. 03. 19)**
- Kaggle에 기존재하는 데이터셋을 활용하며, 추가적으로 필요한 이미지는 저작권에 문제 없는 이미지를 수집한다.
- 화농성 여드름, 염증성 여드름, 좁쌀 여드름, 정상 여드름 등 총 4가지 타입으로 데이터를 라벨링한다.
- 수집한 이미지에서 노이즈 제거 및 필터링을 위해 OpenCV 라이브러리를 활용한다.
- 이미지 분류 및 분석을 위해 TensorFlow, PyTorch 라이브러리를 활용한다.
- ResNet과 EfficientNet라는 사전 학습된 모델을 활용하여 이미지 분류 작업 진행
- 웹서비스에서 이미지 분석 기능을 활용하기 위해 Tensorflow serving을 활용하여 API 형식으로 배포한다.
- 실제 모델은 CNN을 기반으로 ResNet과 EfficientNet을 백본으로 활용한다.