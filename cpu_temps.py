"""CS 417 Semester Project
    Kofi Amoah 
    Fall 2023
"""
import argparse
# import numpy as np


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

    #Compute the 