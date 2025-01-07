import cv2
import GUI
import HAL
import utm
import math
# Enter sequential code!
# Enter sequential code!
victim_lat = 40+16/60+47.23/3600
boat_lat = 40+16/60+48.2/3600

boat_long = 3+49/60+3.5/3600
victim_long = 3+49/60+1.78/3600

coord_utm_boat = utm.from_latlon(boat_lat,boat_long)
coord_utm_victim = utm.from_latlon(victim_lat,victim_long)

dist_y = coord_utm_victim[1] - coord_utm_boat[1]
dist_x = coord_utm_boat[0] - coord_utm_victim[0]

print(dist_x)
print(dist_y)

z = 2
az = 0.2
HAL.takeoff(z)
coord = HAL.get_position()
print(coord)

# Drone's takeoff altitude

tolerance = 0.1

#while coord[0] != dist_x and coord[1] != dist_y:
    # Enter iterative code!

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while abs(coord[0] - dist_x) > tolerance and abs(coord[1] - dist_y) > tolerance:


    HAL.set_cmd_pos(dist_x, dist_y, z, az)
    coord = HAL.get_position()


    image = HAL.get_frontal_image()
    GUI.showImage(image)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        print(f"Detected {len(faces)} face(s).")
        for (x, y, w, h) in faces:
            # Highlight the face in the image
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        GUI.showImage(image)

        # Mark face as safe
        print("Initiating rescue action...")

        HAL.hover() 
        HAL.drop_rescue_kit() 

        break

while True:
    pass
