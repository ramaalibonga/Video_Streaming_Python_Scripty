import cv2

#intantiation of VideoCapture object
vid  = cv2.VideoCapture(0)
vid.set(3,200)
vid.set(2,200)

# video width && height
video_width = int(vid.get(3))
video_height = int(vid.get(4))


video_size = (video_width,video_height)

#write video to the mp4 format

save_video = cv2.VideoWriter('stream_01.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10,video_size)

while(vid.isOpened()):
     ret,frame = vid.read()
     if ret : 
        save_video.write(frame)
        cv2.imshow("frame",frame)

      #press q button to quit.
     if cv2.waitKey(1) & 0xFF == ord('q'):
          break
  
save_video.release()
vid.release()
cv2.destroyAllWindows()


