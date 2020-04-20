import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



'''

Script for loading the .csv files into data objects.
Each .csv file is converted to a Data object.

The following datasets are loaded:
 - accel_data
 - gyro_data
 - altitude
 - ahrs
 - est_corr
 - est
 - cmds
 - range_data
 - ransac_in
 - ransac_out
 - gates
 - pnp
 - flightplan
 - control
 - health
 
To see what data is available in these sets, use "DATA_NAME.headers" (fill in from list above):
   cmds.headers  =>  ['t', 'phi', 'theta', 'psi']
Then, use any of these headers to obtain the list of float values:
   cmds.phi      =>  [-0.01096, -0.021921, -0.043842, ...]

For example, to plot the throttle setting against time from the altitude dataset, use:
   plt.plot(altitude.t, altitude.throttle)
   
'''



# Class for storing data
class Data:
    def __init__(self, name, headers):
        self.headers = headers

    def addData(self, header, newSet):
        exec_string = 'self.' + header + ' = [' + ', '.join(str(x) for x in newSet) + ']'
        exec(exec_string)


# Function for loading a .csv file into the Data class
def load_csv(path, headers):
    name = os.path.splitext(os.path.basename(path))[0]
    f = open(path)
    lines = f.readlines()
    f.close()

    newData = Data(name, headers)
    
    for i in range(len(headers)):
        header = headers[i]
        newSet = []
        for line in lines:
            parts = line.strip().split(',')
            parts = [k for k in parts if k]
            if len(parts) == len(headers):
                try:
                    newSet.append(float(parts[i]))
                except:
                    newSet.append(None)
        newData.addData(header, newSet)
            
    return newData


### Function to check the lengths of the data stored in a class (debugging)
##def checkLength(obj):
##    variables = dir(obj)
##    for variable in variables:
##        if variable[0:2] != '__' and variable != 'addData':
##            exec('print(len(obj.' + variable + '))')
##    print()



# ----------------------------------------------------------------------------------
# Go through all the required files and store them into Data objects
# ----------------------------------------------------------------------------------
cwd = os.getcwd()
folderpath = os.path.join(cwd, '2019_11_15_Race3_Heat3')

# Acceleration data
filepath = os.path.join(folderpath, 'accel_data.csv')
accel_data = load_csv(filepath, ['t_raw1', 't_raw2', 's1', 's2', 's3'])
t = np.array(accel_data.t_raw1) + np.array(accel_data.t_raw2) / 1e9
t = t - t[0]
accel_data.addData('t', list(t))
accel_data.headers.append('t')

# Gyro data
filepath = os.path.join(folderpath, 'gyro_data.csv')
gyro_data = load_csv(filepath, ['t_raw1', 't_raw2', 'o1', 'o2', 'o3'])
t = np.array(gyro_data.t_raw1) + np.array(gyro_data.t_raw2) / 1e9
t = t - t[0]
gyro_data.addData('t', list(t))
gyro_data.headers.append('t')

# Altitude data
filepath = os.path.join(folderpath, 'altitude.csv')
altitude = load_csv(filepath, ['t', 'z_state', 'z_laser', 'vz_laser', 'z_laser_raw', 'throttle_trim', 'throttle', 'z_setpoint'])

# Attitude and heading reference system data
filepath = os.path.join(folderpath, 'ahrs.csv')
ahrs = load_csv(filepath, ['t', 'phi1', 'theta1', 'psi1', 'phi2', 'theta2', 'psi2'])

# Corrected state data
filepath = os.path.join(folderpath, 'est_corr.csv')
est_corr = load_csv(filepath, ['t', 'vx', 'vy', 'vz', 'x', 'y', 'z'])

# Estimator data
filepath = os.path.join(folderpath, 'est.csv')
est = load_csv(filepath, ['t', 'vx', 'vy', 'vz', 'x', 'y', 'z'])

# Commands data
filepath = os.path.join(folderpath, 'cmds.csv')
cmds = load_csv(filepath, ['t', 'phi', 'theta', 'psi'])

# Range data
filepath = os.path.join(folderpath, 'range_data.csv')
range_data = load_csv(filepath, ['t_raw1', 't_raw2', 'h'])
t = np.array(range_data.t_raw1) + np.array(range_data.t_raw2) / 1e9
t = t - t[0]
range_data.addData('t', list(t))
range_data.headers.append('t')

# Ransac in data
filepath = os.path.join(folderpath, 'ransac_in_f.csv')
ransac_in = load_csv(filepath, ['t', 'x', 'y', 'z', 'idk'])

# Ransac out data
filepath = os.path.join(folderpath, 'ransac_out_f.csv')
ransac_out = load_csv(filepath, ['t', 'x', 'y', 'z', 'vx', 'vy', 'vz'])

# Gates data
filepath = os.path.join(folderpath, 'waypoints.csv')
gates = load_csv(filepath, ['x', 'y', 'z', 'psi', 'psi_gate', 'type', 'empty', 'nr'])

# PNP data
filepath = os.path.join(folderpath, 'pnp_f.csv')
pnp = load_csv(filepath, ['t', 'i', 'gate_id', 'image_contour', 'pos_w_at0', 'pos_w_at1', 'pos_w_at2', 'yaw_fw', 'pos_fw_0', 'pos_fw_1', 'pos_fw_2', 'prior_recovery'])

# Flightplan data
filepath = os.path.join(folderpath, 'flightplan.csv')
flightplan = load_csv(filepath, ['t', 'idk1', 'idk2', 'idk3'])

# Control data
filepath = os.path.join(folderpath, 'control.csv')
control = load_csv(filepath, ['t', 'err_x_b1', 'err_x_b2', 'err_v_b1', 'err_v_b2', 'err_x_g1', 'err_x_g2', 'err_v1', 'err_v2', 'acc_cmd1', 'acc_cmd2', 'att_cmd1', 'att_cmd2', 'endp_error', 'len_error'])

# Betaflight black box data (there are too little columns?)
#filepath = os.path.join(folderpath, 'betaflight.csv')
#betaflight = load_csv(filepath, ['t', 'roll', 'pitch', 'yaw', 'throttle'])

# Health data
filepath = os.path.join(folderpath, 'health.csv')
health = load_csv(filepath, ['t', 'imu_cnt', 'rng_cnt', 'rng_ok', 'cam_cnt', 'cam_sleep_raw', 'ransac'])
cam_sleep = np.array(health.cam_sleep_raw) - health.cam_sleep_raw[0]
health.addData('cam_sleep', list(cam_sleep))
health.headers.append('cam_sleep')


### Check if all the data is loaded (all lists should have a length bigger than 0)
##checkLength(accel_data)
##checkLength(gyro_data)
##checkLength(altitude)
##checkLength(ahrs)
##checkLength(est_corr)
##checkLength(est)
##checkLength(cmds)
##checkLength(range_data)
##checkLength(ransac_in)
##checkLength(ransac_out)
##checkLength(gates)
##checkLength(pnp)
##checkLength(flightplan)
##checkLength(control)
##checkLength(health)



# ----------------------------------------------------------------------------------
# Plot the data in some way
# ----------------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(est_corr.x, est_corr.y, est_corr.z, label='est_corr.csv')
ax.plot(est.x, est.y, est.z, label='est.csv')
ax.plot(ransac_in.x, ransac_in.y, ransac_in.z, label='ransac_in_f.csv')
ax.plot(ransac_out.x, ransac_out.y, ransac_out.z, label='ransac_out_f.csv')
ax.scatter(gates.x, gates.y, gates.z, label='gates.csv')
plt.legend()
plt.show()
