import cv2

# Đọc ảnh và chuyển sang grayscale
image = cv2.imread("/Users/vudn-mac/Documents/opencv-project/istockphoto-1404216298-612x612 (1).jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

ret , threshold_image = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = cv2.drawContours(gray_image, contours, -1, (0, 255, 0), 2)

new_contour = [con for con in contours if cv2.contourArea(con) > 100]

print(f"So luong vien thuoc la {len(contours)}")
print(f"So luong vien thuoc sau khi loc la {len(new_contour)}")

cv2.imshow("anh goc", image)
cv2.imshow("threshold image", threshold_image)
cv2.imshow("contour image", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()