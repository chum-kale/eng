from flask import Flask, render_template, Response, request, send_file, redirect, url_for
import cv2
import numpy as np
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

app = Flask(__name__)

cap = None
fgbg = None
kernel = np.ones((5, 5), np.uint8)
video_enabled = False
tampering_detected = False
tampering_log = []

# Variables to control email sending
last_email_time = datetime.datetime(2000, 1, 1)
email_interval = datetime.timedelta(minutes=5)

def init_video_capture():
    global cap, fgbg
    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()

def send_alert_email():
    # Replace with your email and password
    sender_email = 'chinmaykale2020.comp@mmcoe.edu.in'
    sender_password = 'C$K@3m501'

    # Recipient email
    recipient_email = 'parthbapat2020.comp@mmcoe.edu.in'

    # Check if enough time has passed since the last email
    global last_email_time, email_interval
    current_time = datetime.datetime.now()
    if (current_time - last_email_time) < email_interval:
        return

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Tampering Detected'

    # Message body
    message = 'Tampering has been detected in your video feed at ' + current_time.strftime("%Y-%m-%d %H:%M:%S")
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

    # Update the last email time
    last_email_time = current_time

def video_tempering():
    global video_enabled, tampering_detected, tampering_log

    while video_enabled:
        ret, frame = cap.read()
        if not ret:
            break

        bounding_rect = []
        fgmask = fgbg.apply(frame)

        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0, len(contours)):
            bounding_rect.append(cv2.boundingRect(contours[i]))

        a = 0  
        for i in range(0, len(contours)):
            if bounding_rect[i][2] >= 40 or bounding_rect[i][3] >= 40:
                a = a + (bounding_rect[i][2]) * bounding_rect[i][3]

        brightness_level = np.mean(frame)
        if a >= int(frame.shape[0]) * int(frame.shape[1]) / 2 or brightness_level < 50: 
            tampering_detected = True
            send_alert_email()  # Send an email alert
        else:
            tampering_detected = False

        if tampering_detected:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tampering_log.append(f"Tampering detected at {timestamp}")

        if tampering_detected:
            cv2.putText(frame, "TAMPERING DETECTED", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', video_enabled=video_enabled, tampering_detected=tampering_detected)

@app.route('/video')
def video():
    return Response(video_tempering(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start', methods=['POST'])
def start_video():
    global video_enabled, tampering_detected
    video_enabled = True
    tampering_detected = False
    init_video_capture()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop_video():
    global video_enabled
    video_enabled = False

    log_content = "\n".join(tampering_log)
    with open("tampering_log.txt", "w") as file:
        file.write(log_content)

    return send_file("tampering_log.txt", as_attachment=True)

@app.route('/start_again', methods=['POST'])
def start_again():
    global tampering_detected
    tampering_detected = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
