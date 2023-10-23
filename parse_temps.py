#! /usr/bin/env python3

"""
Taken from Professor Kennedy's Github repository
Link- https://github.com/cstkennedy/cs417-examples/tree/master/SemesterProject-CPU-Temps

This module is a collection of input helpers for the CPU Temperatures Project.
All code may be used freely in the semester project, if it is imported using 
''import parse_temps'' or ''from parse_temps import {...}'' where ''{...}''
represents one or more functions.
"""

import re
from typing import (TextIO, Iterator, List, Tuple)

def parse_raw_temps (original_temps: TextIO,
                     step_size: int = 30) -> Iterator[Tuple[ List[float]]]:
    """
    Take an input file and time-step size amd parse all core temps.

    Args:
    original_temps : the input file to parse

    step_size : the time-step size in seconds

    Returns:
    A tuple containing the next time step and a list containing _n_ core temps
    as floating point values (where _n_ is the number of CPU cores)
    """
    split_re = re.compile (r"[^0-9]*\s+|[^0-9]*$")

    for step, line in enumerate(original_temps):
        yield (step * step_size), \
        [float(entry) for entry in split_re.split(line) if line > 0]
                     
