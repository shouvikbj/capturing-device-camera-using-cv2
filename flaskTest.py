import requests
import numpy as np
import cv2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	url = "http://192.168.1.4:8080/shot.jpg"
	cap = cv2.VideoCapture(url)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
	while True:
		img_resp = requests.get(url)
		img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
		img = cv2.imdecode(img_arr, -1)
		out.write(img)
		cv2.imshow("Mobile Camera", img)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	return "<strong>Video Record Complete</strong>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
