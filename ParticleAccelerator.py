import matplotlib.pyplot as plt
import numpy as np
import time

# Particle class
class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.energy = 0

    def update_position(self, acceleration, time_step):
        # Update velocity based on acceleration
        self.velocity += acceleration * time_step
        # Update position in a circular path
        self.position += self.velocity * time_step

    def gain_energy(self, energy_increment):
        self.energy += energy_increment


# Accelerator class
class ParticleAccelerator:
    def __init__(self, radius, particle, energy_increment):
        self.radius = radius
        self.particle = particle
        self.energy_increment = energy_increment

    def simulate(self, total_time, time_step):
        positions = []
        times = np.arange(0, total_time, time_step)

        for t in times:
            # Simulate circular movement
            angle = (self.particle.position / self.radius) % (2 * np.pi)
            x = self.radius * np.cos(angle)
            y = self.radius * np.sin(angle)
            positions.append((x, y))

            # Update particle position and energy
            self.particle.update_position(acceleration=0.01, time_step=time_step)
            self.particle.gain_energy(self.energy_increment)

        return positions


# Initialize simulation
radius = 10  # Radius of the accelerator
initial_position = 0  # Initial position (radians)
initial_velocity = 0.5  # Initial velocity
mass = 1  # Mass of the particle
energy_increment = 0.1  # Energy gained per time step
total_time = 20  # Total simulation time
time_step = 0.1  # Time step for the simulation

# Create a particle
particle = Particle(position=initial_position, velocity=initial_velocity, mass=mass)

# Create the accelerator
accelerator = ParticleAccelerator(radius=radius, particle=particle, energy_increment=energy_increment)

# Simulate the particle accelerator
positions = accelerator.simulate(total_time=total_time, time_step=time_step)

# Extract x and y positions for plotting
x_positions, y_positions = zip(*positions)

# Plot the particle trajectory
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, label="Particle Path")
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Particle Accelerator Simulation")
plt.xlabel("x position")
plt.ylabel("y position")
plt.legend()
plt.grid()
plt.show()
