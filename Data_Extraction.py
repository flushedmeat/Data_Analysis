import numpy as np
from matplotlib import pyplot as plt
import csv

'''
This scripts enables you to use the data from the CSV files provided by guide. All the data is extracted and transformed into floats.
The data files are ordered in columns with the following names 
altitude.csv
Column Number: 1        2       3           4           5           6                   7
Variable       time_alt, z_state, z_laser, vz_laser, z_laser_raw, throttle_trim_integral, throttle_cmd

est.csv
Column Number:      1       2       3     4     5       6
Variable        time_est vx_est, vy_est, vz_est, x_est, y_est, z_est

est_corr.csv
Column Number:      1               2           3           4           5           6           7
Variable        time_est_corr, vx_est_corr, vy_est_corr, vz_est_corr, x_est_corr, y_est_corr, z_est_corr

accel_data.csv
Column Number:      1       2       3      4
Variable        time_acc, x_acc, y_acc, z_acc

ahrs.csv
Column Number:      1           2       3           4
Variable        time_AHRS, phi_AHRS, theta_AHRS, psi_AHRS
'''


# Altitude data extraction

def func_altitude():
    with open('altitude.csv', newline='') as File:
        reader = csv.reader(File)
        time_alt = np.array([])
        z_state = np.array([])
        z_laser = np.array([])
        vz_laser = np.array([])
        z_laser_raw = np.array([])
        throttle_trim_integral = np.array([])
        throttle_cmd = np.array([])
        i = 0
        for row in reader:
            if i < 1505:
                time_alt = np.append(time_alt, float(row[0]))
                z_state = np.append(z_state, float(row[1]))
                z_laser = np.append(z_laser, float(row[2]))
                vz_laser = np.append(vz_laser, float(row[3]))
                z_laser_raw = np.append(z_laser_raw, float(row[4]))
                throttle_trim_integral = np.append(throttle_trim_integral, float(row[5]))
                throttle_cmd = np.append(throttle_cmd, float(row[6]))
                i = i + 1
            else:
                i = i + 1
        return time_alt, z_state, z_laser, vz_laser, z_laser_raw, throttle_trim_integral, throttle_cmd

# Predicted State Extraction
def func_predict_state():
    with open('est.csv', newline='') as File:
        reader = csv.reader(File)
        time_est = np.array([])
        vx_est = np.array([])
        vy_est = np.array([])
        vz_est = np.array([])
        x_est = np.array([])
        y_est = np.array([])
        z_est = np.array([])
        i = 0
        for row in reader:
            if i < 5213:
                time_est = np.append(time_est, float(row[0]))
                vx_est = np.append(vx_est, float(row[1]))
                vy_est = np.append(vz_est, float(row[2]))
                vz_est = np.append(vz_est, float(row[3]))
                x_est = np.append(x_est, float(row[4]))
                y_est = np.append(y_est, float(row[5]))
                z_est = np.append(z_est, float(row[6]))
                i = i + 1
            else:
                i = i + 1

        return time_est, vx_est, vy_est, vz_est, x_est, y_est, z_est

# Predicted State Corrected Extraction

def func_est_corr():
    with open('est_corr.csv', newline='') as File:
        reader = csv.reader(File)
        time_est_corr = np.array([])
        vx_est_corr = np.array([])
        vy_est_corr = np.array([])
        vz_est_corr = np.array([])
        x_est_corr = np.array([])
        y_est_corr = np.array([])
        z_est_corr = np.array([])
        i = 0
        for row in reader:
            if i < 5213:
                time_est_corr = np.append(time_est_corr, float(row[0]))
                vx_est_corr = np.append(vx_est_corr, float(row[1]))
                vy_est_corr = np.append(vz_est_corr, float(row[2]))
                vz_est_corr = np.append(vz_est_corr, float(row[3]))
                x_est_corr = np.append(x_est_corr, float(row[4]))
                y_est_corr = np.append(y_est_corr, float(row[5]))
                z_est_corr = np.append(z_est_corr, float(row[6]))
                i = i + 1
            else:
                i = i + 1

        return time_est_corr, vx_est_corr, vy_est_corr, vz_est_corr, x_est_corr, y_est_corr, z_est_corr

# Accelerations

def func_accel():
    with open('accel_data.csv', newline='') as File:
        reader = csv.reader(File)
        time_acc = np.array([])
        x_acc = np.array([])
        y_acc = np.array([])
        z_acc = np.array([])
        i = 0
        for row in reader:
            if i == 0:
                time_acc_0 = float(row[0]) + float(row[1]) / 1e9
                time_acc = np.append(time_acc, float(row[0]) + float(row[1]) / 1e9 - time_acc_0)
                x_acc = np.append(x_acc, float(row[2]))
                y_acc = np.append(y_acc, float(row[3]))
                z_acc = np.append(z_acc, float(row[4]))
                i = i + 1
            else:
                time_acc = np.append(time_acc, float(row[0]) + float(row[1]) / 1e9 - time_acc_0)
                x_acc = np.append(x_acc, float(row[2]))
                y_acc = np.append(y_acc, float(row[3]))
                z_acc = np.append(z_acc, float(row[4]))

        return time_acc, x_acc, y_acc, z_acc

