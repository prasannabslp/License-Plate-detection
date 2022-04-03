import cv2

vidcap = cv2.VideoCapture('video.MOV')
success, image = vidcap.read()
count = 1
while success:
    #cv2.imwrite("images/image_%d.jpg" % count, image)
    success, image = vidcap.read()
    print('Saved image ', count)
    count += 1
