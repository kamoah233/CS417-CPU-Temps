"""CS 417 Semester Project
    Kofi Amoah 
    Fall 2023
"""
import argparse
import numpy as np
import driver


Parser = argparse.ArgumentParser()
args = Parser.parse_args()
Parser.add_argument('input_file', type=str, help='input file to read')

def piecewise_linear_interpolation(time, data):
    """
    Find the slope between two points
    :param time: time in seconds
    :param data: data from one core
    :return: slope
    """
    pli = []
    for i in range(len(time)-1):
        pli.append((data[i+1] - data[i])/(time[i+1]-time[i]))
    
    return pli

def least_squares_approximation(time, data):
    """
    Find the least squares approximation of the data
    
    :param time: time in seconds
    :param data: cpu temp data from one core
    
    """
    k = len(time)

    s_x_i = 0
    s_x_2_i = 0
    sfi = 0 
    s_x_i_f_i = 0

    """ s_x_i = np.sum(x)
    s_x_2_i = np.sum(x**2)
    sfi = np.sum(f)
    s_x_i_f_i = np.sum(x*f) """

    for i,j in enumerate(time, data):
        s_x_i += i
        s_x_2_i += i**2
        sfi += j
        s_x_i_f_i += i*j
    

    #Compute c1
    c1 = (s_x_2_i*sfi - s_x_i*s_x_i_f_i)/(k*s_x_2_i - s_x_i**2)

    #c0 computation
    c0 = ((s_x_2_i*sfi)-(s_x_i*s_x_i_f_i))/(k*s_x_2_i - s_x_i**2)

    return np.array([c0, c1])

if __name__ == '__main__':
    date = driver._get_date(args.input_file)
    
    times, cores = driver._read_file(args.input_file)

    cores_pli = []
    cores_lsa = []
    for i, core in enumerate(cores):
        cores_pli.append(piecewise_linear_interpolation(times, core))
        cores_lsa.append(least_squares_approximation(times, core))
  
    for i, core in enumerate(cores):
        driver._write_to_output_file(date, times, core, cores_pli[i], cores_lsa[i])



    

