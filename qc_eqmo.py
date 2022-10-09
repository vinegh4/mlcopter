import numpy as np

def v_body_to_inertial(v_body, w_body):
    return v_body + np.cross(v_body, w_body)

def prop_thrust_to_body_force(prop_thrust):
    return np.array([0, 0,-1 * np.sum(prop_thrust)])

##aka L
#def apply_rolling_moment():
#    moment[0] = prop_thrust[0] * np.linalg.norm(prop_locs_body[0]) - prop_thrust[1] * np.linalg.norm(prop_locs_body[1]) \
#        - prop_thrust[2] * np.linalg.norm(prop_locs_body[2]) + prop_thrust[3] * np.linalg.norm(prop_locs_body[3])
#
##aka M
#def apply_pitching_moment():
#    moment[1] = -1 * prop_thrust[0] * np.linalg.norm(prop_locs_body[0]) + prop_thrust[1] * np.linalg.norm(prop_locs_body[1]) \
#                - prop_thrust[2] * np.linalg.norm(prop_locs_body[2]) + prop_thrust[3] * np.linalg.norm(prop_locs_body[3])
##aka N
#def apply_yawing_moment():
#    moment[2] = -1 * prop_torque(prop_thrust[0], prop_locs_body[0,0], prop_locs_body[0, 1]) \
#                - prop_torque(prop_thrust[1], prop_locs_body[1,0], prop_locs_body[1, 1]) \
#                + prop_torque(prop_thrust[2], prop_locs_body[2,0], prop_locs_body[2, 1]) \
#                + prop_torque(prop_thrust[3], prop_locs_body[3,0], prop_locs_body[3, 1])
#
#def update_f_gravity_body():
#    f_gravity_body[0] = -1 * f_gravity_inertial[2] * np.sin(euler[1])
#    f_gravity_body[1] = f_gravity_inertial[2] * np.sin(euler[0]) * np.cos(euler[1])
#    f_gravity_body[2] = f_gravity_inertial[2] * np.cos(euler[0]) * np.cos(euler[1])
#
#def prop_torque(thrust, dist_x, dist_y) -> float:
#   #TODO figure out how to derive torque from these params
#    return 0.0