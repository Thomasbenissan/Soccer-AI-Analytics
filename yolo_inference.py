from unittest import result
from ultralytics import YOLO

model = YOLO('yolov8l') #model size

results = model.predict('input_videos/bundesliga.mp4', save=True)


print(results[0])
print('===============================================')
for box in results[0].boxes:
    print(box)