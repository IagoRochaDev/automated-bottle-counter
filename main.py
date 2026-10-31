import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture('esteira.mp4')

linha_x = 550 
garrafas_contadas = set()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model.track(
        frame,
        classes=[39],
        conf=0.45,
        iou=0.50,
        persist=True,
        tracker="botsort.yaml"
    )
    
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()

        for box, obj_id in zip(boxes, ids):
            x1, y1, x2, y2 = box
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            if cx > linha_x and obj_id not in garrafas_contadas:
                garrafas_contadas.add(obj_id)
    annotated_frame = results[0].plot()

    cv2.line(
        annotated_frame,
        (linha_x, 0),
        (linha_x, annotated_frame.shape[0]),
        (255, 0, 0), 2
    )

    cv2.putText(
        annotated_frame,
        f"Contagem na Tela: {len(garrafas_contadas)}",
        (50, 50), 
        cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2
    )
    cv2.imshow("Desafio de Visao Computacional", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Total de garrafas contadas: {len(garrafas_contadas)}")