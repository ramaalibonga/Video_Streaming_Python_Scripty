import cv2

#initialization of  cv2 object
vid  = cv2.VideoCapture(0)
vid.set(3,200)
vid.set(2,200)

# set video width & height
video_width = int(vid.get(3))
video_height = int(vid.get(4))


video_size = (video_width,video_height)

#write video in mp4 format

save_video = cv2.VideoWriter('stream_01.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10,video_size)

while(vid.isOpened()):
     ret,frame = vid.read()
     if ret : 
        save_video.write(frame)
        cv2.imshow("frame",frame)

      #press q button to quit.
     if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# save video
save_video.release()
vid.release()
cv2.destroyAllWindows()


