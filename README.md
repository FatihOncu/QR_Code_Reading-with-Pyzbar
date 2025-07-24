\# QR Code Reader with Pyzbar



- This project is a real-time QR code scanner built with Python. It uses your webcam to detect and decode QR codes in live video.



\# Libraries Used


 - OpenCV: For opening the webcam, enhancing image contrast and brightness, and preprocessing the frame.

 - Pyzbar: For detecting and decoding QR codes from the image.



\# How It Works



1\. OpenCV captures the video stream from your webcam.

2\. The image is converted to grayscale and enhanced using contrast and tone adjustments.

3\. Pyzbar scans the processed image to detect and decode any QR code present.

4\. Each step is clearly explained with comments in the code.



\# Performance



- Depending on the size of the QR code and the quality of the camera, the system can successfully read codes from relatively long distances.



\# How to Run



- Install the required libraries:



```bash

pip install opencv-python pyzbar



