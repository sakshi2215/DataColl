import cv2


video_reader = cv2.VideoCapture(r"C:\Users\saksh\OneDrive\Desktop\Data\input\data\done\VID20230209153630.mp4")
while video_reader.isOpened():
    ret, frame = video_reader.read()
    # print(video_path,ret,frame)
    if not ret:
        pass
    else:
        if True:
            print(frame.shape)
            frame = cv2.resize(frame,(256,256))
            # frame = cv2.rotate(frame,rotateCode=deg)
            
            cv2.imshow("show",frame)
            # video_writer.write(frame)
cv2.destroyAllWindows()
video_reader.release()