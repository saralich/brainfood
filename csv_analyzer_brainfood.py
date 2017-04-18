import pandas as pd
import matplotlib.pyplot as plt
import csv_formatter_brainfood
import math
import sys
import copy

# plt.style.use('presentation')
pd.set_option('display.mpl_style', 'default')

# function applied to data
# def frontal_asymmetry_log(x):
#    return math.log(x)

# returns a dataframe back given a csv file
def getDF(csv_file):
    hasmap = csv_formatter_brainfood.get_hashmap_format('./CSV Data/' + csv_file, '/muse/elements/beta_relative')
    i = [pd.Timestamp(x).strftime('%M:%S.%f')[:-3] for x in hasmap['Time']]
    del hasmap['Time']

    return pd.DataFrame(hasmap, index=i)

# gives an array of all the same mean back (used for the threshold)
def get_array(mean, baseline_data):
    arr = []
    for x in range(0, baseline_data):
        arr.append(mean)
    return arr

# change this to change the person + trial you're looking at.
name = sys.argv[1]

# constructs the dataframe
baseline_data = getDF('BrainFood_' + name + '_relax.csv')

# get the relax threshold
relax_threshold = pd.Series(get_array(getDF('BrainFood_' + name + '_relax.csv').mean().mean(), len(baseline_data)), index=baseline_data.index)

# contsructs NF nature1 dataframe
nofood_nature1_data = getDF('BrainFood_' + name + '_nofood_nature1.csv')

# rename columns to match sensors
nofood_nature1_data = nofood_nature1_data.rename(index=str,columns={'Value 0':'TP9 (NF)','Value 1':'AF7 (NF)','Value 2':'AF8 (NF)','Value 3':'TP10 (NF)'})

# set the threshold to the dataframe for comparison
nofood_nature1_data['Relax Threshold'] = relax_threshold

# constructs NF office dataframe
nofood_office_data = getDF('BrainFood_' + name + '_nofood_office.csv')

# rename columns to match sensors
nofood_office_data = nofood_office_data.rename(index=str,columns={'Value 0':'TP9 (NF)','Value 1':'AF7 (NF)','Value 2':'AF8 (NF)','Value 3':'TP10 (NF)'})

# set the threshold to the dataframe for comparison
nofood_office_data['Relax Threshold'] = relax_threshold

# constructs NF nature2 dataframe
nofood_nature2_data = getDF('BrainFood_' + name + '_nofood_nature2.csv')

# rename columns to match sensors
nofood_nature2_data = nofood_nature2_data.rename(index=str,columns={'Value 0':'TP9 (NF)','Value 1':'AF7 (NF)','Value 2':'AF8 (NF)','Value 3':'TP10 (NF)'})

# set the threshold to the dataframe for comparison
nofood_nature2_data['Relax Threshold'] = relax_threshold

# contsructs nature1 the dataframe
food_nature1_data = getDF('BrainFood_' + name + '_food_nature1.csv')

# rename columns to match sensors
food_nature1_data = food_nature1_data.rename(index=str,columns={'Value 0':'TP9 (F)','Value 1':'AF7 (F)','Value 2':'AF8 (F)','Value 3':'TP10 (F)'})

# set the threshold to the dataframe for comparison
food_nature1_data['Relax Threshold'] = relax_threshold

# constructs the office dataframe
food_office_data = getDF('BrainFood_' + name + '_food_office.csv')

# rename columns to match sensors
food_office_data = food_office_data.rename(index=str,columns={'Value 0':'TP9 (F)','Value 1':'AF7 (F)','Value 2':'AF8 (F)','Value 3':'TP10 (F)'})

# set the threshold to the dataframe for comparison
food_office_data['Relax Threshold'] = relax_threshold

# constructs the nature2 dataframe
food_nature2_data = getDF('BrainFood_' + name + '_food_nature2.csv')

# rename columns to match sensors
food_nature2_data = food_nature2_data.rename(index=str,columns={'Value 0':'TP9 (F)','Value 1':'AF7 (F)','Value 2':'AF8 (F)','Value 3':'TP10 (F)'})

# set the threshold to the dataframe for comparison
food_nature2_data['Relax Threshold'] = relax_threshold

"""

Dislaying Graphs

"""
# no food nature1 graph
nofood_nature1_graph = nofood_nature1_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Nature1 Beta Waves AF7')
nofood_nature1_graph.set_xlabel('Time (MM:SS.NS)')
nofood_nature1_graph.set_ylabel('Beta Relative')
nofood_nature1_graph.set_xlim(0.0, 1500.0)

# no food office graph
nofood_office_graph = nofood_office_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Office Beta Waves AF7')
nofood_office_graph.set_xlabel('Time (MM:SS.NS)')
nofood_office_graph.set_ylabel('Beta Relative')
nofood_office_graph.set_xlim(0.0, 1500.0)

# no food nature2 graph
nofood_nature2_graph = nofood_nature2_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Nature2 Beta Waves AF7')
nofood_nature2_graph.set_xlabel('Time (MM:SS.NS)')
nofood_nature2_graph.set_ylabel('Beta Relative')
nofood_nature2_graph.set_xlim(0.0, 1500.0)

