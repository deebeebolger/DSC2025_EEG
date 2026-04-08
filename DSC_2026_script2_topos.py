import mne
import numpy as np
import matplotlib.pyplot as plt
import os

# We begin by loading in .fif file that we saved at the end of script 1.
# This is the data that has been high-pass filtered and re-referenced. 
fnameIn = 'sub-001_eeg_sub-001_task-think1_eeg_hpf_ref_raw.fif'
fpathIn = 'Data'
fullnameIn = os.path.join(fpathIn, fnameIn)
rawIn = mne.io.read_raw_fif(fullnameIn, preload=True)

##--------------------Plot topographies for defined time interval-----------------------------
'''
In addition to looking at the signal as a function, we can look at the spatial distribution 
of activity across the head (topography) over a given time interval.
A topography over a time interval can be used to highlight activity at a specific time interval. 
To plot a single topography, we need to define a vector of the mean activity over define time interval for each
electrode.
Before we can visualize the topography, we need to define the electrode layout or "montage" that corresponds to 
the current dataset's configuration. 
'''

montage = mne.channels.make_standard_montage('standard_1020')  # Assigning the standard 10-20 montage
mne.viz.plot_montage(mne.channels.make_standard_montage('standard_1020'))  # Visualize the montage
rawIn.set_montage(montage)

timeIntval = [5, 10]  # Defining the time interval over which to plot the topography.
timeIndx = rawIn.time_as_index(timeIntval)  # Find the indices of the samples in the defined time interval.
chanRange = np.arange(0, 64)
dataSeg1 = rawIn.get_data(chanRange, timeIndx[0], timeIndx[1])
dataSeg_mean = np.mean(dataSeg1, 1)

fig1, ax1 = plt.subplots(1)
mne.viz.plot_topomap(dataSeg_mean, rawIn.info, ch_type='eeg', axes=ax1)

'''
Now we will plot several topographies over time from 60seconds to 80seconds in 5 second steps.
This allows us to appreciate the change in activity across all electrodes over time.
'''

timeIntvals = np.arange(5, 25, 5)
fig2, axes = plt.subplots(1, len(timeIntvals) - 1, figsize=(15, 5))
for ind in range(len(timeIntvals) - 1):
    ind
    curr_int = [timeIntvals[ind], timeIntvals[ind + 1]]
    timeIndx2 = rawIn.time_as_index(curr_int)
    dataSegCurr = rawIn.get_data(chanRange, timeIndx2[0], timeIndx2[1])
    dataMeanCurr = np.mean(dataSegCurr, 1)

    mne.viz.plot_topomap(dataMeanCurr, rawIn.info, ch_type='eeg', axes=axes[ind], show=False)
    axes[ind].set_title(str(timeIntvals[ind]) + ' - ' + str(timeIntvals[ind + 1]) + 'seconds', {'fontsize': 20})

plt.show()

## Estimate the Current Source Density by calculating the Surface Laplacian
'''
The aim of estimating the current-source density via the spatial Laplacian is to reduce the "smearing" effects due to volume conduction and to have a topography that differentiates more clearly the activity between different regions. The key parameters of the spatial Laplacian are:

the m-constant that affects the stiffness or rigidity of the spherical spline. This should ideally be set to 4.
the smoothing constant, lambda. This is set to .000001 by default.
You can try out different values of these parameters and see if/how they alter the resulting topography.

It is important to have added the channel montage to the dataset before carrying out the spatial Laplacian.
'''

# Estimate the current source density using the Laplacian 

rawCSD = mne.preprocessing.compute_current_source_density(rawIn, stiffness=4, lambda2=1e-5)
data2plot_csd = np.array(rawCSD.get_data())

data2plot_csd_seg = data2plot_csd[chanRange, timeIndx[0]:timeIndx[1]]
data2plot_csd_segmean = np.mean(data2plot_csd_seg,1)

# Visualize the average  CSD activity over the time interval as a topography
fig2, ax2 = plt.subplots(1)
mne.viz.plot_topomap(data2plot_csd_segmean, rawCSD.info, ch_type='eeg', axes=ax2)