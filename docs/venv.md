# 모델 테스트를 위한 가상환경 설정

venv로 접근해서 uvicorn + FastAPI 서버 환경을 설정하는 방법을 단계별로 정리한다.

⸻

✅ 1️⃣ venv 생성

프로젝트 폴더 (예: AcneLog_AI)에서:

python3 -m venv venv

	•	여기서 venv라는 이름의 폴더가 생성됨.

⸻

✅ 2️⃣ venv 활성화

macOS / Linux 기준:

source venv/bin/activate

활성화되면 터미널 prompt에 (venv) 표시가 보임

⸻

✅ 3️⃣ venv 안에서 필요한 패키지 설치

venv 안에서만 아래 설치 진행:

pip install fastapi uvicorn tensorflow pillow opencv-python

필요하다면 jupyter까지 설치:

pip install jupyter


⸻

✅ 4️⃣ uvicorn 실행

이제 venv 안이기 때문에 uvicorn 명령어도 바로 인식될 것:

uvicorn tflite_api_server:app --reload --host 0.0.0.0 --port 8000


⸻

🔔 추가 팁: Python 모듈 방식 실행

만약 그래도 PATH 문제 있다면 venv 활성화 후 아래 방식으로 실행 가능:

python -m uvicorn tflite_api_server:app --reload --host 0.0.0.0 --port 8000


⸻

✅ 5️⃣ 종료 방법
	•	서버 종료:

Ctrl + C


	•	venv 비활성화:

deactivate



⸻

💡 정리

# 한 번만:
python3 -m venv venv

# 사용할 때마다:
source venv/bin/activate
pip install fastapi uvicorn tensorflow pillow opencv-python

uvicorn tflite_api_server:app --reload --host 0.0.0.0 --port 8000


⸻