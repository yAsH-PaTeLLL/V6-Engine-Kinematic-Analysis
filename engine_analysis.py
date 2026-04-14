import numpy as np
import matplotlib.pyplot as plt


# USER INPUT

print("Enter values (press Enter or type 0 to use default values)\n")

# Crank radius
r_input = input("Enter crank radius r (default = 0.05 m): ")
if r_input == "" or r_input == "0":
    r = 0.1135
else:
    r = float(r_input)

# Connecting rod length
l_input = input("Enter connecting rod length l (default = 0.15 m): ")
if l_input == "" or l_input == "0":
    l = 0.1524
else:
    l = float(l_input)

# Force
F_input = input("Enter force F (default = 1000 N): ")
if F_input == "" or F_input == "0":
    F = 38010
else:
    F = float(F_input)


# CRANK ANGLE
theta = np.linspace(0, 2*np.pi, 500)
theta_deg = np.degrees(theta)


# CALCULATIONS

# Displacement
x = r * np.cos(theta) + np.sqrt(l**2 - (r * np.sin(theta))**2)

# Velocity 
v = np.gradient(x, theta)

# Acceleration 
a = np.gradient(v, theta)

# Torque 
torque = F * r * np.sin(theta)

# PLOTTING

# Displacement
plt.figure()
plt.plot(theta_deg, x)
plt.xlabel("Crank Angle (degrees)")
plt.ylabel("Displacement (m)")
plt.title("Displacement vs Crank Angle")
plt.grid()
plt.savefig("displacement.png")
plt.show()

# Velocity
plt.figure()
plt.plot(theta_deg, v)
plt.xlabel("Crank Angle (degrees)")
plt.ylabel("Velocity")
plt.title("Velocity vs Crank Angle")
plt.grid()
plt.savefig("velocity.png")
plt.show()

# Acceleration
plt.figure()
plt.plot(theta_deg, a)
plt.xlabel("Crank Angle (degrees)")
plt.ylabel("Acceleration")
plt.title("Acceleration vs Crank Angle")
plt.grid()
plt.savefig("acceleration.png")
plt.show()

# Torque
plt.figure()
plt.plot(theta_deg, torque)
plt.xlabel("Crank Angle (degrees)")
plt.ylabel("Torque")
plt.title("Torque vs Crank Angle")
plt.grid()
plt.savefig("torque.png")
plt.show()


# RESULTS

print("\nValues Used:")
print("r =", r)
print("l =", l)
print("F =", F)

print("\nResults:")
print("Max Displacement:", np.max(x))
print("Min Displacement:", np.min(x))
print("Max Velocity:", np.max(v))
print("Max Acceleration:", np.max(a))
print("Max Torque:", np.max(torque))
