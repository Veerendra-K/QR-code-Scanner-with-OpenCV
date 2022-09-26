# Webcam QR code scanner using OpenCV

![Image github](https://myoctocat.com/assets/images/base-octocat.svg)
![This is an QR code for My Github Account](https://github.com/Veerendra-K/QR-code-Scanner-with-OpenCV/blob/main/Github-QR.png) 
> This is an QR code **link** for My Github Account Scan n **Do Support!**

#

<strong> Firstly you need to open your webcam, and you’ve to run your python program to make it ready to scan the QR code. You can take the Qr code picture on your mobile and show the picture in front of your webcam. It correctly identifies the QR code that presents on your screen. And this program redirects you to a link hidden in the QR code.</strong>

# Requirements:
              pip install OpenCV
              pip install webbrowser ( built in )
----------------------------------------------------------------------------------------------------
- <strong> Step 1: </strong>
```
    For creating the QR code scanner you need to install the OpenCV library on your command prompt.
    First, you need to import the cv2 and browser library.
    Cv2 is used for scanning the QR code through a webcam and a web browser is used to take the URL into the browser. 
```

- <strong> Step 2: </strong>
``` 
    Next, we need to start the camera for capturing the QR code. 
    For that declare a variable called a 'cam' and in this variable pass the instance cv2.VideoCapture(0). 
    The next process is we need to create a variable called detector and in this variable call the object cv2.QRCodeDetector(). 
    This object is a very helpful one for capturing QR codes in real-time. 
```

- <strong> Step 3: </strong>
``` 
   This step is very important you need to create a while loop and in this loop create a variable called an img and 
   this loop will read your webcam screen continuously until this loop breaks
```

- <strong> Step 4: </strong>
``` 
    Next, create a variable called data, and this variable is to be used to decode the QR code, and 
    if any data is present in the QR code image it will break the loop and it open the link in your browser. 
    So this is the condition that I inserted here.
```

- <strong> Step 5: </strong>
``` 
   Finally, call the object cv2.imshow this will produce the output and you’ve to assign the key to break the loop. 
   Here I assigned the key that is called q, when we press the q it will stop the video streaming.

  And then you’ve to create the variable, 
  in this variable you need to call the object webbrowser.open( pass the variable an in this object )
```
