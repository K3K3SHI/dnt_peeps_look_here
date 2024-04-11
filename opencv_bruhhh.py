import cv2
import numpy as np

def Task1():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

# Convert the image to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Set the hue value to make the image appear orange
    hsv_frame[:, :, 0] = 15  # Orange hue value

# Convert the HSV image back to BGR color space
    orange_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)

# Display the original and orange-tinted images
    cv2.imshow('Original Image', frame)
    cv2.imshow('Orange Image', orange_frame)

    cv2.waitKey(0)
    cap.release()

def Task2():
    # Open the video file
    cap = cv2.VideoCapture(0)

# Get the frame rate of the original video
    fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object with reduced frame rate
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps / 2, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

    # Write the frame to the output video
        out.write(frame)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

option = int(input("1 or 2"))

if option == 1:
    Task1()
else:
    Task2()
