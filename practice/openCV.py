# 13장 심화문제 1번
import cv2

img1 = cv2.imread('c:/workplace/myData.png')
img2 = cv2.imread('c:/workplace/bag_cartoon.png')
img1 = cv2.resize(img1, (300, 400))
img2 = cv2.resize(img2, (300, 400))

img_merged = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
"""
cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None) -> dst
- src1: (입력) 첫 번째 영상
- alpha: 첫 번째 영상 가중치
- src2: 두 번째 영상. src1과 같은 크기 & 같은 타입
- beta: 두 번째 영상 가중치
- gamma: 결과 영상에 추가적으로 더할 값
- dst: 가중치 합 결과 영상
- dtype: 출력 영상(dst)의 타입
"""
cv2.imshow('merged', img_merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