# AHRS

def func_AHRS():
    with open('ahrs.csv', newline='') as File:
        reader = csv.reader(File)
        time_AHRS = np.array([])
        phi_AHRS = np.array([])
        theta_AHRS = np.array([])
        psi_AHRS = np.array([])
        i = 0
        for row in reader:
            if i < 5230:
                time_AHRS = np.append(time_AHRS, float(row[0]))
                phi_AHRS = np.append(phi_AHRS, float(row[1]))
                theta_AHRS = np.append(theta_AHRS, float(row[2]))
                psi_AHRS = np.append(psi_AHRS, float(row[3]))
                i = i + 1
            else:
                i = i + 1

        return time_AHRS, phi_AHRS, theta_AHRS, psi_AHRS


# Range Data
def func_range():

    with open('range_data.csv', newline='') as File:
        reader = csv.reader(File)
        time_range = np.array([])
        range_dat = np.array([])
        i = 0

        for row in reader:
            if i == 0:
                time_0_range = float(row[0]) + float(row[1]) / 1e9
                time_range = np.append(time_range, float(row[0]) + float(row[1]) / 1e9 - time_0_range)
                range_dat = np.append(range_dat, float(row[2]))
                i = i + 1
            else:
                time_range = np.append(time_range, float(row[0]) + float(row[1]) / 1e9 - time_0_range)
                range_dat = np.append(range_dat, float(row[2]))

        return time_range, range_dat

# Gyro Data

def func_gyro():
    with open('gyro_data.csv', newline='') as File:
        reader = csv.reader(File)
        time_gyro = np.array([])
        phi_gyro = np.array([])
        theta_gyro = np.array([])
        psi_gyro = np.array([])
        i = 0

        for row in reader:
            if i == 0:
                time_0_gyro = float(row[0]) + float(row[1]) / 1e9
                time_gyro = np.append(time_gyro, float(row[0]) + float(row[1]) / 1e9 - time_0_gyro)
                phi_gyro = np.append(phi_gyro, float(row[2]))
                theta_gyro = np.append(theta_gyro, float(row[3]))
                psi_gyro = np.append(psi_gyro, float(row[4]))
                i = i + 1
            else:
                time_gyro = np.append(time_gyro, float(row[0]) + float(row[1]) / 1e9 - time_0_gyro)
                phi_gyro = np.append(phi_gyro, float(row[2]))
                theta_gyro = np.append(theta_gyro, float(row[3]))
                psi_gyro = np.append(psi_gyro, float(row[4]))

        return time_gyro, phi_gyro, theta_gyro, psi_gyro

# RANSAC IN

def func_ransac_in():
    with open('ransac_in_f.csv', newline='') as File:
        reader = csv.reader(File)
        time_ran_in = np.array([])
        x_ran_in = np.array([])
        y_ran_in = np.array([])
        z_ran_in = np.array([])
        unkown_ran_in = np.array([])
        i = 0

        for row in reader:
            time_ran_in = np.append(time_ran_in, float(row[0]))
            x_ran_in = np.append(x_ran_in, float(row[1]))
            y_ran_in = np.append(y_ran_in, float(row[2]))
            z_ran_in = np.append(z_ran_in, float(row[3]))
            unkown_ran_in = np.append(unkown_ran_in, float(row[4]))

        return time_ran_in, x_ran_in, y_ran_in, z_ran_in

# RANSAC Out

def func_ransac_out():
    with open('ransac_out_f.csv', newline='') as File:
        reader = csv.reader(File)
        time_ran_out = np.array([])
        x_ran_out = np.array([])
        y_ran_out = np.array([])
        z_ran_out = np.array([])
        unkown_ran_out = np.array([])
        i = 0

        for row in reader:
            time_ran_out = np.append(time_ran_out, float(row[0]))
            x_ran_out = np.append(x_ran_out, float(row[1]))
            y_ran_out = np.append(y_ran_out, float(row[2]))
            z_ran_out = np.append(z_ran_out, float(row[3]))
            unkown_ran_out = np.append(unkown_ran_out, float(row[4]))

        return time_ran_out, x_ran_out, y_ran_out, z_ran_out

# Gates

def func_gate():
    with open('waypoints.csv', newline='') as File:
        reader = csv.reader(File)
        x_gate = np.array([])
        y_gate = np.array([])
        z_gate = np.array([])

        for row in reader:
            x_gate = np.append(x_gate, float(row[0]))
            y_gate = np.append(y_gate, float(row[1]))
            z_gate = np.append(z_gate, float(row[2]))

        return x_gate, y_gate, z_gate

'Test test test'



