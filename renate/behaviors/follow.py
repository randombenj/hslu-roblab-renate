import logging
import threading
import time


def start_following(renate):
    logging.info("following")

    renate.robot.ALTracker.stopTracker()
    renate.robot.ALTracker.unregisterAllTargets()

    # robot must be in standing posture and stiff
    #  (http://doc.aldebaran.com/2-5/naoqi/trackers/index.html)
    renate.robot.ALRobotPosture.goToPosture("Stand", 0.5)
    renate.robot.ALMotion.stiffnessInterpolation("Body", 1, 0.1)

    renate.robot.ALTracker.registerTarget("People", [])
    distance_x, distance_y = 1.0, 1.0
    threshold_x, threshold_y = 0.0, 0.0
    angle_wz = 0.0
    threshold_wz = 0.0

    # track
    renate.robot.ALTracker.setRelativePosition([
      distance_x,
      distance_y,
      angle_wz,
      threshold_x,
      threshold_y,
      threshold_wz
    ])

    renate.robot.ALLeds.fadeRGB2("FaceLeds", "blue", 1)
    renate.robot.ALTracker.setEffector("None") # no arms
    renate.robot.ALTracker.setMode("Move")

    # view if pepper looses target
    (renate.robot.ALMemory.subscriber("ALTracker/TargetLost")
      .signal.connect(lambda: logging.info("lost target")))

    renate.robot.ALTracker.track("People")
    renate.following = True

    def track_target_loss(renate):
        while renate.following:
            time.sleep(0.2)
            target_position = renate.robot.ALTracker.getTargetPosition(2)
            print(target_position)

    #thread = threading.Thread(target=track_target_loss, args=[renate])
    #thread.daemon = True
    #thread.start()

def stop_following(renate):
      logging.info("stop following")
      renate.following = False
      renate.robot.ALTracker.stopTracker()
      renate.robot.ALTracker.unregisterAllTargets()
      renate.robot.ALMotion.wakeUp()
      renate.robot.ALMotion.stiffnessInterpolation("Body", 1, 0.1)
      renate.robot.ALRobotPosture.goToPosture("Stand", 0.5)

      renate.robot.ALLeds.reset("FaceLeds")
