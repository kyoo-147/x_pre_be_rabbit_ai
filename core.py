import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load mô hình từ file h5
classifier = load_model('ASLModel.h5')

# Định nghĩa khung ROI
roiLeftTop = (330, 100)
roiRightBottom = (450, 300)

# Hàm nhận diện bàn tay và vẽ khung ROI
def hand_detection(frame):
    # Chuyển đổi frame sang không gian màu HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Xác định phạm vi màu của bàn tay trong không gian màu HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Tìm các điểm ảnh thuộc về màu da
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Tìm contours trong mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Xác định bounding box của bàn tay
    bounding_box = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Chọn ngưỡng diện tích tùy thuộc vào kích thước của ảnh
            x, y, w, h = cv2.boundingRect(contour)
            bounding_box = [(x, y), (x + w, y + h)]
            break

    return bounding_box

# Mở camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()
    if not ret:
        break

    # Xử lý frame để có được bounding box bàn tay
    bbox = hand_detection(frame)

    # Vẽ khung ROI
    cv2.rectangle(frame, roiLeftTop, roiRightBottom, (0, 255, 0), 2)

    # Hiển thị bounding box bàn tay nếu có
    if bbox:
        cv2.rectangle(frame, bbox[0], bbox[1], (0, 255, 0), 2)
        
    cv2.imshow('Hand Detection', cv2.resize(frame, (840, 680)))

    # Hiển thị frame
    # cv2.imshow('Hand Detection', frame)

    # Thoát khỏi vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
