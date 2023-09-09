from flask import Flask, render_template, Response, request
import cv2
import audio

app=Flask(__name__)
camera = cv2.VideoCapture(0)

# Audio recording parameters
STREAMING_LIMIT = 240000  # 4 minutes
SAMPLE_RATE = 44100
CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms
mic_manager = None
# import json

def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/audio_feed/<int:rec>')
def audio_feed(rec):
    global mic_manager
    if rec == 1:
        mic_manager = audio.ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
        return Response(audio.audio_trans(mic_manager))
    else:
        return Response(audio.stop_trans(mic_manager))

@app.route('/audio_feed')
def audio_feed():
    return Response(audio.audio_trans())

if __name__=='__main__':
    app.run(debug=True)