#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']
for room in testingrooms:
    pathway_testingroom = 'testingroom' + room + '/experiment_data.csv' #new pathway for the directory to determine where the experiment files are
    pathway_rawdata = 'rawdata/experiment_data_' + room + '.csv' #where files will be moved
    shutil.copy(pathway_testingroom,pathway_rawdata) #this function allows to move and rename files in testingroom to rawdata

#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5))
for room in testingrooms:
    new_pathway = 'rawdata/experiment_data_' + room + '.csv'
    tmp = sp.loadtxt(new_pathway, delimiter=',')
    data = np.vstack([data,tmp])


#%%
# calculate overall average accuracy and average median RT
#
import numpy as np
accuracy_list = []
for acc in range(92):
    accuracy_list.append(data[acc][3]) #this allows us to add acc from column 3 onto accuracy_list

acc_avg = np.mean=(accuracy_list)*100   # 91.48%

mrt_list = []
for rt in range(92):
    mrt_list.append(data[rt][4]) #allows us to add rt from column 4 onto mrt_list
    
mrt_avg = np.median=(mrt_list)   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#


#for stimulus in range(92): 
#    x = data[stimulus][1]
#    if x == 1:
#        words += 1
#    else:
#        faces += 1

words = 0
faces = 0
words_rt_sum = 0
words_acc_sum = 0
faces_rt_sum = 0
faces_acc_sum = 0

for stim in range(92):
    s = data[stim][1]
    if s > 1:
        faces += 1 #this counts the number of datapoints for each condition
        faces_rt_sum+= (data[stim][4])
        faces_acc_sum+= (data[stim][3])
    else:
        words += 1 #this counts the number of datapoints for each condition
        words_rt_sum+= (data[stim][4])
        words_acc_sum+= (data[stim][3])

#calculating averages for each condition:

# words: 88.6%, 489.4ms
words_rt_avg = words_rt_sum / words
words_acc_avg = (words_acc_sum / words)*100

#faces: 94.4%, 465.3ms
faces_rt_avg = faces_rt_sum / faces
faces_acc_avg = (faces_acc_sum / faces)*100
#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
import numpy as np
acc_wp_list = []
acc_bp_list = []
mrt_wp_list = []
mrt_bp_list = []

for stim in range(92):
    t = data[stim][2]
if t > 1:
    acc_wp_list.append(data[stim][3])
    mrt_wp_list.append(data[stim][4])
else:
    acc_bp_list.append(data[stim][3])
    mrt_bp_list.append(data[stim][3])

acc_wp = np.mean=(acc_wp_list)*100 # 94.0%
acc_bp = np.mean=(acc_bp_list)*100  # 88.9%
mrt_wp = np.mean=(mrt_wp_list)  # 469.6ms
mrt_bp = np.mean=(mrt_bp_list)  # 485.1ms
#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
import numpy as np
words_wp_median_rt = []
words_bp_median_rt = []
faces_wp_median_rt = []
faces_bp_median_rt = []

for rt in range(92):
    stim = data[rt][1]
    pairing = data[rt][2]
    if stim ==1 and pairing ==1:
        words_wp_median_rt.append(data[rt][4])
    elif stim ==1 and pairing ==2:
        words_bp_median_rt.append(data[rt][4])
    elif stim ==2 and pairing == 1:
        faces_wp_median_rt.append(data[rt][4])
    elif stim == 2 and pairing ==2:
        faces_bp_median_rt.append(data[rt][4])

wwp_median_rt = np.median=(words_wp_median_rt)
wbp_median_rt = np.median=(words_bp_median_rt)
fwp_median_rt = np.median=(faces_wp_median_rt)
fbp_median_rt = np.median=(faces_bp_median_rt)
# words - white/pleasant:1,1 478.4ms
# words - black/pleasant:1,2 500.3ms
# faces - white/pleasant:2,1 460.8ms
# faces - black/pleasant:2,2 469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
ttest_words: scipy.stats.ttest_rel(words_wp_median_rt,words_bp_median_rt)
ttest_faces: scipy.stats.ttest_rel (faces_wp_median_rt,faces_bp_median_rt)
# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...