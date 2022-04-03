import cv2
import glob

path = glob.glob("images/*.*")

for file in path:
    img = cv2.imread(file)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
