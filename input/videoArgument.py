import cv2
from glob import glob
import os, sys
import uuid
import random



path = "C:\\Users\\saksh\\OneDrive\\Desktop\\Data\\input"


main_folder_path=""
output_folder_path=""
no_of_clips_to_augment_per_frame=0
video_clip_names=[]
fourcc = 'mp4v'  # output video codec
# video_writer = cv2.VideoWriter(path_of_video_to_save, cv2.VideoWriter_fourcc(*fourcc),fps,(w,h))

def videoArgument(root:str,video_path:str):
    video_reader = cv2.VideoCapture(video_path)
    fps = int(video_reader.get(cv2.CAP_PROP_FPS))
    deg = random.randint(0,10)
    rand_path = path+f"{root}\\{str(uuid.uuid4())}.mp4"[1:].replace("/","\\")
    print(rand_path)
    w = 256
    h = 256
    video_writer = cv2.VideoWriter(rand_path, cv2.VideoWriter_fourcc(*fourcc),fps,(w,h))
    try:
        while video_reader.isOpened():
            ret, frame = video_reader.read()
            print(video_path,ret,frame)
            if not ret:
                pass
            else:
                if frame != None:
                    frame = cv2.resize(frame,(256,256))
                    frame = cv2.rotate(frame,rotateCode=deg)
                    cv2.imshow("show",frame)
                    video_writer.write(frame)
    except Exception as e:
        print(e)
    try:
        cv2.destroyAllWindows()
    except:
        pass
    video_reader.release()
    video_writer.release()
count = 0
for dirs,_,files in os.walk("./data/"):
    if count == 2:
        break
    for file in files:
        for _ in range(5):
            print(path+f"{dirs}\\{file}"[1:].replace("/","\\"))
            videoArgument(dirs,path+f"{dirs}\\{file}"[1:].replace("/","\\"))
            break
        break
    count += 1   
    




