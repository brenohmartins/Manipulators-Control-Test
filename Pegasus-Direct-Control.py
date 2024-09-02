from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math

client = RemoteAPIClient()
sim = client.require('sim')


def moveToConfig(handles, maxVel, maxAccel, maxJerk, targetConf):
    params = {
        'joints': handles,
        'targetPos': targetConf,
        'maxVel': maxVel,
        'maxAccel': maxAccel,
        'maxJerk': maxJerk,
    }
    sim.moveToConfig(params)

sim.startSimulation()

jointHandles = [-1, -1, -1, -1, -1]
for i in range(5):
    jointHandles[i] = sim.getObjectHandle('/Pegasus/axis' + str(i+1))

vel = 120
accel = 40
jerk = 80
maxVel = [vel*math.pi/180] * 5
maxAccel = [accel*math.pi/180] * 5
maxJerk = [jerk*math.pi/180] * 5

defoult_pose = [90*math.pi/180, 0, -135*math.pi/180, -45*math.pi/180, 360*math.pi/180]
moveToConfig(jointHandles, maxVel, maxAccel, maxJerk, defoult_pose)

sim.wait(10)

sim.stopSimulation()
  