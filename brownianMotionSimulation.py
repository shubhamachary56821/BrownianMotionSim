import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Arena size
arena_size = 10  # 10x10 square
robot_position = np.array([0.0, 0.0])  # Start at the center
robot_direction = np.array([1.0, 0.5])  # Initial direction
robot_direction /= np.linalg.norm(robot_direction)  # Normalize direction

step_size = 0.3  # Movement step size

# Update function for animation
def update(frame):
    global robot_position, robot_direction

    # Move forward
    robot_position += robot_direction * step_size

    # Check for wall collision and reflect direction
    for i in range(2):  # Check x and y
        if abs(robot_position[i]) >= arena_size / 2:
            robot_direction[i] *= -1  # Reflect motion
            robot_position[i] = np.clip(robot_position[i], -arena_size / 2, arena_size / 2)

    # ✅ Fix: Set data as a sequence
    robot.set_data([robot_position[0]], [robot_position[1]])
    return robot,

# Visualization setup
fig, ax = plt.subplots()
ax.set_xlim(-arena_size / 2, arena_size / 2)
ax.set_ylim(-arena_size / 2, arena_size / 2)
robot, = ax.plot([], [], 'ro', markersize=8)  # Red dot

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
