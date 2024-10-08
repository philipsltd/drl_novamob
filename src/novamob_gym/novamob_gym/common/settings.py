# Define environment constants that can be manipulated
MAX_EPISODE_TIME = 60  # seconds
GOAL_THRESHOLD = 0.1  # meters
COLLISION_DISTANCE = 0.12  # meters
MAX_TILT = 1.57  # radians = 90 degrees
TIME_DELTA = 0.01  # seconds
TRACK_WIDTH = 1.0  # meters

# Define the possible outcomes of the episode to calculate the reward
UNKNOWN = 0
GOAL_REACHED = 1
COLLISION = 2
TIMEOUT = 3
ROLLED_OVER = 4

# Define the reward function to use
REWARD_FUNCTION = "2"

# Define the topics to subscribe to
LIDAR_TOPIC = '/scan'
ODOM_TOPIC = '/odom'
VEL_TOPIC = '/cmd_vel'