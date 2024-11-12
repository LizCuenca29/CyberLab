import GUI
import HAL

import cv2
# Enter sequential code!

kd = 0.001
kp = 0.004
ki = 0.00001
i = 0
integral = 0
previous_error = 0

while True:
    # Enter iterative code!
    img = HAL.getImage()
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv,(0,125,125),(30,255,255))
    
    contours, hierarchy = cv2.findContours (red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    M = cv2.moments(contours[0])
    
    if M["m00"] != 0:
        cX = M["m10"]/ M["m00"]
        cY = M["m01"]/ M["m00"]
    else:
      
      cX,cY= 0, 0
      
    if cX>0:
      err = 320 - cX
      difference= previous_error - err
    
      HAL.setV(4)
      HAL.setW(0.005 * err + kd * difference + ki * integral )
      
    
    GUI.showImage(red_mask)
    print('%d cX: %.2f cY: %.2f' % (i, cX,cY))
    i = i +1
    integral += err
    previous_error = err