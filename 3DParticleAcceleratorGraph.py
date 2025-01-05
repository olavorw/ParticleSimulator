import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Particle class
class Particle:
    def __init__(self, position, velocity, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.energy = 0

    def update_position(self, force, time_step):
        # Calculate acceleration
        acceleration = force / self.mass
        # Update velocity
        self.velocity += acceleration * time_step
        # Update position
        self.position += self.velocity * time_step

    def gain_energy(self, energy_increment):
        self.energy += energy_increment


# ParticleAccelerator class
class ParticleAccelerator:
    def __init__(self, radius, length, particle, energy_increment):
        self.radius = radius
        self.length = length
        self.particle = particle
        self.energy_increment = energy_increment

    def simulate(self, total_time, time_step):
        positions = []
        times = np.arange(0, total_time, time_step)

        for t in times:
            # Calculate force to keep particle in circular motion
            force_magnitude = (self.particle.mass * np.linalg.norm(self.particle.velocity) ** 2) / self.radius
            force_direction = -self.particle.position[:2] / np.linalg.norm(self.particle.position[:2])
            force = np.array([force_direction[0], force_direction[1], 0]) * force_magnitude

            # Add a vertical motion component for 3D spiral
            force += np.array([0, 0, 0.1 * self.particle.mass])

            # Update particle position and gain energy
            self.particle.update_position(force, time_step)
            self.particle.gain_energy(self.energy_increment)

            # Append current position
            positions.append(self.particle.position.copy())

        return np.array(positions)


# Simulation parameters
radius = 10  # Radius of the accelerator
length = 50  # Length of the accelerator (for vertical extension)
initial_position = [radius, 0, 0]  # Initial position
initial_velocity = [0, 1, 0.1]  # Initial velocity
mass = 1  # Mass of the particle
energy_increment = 0.1  # Energy gained per time step
total_time = 20  # Total simulation time
time_step = 0.05  # Time step for the simulation

# Create a particle
particle = Particle(position=initial_position, velocity=initial_velocity, mass=mass)

# Create the accelerator
accelerator = ParticleAccelerator(radius=radius, length=length, particle=particle, energy_increment=energy_increment)

# Simulate the particle accelerator
positions = accelerator.simulate(total_time=total_time, time_step=time_step)

# Extract x, y, z positions
x_positions, y_positions, z_positions = positions.T

# 3D Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the particle's path
ax.plot(x_positions, y_positions, z_positions, label="Particle Path", lw=2)
ax.scatter(x_positions[0], y_positions[0], z_positions[0], color="red", label="Start Point", s=50)
ax.scatter(x_positions[-1], y_positions[-1], z_positions[-1], color="green", label="End Point", s=50)

# Set labels and title
ax.set_title("3D Particle Accelerator Simulation")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()
