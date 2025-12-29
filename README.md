# Robotic arm target grasping interaction system based on particle swarm optimization algorithm
A real-time interactive system for target grasping of planar redundant manipulator based on PSO algorithm is constructed. A group of particles are designed by the algorithm to find the best joint solution space through cooperation, so as to realize the real-time grasping target, obstacle avoidance detection and visual output of the manipulator.

✨ Key Features
🤖 Intelligent Inverse Kinematics:
Uses the collective intelligence of the PSO algorithm to automatically calculate joint angles for precise target grasping, effectively handling the multi-solution nature of redundant manipulators.

🛡️ Smart Obstacle Avoidance:
Built-in geometric collision detection. When obstacles (red circles) are present, the algorithm automatically filters for safe postures, prioritizing mechanical safety.

☁️ Dynamic Workspace Analysis:
Real-time sampling using the Monte Carlo method generates a blue point cloud background, intuitively displaying the theoretical reachable area under the current arm configuration.

📉 Smooth Motion Control:
Adopts a hybrid initialization strategy (Local + Global search) to eliminate jitter during continuous control, ensuring smooth motion trajectories.​​
