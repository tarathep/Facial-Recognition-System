from PyQt5 import QtCore
import cv2
import numpy as np
from PIL import Image
import os
from PyQt5 import QtCore, QtGui,QtWidgets
from Database import Find


class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=1, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)

        self.timer = QtCore.QBasicTimer()

        self.camera.set(3, 320);
        self.camera.set(4, 240);

        self.camera.set(15, 0.1)


    def start_recording(self):
        self.timer.start(0, self)


    def stop_recording(self):
        self.timer.stop()
        self.camera.release()

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)

    # check Active  Camera is running ?
    def timerIsActive(self):
        return self.timer.isActive()

#USING TRAINING
class training:
    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()


    # Create method to get the images and label data
    def getImagesAndLabels(path):
        # Using prebuilt frontal face training model, for face detection
        detector = cv2.CascadeClassifier("trainer/haarcascade_frontalface_default.xml");

        # Get all file path
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        # Initialize empty face sample
        faceSamples = []

        # Initialize empty id
        ids = []

        # Loop all the file path
        for imagePath in imagePaths:

            # Get the image and convert it to grayscale
            PIL_img = Image.open(imagePath).convert('L')

            # PIL image to numpy array
            img_numpy = np.array(PIL_img, 'uint8')

            # Get the image id
            id = int(os.path.split(imagePath)[-1].split(".")[1])

            # Get the face from the training images
            faces = detector.detectMultiScale(img_numpy)

            # Loop for each face, append to their respective ID
            for (x, y, w, h) in faces:
                # Add the image to face samples
                faceSamples.append(img_numpy[y:y + h, x:x + w])

                # Add the ID to IDs
                ids.append(id)

        # Pass the face array and IDs array
        return faceSamples, ids


#CREARE DATA SET IMAGE CAMERA BY ID
class CreateDataSet(QtWidgets.QWidget):

    def assure_path_exists(self,path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def __init__(self, haar_cascade_filepath, parent=None):
        super().__init__(parent)
        self.imgdata = []
        self.frame = 0
        self.imsave = False

        self.classifier = cv2.CascadeClassifier(haar_cascade_filepath)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 1
        self._min_size = (30, 30)

        # Load prebuilt model for Frontal Face
        self.cascadePath = haar_cascade_filepath

        # Create classifier from prebuilt model
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath);

        # Initialize sample face image
        self.count = 0
        self.face_id = 0


    def detect_faces(self, image: np.ndarray):
        # haarclassifiers work better in black and white
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        # Get all face from the video frame
        faces = self.classifier.detectMultiScale(gray_image,1.2,5)
        return faces


    def image_data_slot(self, image_data):

        faces = self.detect_faces(image_data)
        # Convert frame to grayscale
        gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)

        for (x, y, w, h) in faces:
            if self.imsave and self.face_id != 0:
                # Crop the image frame into rectangle
                cv2.rectangle(image_data, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Save the captured image into the datasets folder
                # limit

                # Increment sample face image
                self.count += 1
                self.imgdata.append(gray[y:y + h, x:x + w])

                self.frame = (self.count)
                self.imsave = False

        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape

        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def getFrame(self):
        return self.frame

    def setImgSave(self,bool):
        self.imsave = bool

    def setFaceId(self,id):
        self.face_id = id

    def saveIMG(self):
        for i,_ in enumerate(self.imgdata):
            cv2.imwrite("dataset/User." + str(self.face_id) + '.' + str(i+1) + ".jpg", self.imgdata.pop())


#FACE DETECTION WIDGET
class FaceDetectionWidget(QtWidgets.QWidget):

    def __init__(self, haar_cascade_filepath, parent=None):
        super().__init__(parent)
        self.p = 0
        self.id = 0

        self.classifier = cv2.CascadeClassifier(haar_cascade_filepath)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 1
        self._min_size = (30, 30)


        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        #self.recongnize.assure_path_exists("trainer/")

        # Load the trained mode
        self.recognizer.read('trainer/trainer.yml')

        # Load prebuilt model for Frontal Face
        self.cascadePath = haar_cascade_filepath

        # Create classifier from prebuilt model
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath);

        # Set the font style
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def detect_faces(self, image: np.ndarray):
        # haarclassifiers work better in black and white
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        # Get all face from the video frame
        faces = self.classifier.detectMultiScale(gray_image,1.2,5)
        return faces

    def image_data_slot(self, image_data):
        faces = self.detect_faces(image_data)
        gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
        self.p = 0
        for (x, y, w, h) in faces:

            # Create rectangle around the face
            cv2.rectangle(image_data, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 2)

            # Recognize the face belongs to which ID
            Id, confidence = self.recognizer.predict(gray_image[y:y + h, x:x + w])


            percent = round(100 - confidence, 2)


            # Check the ID if exist
            #Id from tranined ,
            # - - - get data from personal (mangodb)

            find = Find("localhost", 27017, 'Facial_RecogDB').personal(str(Id))
            #   i['id'], i['fname'], i['lname'], i['job'], i['address'], i['age'],i['gender'], i['email'], i['registime']

            if find:
                if percent > 30:
                    self.p = percent
                    I = "{0} {1:.2f}%".format(find[1], percent)
                    self.id = Id
                else:
                    I = "{0} {1:.2f}%".format('unknown', percent)
                    self.id = 0
            else:
                I = "{0} {1:.2f}%".format('unknown', percent)
                self.id = 0

            # Put text describe who is in the picture
            cv2.rectangle(image_data, (x - 20, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
            cv2.putText(image_data, str(I), (x, y - 40), self.font, 1, (255, 255, 255), 2)


        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape

        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def getStatus(self):
        return self.p

    def getIdMatching(self):
        return id

