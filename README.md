# Manipulator-Robotics

### Manipulator Arm:

![image](https://i.imgur.com/aeJoJf4.gif)

## So, What is a Manipulator?

A Manipulator arm is a robotic arm made of several segments connected through joints. It is used to interact with the environment.
It consists of base, links which are connected through joints, and end effector.

Two types of joints:

1. Revolute joint and
2. Prismatic joints.

## Degree of freedom:

The total number of variabloes which define the state of a Manipulator arm is called the degree of freedom(dof).

## What about controlling a Manipulator then?

We have the following methods to control the Manipulator:

1. Forward Kinematics,
2. Inverse Kinematics
3. Dynamics

### Forward Kinematics

Involves taking in desired joint position values to move the the manipulator.

### Inverse Kinematics

Involves obtaining desired joint position values for the destination position in task space.

### Dynamics

Dynamics corresponds to using controlling Force and/or Torque values for all joints such that the final positions are approximately the destination positions.

**Application of Dynamics:**
**Pick and place: **

![image](https://i.imgur.com/aeJoJf4.gif)

### Tools and softwares used to perform the project : 

Coding was entirely done in python and the following libraries were used : 
1. The Numpy library
2. The Sympy library(for trajectory generation)
3. The Time Library
4. The Pybullet setup and library

