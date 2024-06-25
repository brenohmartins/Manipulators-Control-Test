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

jointHandles = [-1, -1, -1, -1, -1, -1]
for i in range(6):
    jointHandles[i] = sim.getObjectHandle('/UR10/joint' + str(i+1))

vel = 120
accel = 40
jerk = 80
maxVel = [vel*math.pi/180] * 6
maxAccel = [accel*math.pi/180] * 6
maxJerk = [jerk*math.pi/180] * 6

targetPos1 = [90*math.pi/180] * 6
moveToConfig(jointHandles, maxVel, maxAccel, maxJerk, targetPos1)

targetPos2 = [-90*math.pi/180, 45*math.pi/180, 90*math.pi/180, 135*math.pi/180, 90*math.pi/180, 90*math.pi/180]
moveToConfig(jointHandles, maxVel, maxAccel, maxJerk, targetPos2)

targetPos3 = [0] * 6
moveToConfig(jointHandles, maxVel, maxAccel, maxJerk, targetPos3)

sim.stopSimulation()