#!/usr/bin/env python
from configuration import PepperConfiguration
from naoqi import qi
from naoqi_proxy_python_classes.ALAnimatedSpeech import ALAnimatedSpeech
from naoqi_proxy_python_classes.ALAudioDevice import ALAudioDevice
from naoqi_proxy_python_classes.ALAudioPlayer import ALAudioPlayer
from naoqi_proxy_python_classes.ALAudioRecorder import ALAudioRecorder
from naoqi_proxy_python_classes.ALAutonomousLife import ALAutonomousLife
from naoqi_proxy_python_classes.ALBacklightingDetection import ALBacklightingDetection
from naoqi_proxy_python_classes.ALBarcodeReader import ALBarcodeReader
from naoqi_proxy_python_classes.ALBasicAwareness import ALBasicAwareness
from naoqi_proxy_python_classes.ALBattery import ALBattery
from naoqi_proxy_python_classes.ALBehaviorManager import ALBehaviorManager
from naoqi_proxy_python_classes.ALBodyTemperature import ALBodyTemperature
from naoqi_proxy_python_classes.ALChestButton import ALChestButton
from naoqi_proxy_python_classes.ALColorBlobDetection import ALColorBlobDetection
from naoqi_proxy_python_classes.ALConnectionManager import ALConnectionManager
from naoqi_proxy_python_classes.ALDarknessDetection import ALDarknessDetection
from naoqi_proxy_python_classes.ALDiagnosis import ALDiagnosis
from naoqi_proxy_python_classes.ALDialog import ALDialog
from naoqi_proxy_python_classes.ALEngagementZones import ALEngagementZones
from naoqi_proxy_python_classes.ALFaceCharacteristics import ALFaceCharacteristics
from naoqi_proxy_python_classes.ALFaceDetection import ALFaceDetection
from naoqi_proxy_python_classes.ALFsr import ALFsr
from naoqi_proxy_python_classes.ALGazeAnalysis import ALGazeAnalysis
from naoqi_proxy_python_classes.ALLandMarkDetection import ALLandMarkDetection
from naoqi_proxy_python_classes.ALLaser import ALLaser
from naoqi_proxy_python_classes.ALLeds import ALLeds
from naoqi_proxy_python_classes.ALLocalization import ALLocalization
from naoqi_proxy_python_classes.ALMemory import ALMemory
from naoqi_proxy_python_classes.ALMotion import ALMotion
from naoqi_proxy_python_classes.ALMovementDetection import ALMovementDetection
from naoqi_proxy_python_classes.ALNavigation import ALNavigation
from naoqi_proxy_python_classes.ALNotificationManager import ALNotificationManager
from naoqi_proxy_python_classes.ALPeoplePerception import ALPeoplePerception
from naoqi_proxy_python_classes.ALPhotoCapture import ALPhotoCapture
from naoqi_proxy_python_classes.ALPreferenceManager import ALPreferenceManager
from naoqi_proxy_python_classes.ALRedBallDetection import ALRedBallDetection
from naoqi_proxy_python_classes.ALRedBallTracker import ALRedBallTracker
from naoqi_proxy_python_classes.ALResourceManager import ALResourceManager
from naoqi_proxy_python_classes.ALRobotPosture import ALRobotPosture
from naoqi_proxy_python_classes.ALSegmentation3D import ALSegmentation3D
from naoqi_proxy_python_classes.ALSensors import ALSensors
from naoqi_proxy_python_classes.ALSittingPeopleDetection import ALSittingPeopleDetection
from naoqi_proxy_python_classes.ALSonar import ALSonar
from naoqi_proxy_python_classes.ALSoundDetection import ALSoundDetection
from naoqi_proxy_python_classes.ALSoundLocalization import ALSoundLocalization
from naoqi_proxy_python_classes.ALSpeechRecognition import ALSpeechRecognition
from naoqi_proxy_python_classes.ALSystem import ALSystem
from naoqi_proxy_python_classes.ALTactileGesture import ALTactileGesture
from naoqi_proxy_python_classes.ALTextToSpeech import ALTextToSpeech
from naoqi_proxy_python_classes.ALTouch import ALTouch
from naoqi_proxy_python_classes.ALTracker import ALTracker
from naoqi_proxy_python_classes.ALUserSession import ALUserSession
from naoqi_proxy_python_classes.ALVideoDevice import ALVideoDevice
from naoqi_proxy_python_classes.ALVideoRecorder import ALVideoRecorder
from naoqi_proxy_python_classes.ALVisionRecognition import ALVisionRecognition
from naoqi_proxy_python_classes.ALVisualCompass import ALVisualCompass
from naoqi_proxy_python_classes.ALVisualSpaceHistory import ALVisualSpaceHistory
from naoqi_proxy_python_classes.ALWavingDetection import ALWavingDetection
from naoqi_proxy_python_classes.ALWorldRepresentation import ALWorldRepresentation
from naoqi_proxy_python_classes.DCM import DCM
from naoqi_proxy_python_classes.PackageManager import PackageManager


