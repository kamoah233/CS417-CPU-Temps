import parse_temps as pt
import numpy as np
from dateutil import parser

def _read_file(input_file):
    """
    Read data from the input file and store, code taken from Professor Kennedy's Github repository

    :param input_file: file to read

    :return: array of data
    """
    original_temps = open(input_file, "r")

    times = []
    cores = [[] for _ in range(4)]
   

    for time, core_temps in pt.parse_raw_temps(original_temps):
        times.append(time)
        for i, core in enumerate(core_temps):
            cores[i].append(core)

    return np.array(times), np.array(cores)

def _get_date(input_file):
    """
    Extract the date from the input file name

    :param input_file: file to read

    :return: date
    """
    date = parser.parse(input_file[0:10])
    return date

def print_core_times(times, cores):
        """
        Print the times and core temperatures

        :param times: times
        :param cores: core temperatures

        return: prints the times and core temperatures
        """
        for i,t in enumerate(times):
            print(f'{times[i]:<7} || {cores[i]:<5} |')

def _write_to_output_file (date, times, cores,PLI_data, LSA_data):
        """
        Write the data to an output file

        :param date: date acquired
        :param times: times in seconds
        :param cores: core temperatures
        :param PLI_data: piecewise linear interpolation data
        :param LSA_data: least squares approximation data

        :return: output file with least squares approximation of a data core
        """

        output_file = "output/" + date + "_core" + str(cores) + ".txt"
        output = open(f'{date}_output.txt', 'w')

        c0 = LSA_data[0]
        c1 = LSA_data[1]
        for i in range(len(times)):
            output.write(f'{times[i]} {cores[i]} {PLI_data[i]} {c0 + c1*times[i]}\n')

        output.close()




    




