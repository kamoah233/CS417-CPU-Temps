import sys 

from parse_temps import parse_raw_temps

from typing import List
def main (args: List[str]) -> int:
    """
    The main function for the CPU Temperatures Project.
    """
    ###################################################################
    # Parse the input file
    with open (args[1], "r") as original_temps:
        temps = list(parse_raw_temps(original_temps))
    
    # Print the parsed data
    for time, core_temps in temps:
        print (time, core_temps)
    
    return 0