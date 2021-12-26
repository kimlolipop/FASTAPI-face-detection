from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2
import uvicorn
import face_detection_engine

import io
from starlette.responses import StreamingResponse
from urllib.request import urlopen

app = FastAPI()




@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # print('file ', file)
    
    if file is not None:
        contents = await file.read()
        file_bytes = np.asarray(bytearray(contents), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        try:
            image, n_faces = face_detection_engine.main(opencv_image)
        except:
            n_faces = face_detection_engine.main(opencv_image)

        print('opencvImage ', opencv_image)
        
        try:
            res, im_png = cv2.imencode(".png", image)
            im = StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
            return im
        except:
            return n_face


        
        
@app.post("/cap_img/")
async def create(file: UploadFile = File(...)):

    
    if file is not None:

        contents = await file.read()
        file_bytes = np.asarray(bytearray(contents), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        try:
            image, n_faces = face_detection_engine.main(opencv_image)
        except:
            n_faces = face_detection_engine.main(opencv_image)
        
        print('opencvImage ', opencv_image)
        
        try:
            res, im_png = cv2.imencode(".png", image)
            im = StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
            return im
        except:
            return n_face

        

# if __name__ == '__main__':
#     uvicorn.run('api:app',port=7001,reload=True)