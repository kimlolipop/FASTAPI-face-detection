#!/usr/bin/python
import sys
import cv2
import argparse



def webcam_capture(img):

    # read image data from input stream
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img, gray


def face_detect(gray, cascasdepath="haarcascade_frontalface_default.xml"):
    # process face detection
    face_cascade = cv2.CascadeClassifier(cascasdepath)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)

    )
    print("The number of faces found = ", len(faces))

    return faces


def render(image, faces, nogui=False):
    # create output image
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + h, y + h), (0, 255, 0), 2)

    if nogui:
        try:
            cv2.imwrite('detected_face.png', image)
        except:
            pass
        
        return len(faces)
    else:
        return image, len(faces)
    


def main(img):
    parser = argparse.ArgumentParser(description='Simple Face Detection.')
    parser.add_argument("-s", "--source",
                        type=str,
                        default="0",
                        help="Source. Path to the input image.")

    parser.add_argument("-m", "--model",
                       type=str,
                       default="haarcascade_frontalface_default.xml",
                       help="Model path. Path to the 'haarcascade_frontalface_default.xml'.")

    parser.add_argument("-u", "--nogui",
                        type=bool,
                        default=False,
                        help="Enable GUI?. Disable GUI. Default False.")

    args = parser.parse_args()
    print("Using model", args.model)

    # Run the face detection
    image, gray = webcam_capture(img)      
    detected_faces = face_detect(gray, cascasdepath=args.model)
    
    
    try:
        iamge, n_faces = render(image, detected_faces, nogui=False)
        # cv2.imshow("Faces found", image)
        # cv2.waitKey(0)
        return image, n_faces

    except:
        n_faces = render(image, detected_faces, nogui=False)
        return n_faces
       
        
   

        