# Class that helps on calling naoqi different modules and methods
# by joining them all in the same place
# This has been half generated, half cleaned up by hand
# Author: Sammy Pfeiffer <Sammy.Pfeiffer at student.uts.edu>
# and updated by Florian Herzog

class Robot(object):
    """
    Your PyNAOQI mate class.
    """
   

    def __init__(self, configuration):
        self.configuration = configuration
        self.connection_url = "tcp://" + configuration.IpPort
        self.app = qi.Application(["OurProject", "--qi-url=" + self.connection_url])
        self.app.start()
        self.session = self.app.session

        self.ALAnimatedSpeech = ALAnimatedSpeech(self.session)
        self.ALAudioDevice = ALAudioDevice(self.session)
        self.ALAudioPlayer = ALAudioPlayer(self.session)
        self.ALAudioRecorder = ALAudioRecorder(self.session)
        self.ALAutonomousLife = ALAutonomousLife(self.session)
        self.ALBacklightingDetection = ALBacklightingDetection(self.session)
        self.ALBarcodeReader = ALBarcodeReader(self.session)
        self.ALBasicAwareness = ALBasicAwareness(self.session)
        self.ALBattery = ALBattery(self.session)
        self.ALBehaviorManager = ALBehaviorManager(self.session)
        self.ALBodyTemperature = ALBodyTemperature(self.session)
        self.ALChestButton = ALChestButton(self.session)
        self.ALColorBlobDetection = ALColorBlobDetection(self.session)
        self.ALConnectionManager = ALConnectionManager(self.session)
        self.ALDarknessDetection = ALDarknessDetection(self.session)
        self.ALDiagnosis = ALDiagnosis(self.session)
        self.ALDialog = ALDialog(self.session)
        self.ALEngagementZones = ALEngagementZones(self.session)
        self.ALFaceCharacteristics = ALFaceCharacteristics(self.session)
        self.ALFaceDetection = ALFaceDetection(self.session)
        self.ALFsr = ALFsr(self.session)
        self.ALGazeAnalysis = ALGazeAnalysis(self.session)
        self.ALLandMarkDetection = ALLandMarkDetection(self.session)
        self.ALLaser = ALLaser(self.session)
        self.ALLeds = ALLeds(self.session)
        self.ALLocalization = ALLocalization(self.session)

        self.ALMemory = ALMemory(self.session)

        self.ALMotion = ALMotion(self.session)
        self.ALMovementDetection = ALMovementDetection(self.session)
        self.ALNavigation = ALNavigation(self.session)
        self.ALNotificationManager = ALNotificationManager(self.session)
        self.ALPeoplePerception = ALPeoplePerception(self.session)
        self.ALPhotoCapture = ALPhotoCapture(self.session)
        self.ALPreferenceManager = ALPreferenceManager(self.session)
        self.ALRedBallDetection = ALRedBallDetection(self.session)
        self.ALRedBallTracker = ALRedBallTracker(self.session)
        self.ALResourceManager = ALResourceManager(self.session)
        self.ALRobotPosture = ALRobotPosture(self.session)
        self.ALSegmentation3D = ALSegmentation3D(self.session)
        self.ALSensors = ALSensors(self.session)
        self.ALSittingPeopleDetection = ALSittingPeopleDetection(self.session)
        self.ALSonar = ALSonar(self.session)
        self.ALSoundDetection = ALSoundDetection(self.session)
        self.ALSoundLocalization = ALSoundLocalization(self.session)
        self.ALSpeechRecognition = ALSpeechRecognition(self.session)
        self.ALSystem = ALSystem(self.session)
        self.ALTactileGesture = ALTactileGesture(self.session)
        self.ALTextToSpeech = ALTextToSpeech(self.session)
        self.ALTouch = ALTouch(self.session)
        self.ALTracker = ALTracker(self.session)
        self.ALUserSession = ALUserSession(self.session)
        self.ALVideoDevice = ALVideoDevice(self.session)
        self.ALVideoRecorder = ALVideoRecorder(self.session)
        self.ALVisionRecognition = ALVisionRecognition(self.session)
        self.ALVisualCompass = ALVisualCompass(self.session)
        self.ALVisualSpaceHistory = ALVisualSpaceHistory(self.session)
        self.ALWavingDetection = ALWavingDetection(self.session)
        self.ALWorldRepresentation = ALWorldRepresentation(self.session)
        self.DCM = DCM(self.session)

if __name__ == '__main__':
    m = Mate("138.25.61.99", 9559)
