"""CS 417 Semester Project
    Kofi Amoah 
    Fall 2023
"""
import argparse
import numpy as np


Parser = argparse.ArgumentParser()

def piecewise_linear_interpolation(time, data):
    """
    Find the slope between two points
    :param time: time in seconds
    :param data: data from one core
    :return: slope
    """
    slope = []
    for i in range(len(time)-1):
        slope.append((data[i+1] - data[i])/(time[i+1]-time[i]))
    
    return slope

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


     