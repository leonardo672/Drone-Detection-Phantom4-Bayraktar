import cv2
import torch
from pathlib import Path

class VideoAnalyzer:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

    def detect_and_save_objects(self, input_path, output_folder="data/Our_DataBase", new_width=640, new_height=480):
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        cap = cv2.VideoCapture(str(input_path))
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (new_width, new_height))
            results = self.model(frame)
            detected_objects = results.xyxy[0]

            for obj in detected_objects:
                x1, y1, x2, y2, conf, cls = obj
                obj_img = frame[int(y1):int(y2), int(x1):int(x2)]
                if obj_img.size > 0:
                    filename = output_folder / f"object_{int(x1)}_{int(y1)}.jpg"
                    cv2.imwrite(str(filename), obj_img)

        cap.release()
        cv2.destroyAllWindows()
