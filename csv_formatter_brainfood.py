import csv
import sys
import pprint
from collections import defaultdict
import datetime

# @Deprecated
# if len(sys.argv) < 2:
#     print "Printing example headers. Please use one of the below headers:"
#     for value in ex_headers:
#         print value.strip(' ')
#     sys.exit(0)

"""
Generates and returns a hashmap that can be used in the pandas python library (http://pandas.pydata.org/pandas-docs/stable/computation.html)

@return hashmap - Consists of Column_Headers => Data(of type List)
"""

def get_hashmap_format(csv_file, header):
    # file that we will be working with
    working_file = []

    # map
    mapping = defaultdict(list)

    # open up file and convert it into a list
    with open(csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        working_file = list(reader)

    time_dict = {}

    not_started_flag = True

    # for the given header return all the data including the timestamp
    for value in working_file:
        value[1] = value[1].strip(' ')
        if header.strip(' ') in value:
            value.remove(value[1])
            # mapping['Time'].append(str(value[0]))
            if not_started_flag:
                start_from_zero = float(value[0])
                not_started_flag = False
            time = datetime.datetime.fromtimestamp(float(value[0]) - start_from_zero).strftime('%H:%M:%S.%f')
            mapping['Time'].append(time)
            value.remove(value[0])
            for x in range(0,len(value)):
                mapping['Value ' + str(x)].append(float(value[x]))

    return mapping

def get_relative_alpha_waves(csv_file, header):
    # file that we will be working with
    working_file = []

    # map
    mapping = defaultdict(list)

    # open up file and convert it into a list
    with open(csv_file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        working_file = list(reader)

    time_dict = {}

    not_started_flag = True

    # for the given header return all the data including the timestamp
    for value in working_file:
        value[1] = value[1].strip(' ')
        if header.strip(' ') in value:
            value.remove(value[1])
            # mapping['Time'].append(str(value[0]))
            if not_started_flag:
                start_from_zero = float(value[0])
                not_started_flag = False
            time = datetime.datetime.fromtimestamp(float(value[0]) - start_from_zero).strftime('%H:%M:%S.%f')[:-3]
            mapping['Time'].append(time)
            value.remove(value[0])
            for x in range(0,len(value)):
                mapping['Value ' + str(x)].append(float(value[x]))

    return mapping