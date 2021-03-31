import sys
from PyQt5 import QtWidgets
from qt.ml import Ui_machinelearning
from pyAudioProcessing.run_classification import train_and_classify
import pyaudio
import wave
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

app= QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("machine learning")
        self.ui = Ui_machinelearning()
        self.ui.setupUi(self)
        self.ui.aufnehmen.clicked.connect(self.on_aufnehmen_click)
        self.ui.einlernen.clicked.connect(self.on_einlernen_click)
        self.ui.testen.clicked.connect(self.on_testen_click)
        self.ui.bild.setPixmap(QtGui.QPixmap('qt/bilder/baugruppe.jpg')) #Bild einfügen
        self.ui.bild.setScaledContents(True)
        self.ui.text.setText("Bitte wählen")


    def on_aufnehmen_click(self):
        self.ui.text.setText("aufnehmen")
        print("aufnehmen")
        for x in range(1,21):
            if x is 1:
                time.sleep(3)
                print("--------------------------------------------------")
                print("Bitte drehen Sie jetzt nach rechts!")
                self.ui.text.setText("Bitte drehen Sie jetzt nach rechts!")
                print("--------------------------------------------------")
                time.sleep(5)
            if x is 11:
                print("--------------------------------------------------")
                print("Bitte aufhören zu drehen!")
                self.ui.text.setText("Bitte aufhören zu drehen!")
                print("--------------------------------------------------")
                time.sleep(3)
                print("--------------------------------------------------")
                print("Bitte drehen Sie jetzt nach links!")
                self.ui.text.setText("Bitte drehen Sie jetzt nach links!")
                print("--------------------------------------------------")
                time.sleep(5)
            if x in [1,10]:
                o="rechts"
            if x in [11,20]:
                o="links"  
            #chunk = 1024  # Record in chunks of 1024 samples
            chunk = 100
            sample_format = pyaudio.paInt16  # 16 bits per sample
            channels = 1
            fs = 44100  # Record at 44100 samples per second
            seconds = 10
            filename = ("data_samples/training/"+str(o)+"/ll"+str(x)+".wav")

            p = pyaudio.PyAudio()  # Create an interface to PortAudio
            print('Recording '+str(x))
            stream = p.open(format=sample_format,
                            channels=channels,
                            rate=fs,
                            frames_per_buffer=chunk,
                            input=True)
            frames = []  # Initialize array to store frames
            # Store data in chunks for 3 seconds
            for i in range(0, int(fs / chunk * seconds)):
                data = stream.read(chunk)
                frames.append(data)
            # Stop and close the stream 
            stream.stop_stream()
            stream.close()
            # Terminate the PortAudio interface
            p.terminate()
            print('Finished recording ' + str(x))
            # Save the recorded data as a WAV file
            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(fs)
            wf.writeframes(b''.join(frames))
            wf.close()
            time.sleep(1)
            if x is 20:
                print("--------------------------------------------------")
                print("Bitte aufhören zu drehen!")
                self.ui.text.setText("Bitte aufhören zu drehen!")
                print("--------------------------------------------------")

    def on_einlernen_click(self):
        print("lernen")
        self.ui.text.setText("ich lerne!")
        train_and_classify("data_samples/training", "train", ["gfcc,mfcc"], "svm", "svm_clf")
        self.ui.bild.setPixmap(QtGui.QPixmap('qt/bilder/baugruppe.jpg'))
        self.ui.text.setText("Bereit")

    def on_testen_click(self):
        print("testen")
        self.ui.text.setText("Testen")

        #chunk = 1024  # Record in chunks of 1024 samples
        chunk = 1024
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1
        fs = 44100  # Record at 44100 samples per second
        seconds = 10
        filename = ("data_samples/testing/test/test.wav")

        for i in range(0,1):
            p = pyaudio.PyAudio()  # Create an interface to PortAudio
            print("Recording Test")
            self.ui.text.setText("Recording Test")
            stream = p.open(format=sample_format,
                            channels=channels,
                            rate=fs,
                            frames_per_buffer=chunk,
                            input=True)
            frames = []  # Initialize array to store frames
            # Store data in chunks for 3 seconds
            for i in range(0, int(fs / chunk * seconds)):
                data = stream.read(chunk)
                frames.append(data)
            # Stop and close the stream 
            stream.stop_stream()
            stream.close()
            # Terminate the PortAudio interface
            p.terminate()
            print("Finished recording Test")
            self.ui.text.setText("Finished recording Test")
            # Save the recorded data as a WAV file
            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(fs)
            wf.writeframes(b''.join(frames))
            wf.close()
            time.sleep(1)
                
            # Classify data
            from pyAudioProcessing.run_classification import train_and_classify

            train_and_classify("data_samples/testing", "classify", ["gfcc,mfcc"], "svm", "svm_clf")

            time.sleep(3)

            import json
            from pprint import pprint

            with open('classifier_results.json') as f:
                data = json.load(f)
            Klasse1 =(data["data_samples/testing\\test"]["test.wav"]["classes"][0])
            Wert1= (data["data_samples/testing\\test"]["test.wav"]["probabilities"][0])
            Klasse2= (data["data_samples/testing\\test"]["test.wav"]["classes"][1])
            Wert2= (data["data_samples/testing\\test"]["test.wav"]["probabilities"][1])
            print("###############################Ergebnis#####################################################")
            #print(str(Klasse1) + ":" + str(Wert1)) #links
            #print(str(Klasse2) + ":" + str(Wert2)) #rechts
            if Wert1>Wert2:
                print("Die Drehrichtung ist "+str(Klasse1)+", mit dem Wahrscheinlickeit von "+str(Wert1))
                self.ui.bild.setPixmap(QtGui.QPixmap('qt/bilder/baugruppelinks.jpg'))
                self.ui.text.setText("Die Drehrichtung ist "+str(Klasse1)+", mit dem Wahrscheinlickeit von "+str(Wert1))
            if Wert1<Wert2:
                print("Die Drehrichtung ist "+str(Klasse2)+", mit dem Wahrscheinlickeit von "+str(Wert2))
                self.ui.bild.setPixmap(QtGui.QPixmap('qt/bilder/baugrupperechts.jpg'))
                self.ui.text.setText("Die Drehrichtung ist "+str(Klasse2)+", mit dem Wahrscheinlickeit von "+str(Wert2))
            if Wert1==Wert2:
                print("Fehler")
                self.ui.text.setText("nochmal bitte, etwas stimmt nicht")
            print("############################################################################################")
    
window = MainWindow()
window.show()
sys.exit(app.exec_())
