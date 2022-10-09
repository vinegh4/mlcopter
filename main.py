import numpy as np
print("hello, world")


### FOR PROP STATE ###
#indeces of props are as follows
# 2----0
# ------
# 1----3
prop_thrust = np.zeros(4)
prop_locs_body = np.zeros([4, 3])
copter_mass = 0.0
grav_const = 9.81

pos_ned = np.zeros(3)
pos_body = np.zeros(3)
v_body = np.zeros(3)
w_body = np.zeros(3)
force = np.zeros(3)
moment = np.zeros(3)
euler = np.zeros(3)
nav_pos = np.zeros(3)
v_inertial = np.zeros(3)
f_gravity_inertial = np.array([0, 0, grav_const * copter_mass])
f_gravity_body = np.zeros(3)

#TODO move all these functions to their own eqmo module where they should be statically implemented with tests
