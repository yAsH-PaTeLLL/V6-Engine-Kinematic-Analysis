# V6-Engine-Kinematic-Analysis

# Kinematic and Torque Analysis of a V6 Engine

## Overview
This project models the motion of a piston in a V6 engine using the slider-crank mechanism. The aim is to analyze how piston displacement, velocity, acceleration, and torque vary with crank angle.

## Objectives
- To model piston motion using basic kinematic equations
- To compute velocity and acceleration numerically
- To analyze torque variation
- To visualize results using Python

## Tools Used
- Python
- NumPy
- Matplotlib

## Methodology
- Crank angle was varied from 0 to 360 degrees
- Displacement was calculated using slider-crank relation
- Velocity and acceleration were obtained using numerical differentiation
- Torque was calculated using a simplified force model
- Graphs were plotted for analysis

## Results

### Displacement vs Crank Angle
![Displacement](displacement.png)

### Velocity vs Crank Angle
![Velocity](velocity.png)

### Acceleration vs Crank Angle
![Acceleration](acceleration.png)

### Torque vs Crank Angle
![Torque](torque.png)

## Observations
- Maximum displacement occurs near dead center positions
- Velocity is highest at mid-stroke
- Acceleration shows rapid changes near extreme positions
- Torque varies approximately sinusoidally with crank angle

## Conclusion
This project demonstrates how engine kinematics can be analyzed using basic computational tools. It also shows the relationship between crank rotation and piston motion.

## Limitations
- Torque model is simplified
- Real engine dynamics are more complex
