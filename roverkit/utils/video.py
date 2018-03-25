from PyQt4.QtCore import *
from PyQt4.QtGui import *
import cv2


class VideoThread(QThread):

    def __init__(self,address):
        super(VideoThread,self).__init__()
        self.ip = address

    def run(self):
        cap = cv2.VideoCapture("http://"+ str(self.ip) + ":5000/?action=stream?dummy=param.mjpg")
        while cap.isOpened():
            _,frame = cap.read()
            # adjust width en height to the preferred values
            image = QImage(frame.tostring(), 640, 480, QImage.Format_RGB888).rgbSwapped()
            self.emit(SIGNAL('newImage(QImage)'), image)
