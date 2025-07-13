from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import tensorflow as tf
import cv2

app = FastAPI()

# 🔹 클래스 이름 매핑 (필요시 수정 가능)
CLASS_NAMES = ["Normal", "Comedones", "Pustules", "Papules", "Folliculitis"]

# 🔹 TFLite Interpreter 로드
try:
    interpreter = tf.lite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()
except Exception as e:
    raise RuntimeError(f"Failed to load TFLite model: {e}")

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
INPUT_SHAPE = input_details[0]['shape'][1:3]  # (height, width)

def preprocess_image(image_bytes):
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Invalid image data or unsupported format")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, tuple(INPUT_SHAPE))
    img = img / 255.0  # Normalize to [0,1]
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img = preprocess_image(contents)

        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])[0]

        pred_class_idx = int(np.argmax(output_data))
        pred_class_name = CLASS_NAMES[pred_class_idx]
        confidence = float(np.max(output_data))

        return JSONResponse({
            "prediction_index": pred_class_idx,
            "prediction_label": pred_class_name,
            "confidence": confidence,
            "scores": output_data.tolist()
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")
    
'''
requirements: pip3 install -r requirements.txt
서버 실행 방법: uvicorn tflite_api_server:app --reload --host 0.0.0.0 --port 8000
'''