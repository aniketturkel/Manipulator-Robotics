import time
import pybullet
import numpy as np
import sympy as sp
import mpmath as m
from sympy import Symbol
import pybullet_data

physics_client = pybullet.connect(pybullet.GUI) #For creating GUI
pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

#planeID = pybullet.loadURDF("Downloads/base.urdf") #For plane
Robot = pybullet.loadURDF("/home/aniket/Downloads/pybullet-force-control-main/urdf/ur5.urdf", useFixedBase = 1)

#pybullet.getNumJoints(Robot)
position, orientation = pybullet.getBasePositionAndOrientation(Robot) #Position and orientation
#pybullet.getJointInfo(Robot, 8) # The second argument is the link number whose info you want
joint_positions = [ j[0] for j in pybullet.getJointStates(Robot, range(8))]
#world_positions = pybullet.getLinkStates(Robot, range(7)) #For positions of links

pybullet.setGravity(0, 0, -9.8)
pybullet.setRealTimeSimulation(0)

#pybullet.addUserDebugLine([0,0,0], [1,1,1], [255,0,0],10)

pybullet.setJointMotorControlArray(Robot, range(8), pybullet.POSITION_CONTROL, targetPositions = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]) #For moving the joints

pybullet.stepSimulation()
time.sleep(1/25)

time.sleep(5)

pybullet.setJointMotorControlArray(Robot, range(8), pybullet.POSITION_CONTROL, targetPositions = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]) #For moving the joints

pybullet.stepSimulation()
time.sleep(1/25)

time.sleep(5)

numJoints = pybullet.getNumJoints(Robot)
revolute_joints = []
upper_limits = []
lower_limits = []
for i in range(numJoints):

    info = pybullet.getJointInfo(Robot, i)

    jointName = info[1]
    jointType = info[2]
    if (jointType == pybullet.JOINT_REVOLUTE):
        revolute_joints.append(i)

    lower_limits.append(-1* np.pi) 
    upper_limits.append( np.pi)

p0 = np.array([0.3,-0.5,1.2])
targetPositionsJoints = pybullet.calculateInverseKinematics(Robot, 7, [0.3,-0.5,1.2])
print(targetPositionsJoints)
pybullet.setJointMotorControlArray(Robot, revolute_joints, pybullet.POSITION_CONTROL, targetPositions = targetPositionsJoints)

for _ in range(10000):  
    pybullet.stepSimulation()
    time.sleep(1/25)
