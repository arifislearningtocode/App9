import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()

        day = now.strftime("%A")
        time = now.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=f'{day}', org=(50, 50),
                    fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN,
                    color=(30, 200, 200), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f'{time}', org=(50, 100),
                    fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)