# food nature1 graph
food_nature1_graph = food_nature1_data.ix[:,['AF7 (F)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Nature1 Beta Waves AF7')
food_nature1_graph.set_xlabel('Time (MM:SS.NS)')
food_nature1_graph.set_ylabel('Beta Relative')
food_nature1_graph.set_xlim(0.0, 1500.0)

# food office graph
food_office_graph = food_office_data.ix[:,['AF7 (F)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Office Beta Waves AF7')
food_office_graph.set_xlabel('Time (MM:SS.NS)')
food_office_graph.set_ylabel('Beta Relative')
food_office_graph.set_xlim(0.0, 1500.0)

# food nature2 graph
food_nature2_graph = food_nature2_data.ix[:,['AF7 (F)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot(title=name + ' Nature2 Beta Waves AF7')
food_nature2_graph.set_xlabel('Time (MM:SS.NS)')
food_nature2_graph.set_ylabel('Beta Relative')
food_nature2_graph.set_xlim(0.0, 1500.0)

# display both the non food and food on the same graph
nofood_nature1_graph_copy = nofood_nature1_graph
combined_nature1_graph = food_nature1_data.ix[:,['AF7 (F)']].ewm(alpha=0.05).mean().plot(title=name + ' Combined Nature 1 Beta Waves AF7 ', ax=nofood_nature1_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot())
combined_nature1_graph.set_xlabel('Time (MM:SS.NS)')
combined_nature1_graph.set_ylabel('Beta Relative')
combined_nature1_graph.set_xlim(0.0, 1500.0)

# display both the non food and food on the same graph
nofood_office_graph_copy = nofood_office_graph
combined_office_graph = food_office_data.ix[:,['AF7 (F)']].ewm(alpha=0.05).mean().plot(title=name + ' Combined Office Beta Waves AF7 ', ax=nofood_office_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot())
combined_office_graph.set_xlabel('Time (MM:SS.NS)')
combined_office_graph.set_ylabel('Beta Relative')
combined_office_graph.set_xlim(0.0, 1500.0)

# display both the non food and food on the same graph
nofood_nature2_graph_copy = nofood_nature2_graph
combined_nature2_graph = food_nature2_data.ix[:,['AF7 (F)']].ewm(alpha=0.05).mean().plot(title=name + ' Combined Nature2 Beta Waves AF7 ', ax=nofood_nature2_data.ix[:,['AF7 (NF)', 'Relax Threshold']].ewm(alpha=0.05).mean().plot())
combined_nature2_graph.set_xlabel('Time (MM:SS.NS)')
combined_nature2_graph.set_ylabel('Beta Relative')
combined_nature2_graph.set_xlim(0.0, 1500.0)

"""

Saving Results to Files

"""

nofood_nature1_graph.get_figure().savefig('./Analyzation/' + name + '/NoFood_Nature1_AF7_Graph')

nofood_office_graph.get_figure().savefig('./Analyzation/' + name + '/NoFood_Office_AF7_Graph')

nofood_nature2_graph.get_figure().savefig('./Analyzation/' + name + '/NoFood_Nature2_AF7_Graph')

food_nature1_graph.get_figure().savefig('./Analyzation/' + name + '/Food_Nature1_AF7_Graph')

food_office_graph.get_figure().savefig('./Analyzation/' + name + '/Food_Office_AF7_Graph')

food_nature2_graph.get_figure().savefig('./Analyzation/' + name + '/Food_Nature2_AF7_Graph')

combined_nature1_graph.get_figure().savefig('./Analyzation/' + name + '/Combined_Nature1_AF7_Graph')

combined_office_graph.get_figure().savefig('./Analyzation/' + name + '/Combined_Office_AF7_Graph')

combined_nature2_graph.get_figure().savefig('./Analyzation/' + name + '/Combined_Nature2_AF7_Graph')


ex_headers = [' /muse/acc', ' /muse/eeg', ' /muse/eeg/quantization', ' /muse/elements/alpha_relative', ' /muse/elements/beta_relative', ' /muse/elements/delta_relative', ' /muse/elements/gamma_relative', ' /muse/elements/theta_relative', ' /muse/elements/horseshoe', ' /muse/elements/is_good', ' /muse/elements/blink', ' /muse/elements/jaw_clench', ' /muse/elements/touching_forehead', ' /muse/elements/experimental/concentration', ' /muse/elements/experimental/mellow', ' /muse/elements/raw_fft0', ' /muse/elements/raw_fft1', ' /muse/elements/raw_fft2', ' /muse/elements/raw_fft3', ' /muse/elements/low_freqs_absolute', ' /muse/elements/alpha_absolute', ' /muse/elements/beta_absolute', ' /muse/elements/delta_absolute', ' /muse/elements/gamma_absolute', ' /muse/elements/theta_absolute', ' /muse/elements/alpha_session_score', ' /muse/elements/beta_session_score', ' /muse/elements/delta_session_score', ' /muse/elements/gamma_session_score', ' /muse/elements/theta_session_score', ' /muse/drlref', ' /muse/config', ' /muse/version', ' /muse/batt']
