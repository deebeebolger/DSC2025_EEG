## In this script we will look at the detection, visualization and removal of noisy electrodes.
# We will also look at the calculation and visualisation of the frequency-based characteristics of the EEG signal
# and how this information can be used to detect noisy electrodes.
"""
We can detect noisy electrodes by considering:
- the amplitude of activity in the time-dependent signal
- the region of the brain over which certain activity is concentrated. For example, we know that eye-blinks are characterised
by positive-going activity over frontal electrodes of the right and left hemispheres.
- by considering the frequency content of the electrode signals. High energy in the low frequency part of a spectrum indicates
activity that is slow, often of high amplitude; activity very often related to movements.

Below we will plot the power spectral density (PSD) of all electrodes for frequencies from 0.5Hz to 40Hz.
The PSD will be plotted in decibels (dB)
"""
import mne
import os
import matplotlib.pyplot as plt

# We begin by loading in .fif file that we saved at the end of script 1.
fnameIn = 'sub-001_eeg_sub-001_task-think1_eeg-hpf-ref_raw.fif'
fpathIn = 'data'
fullnameIn = os.path.join(fpathIn, fnameIn)
rawIn = mne.io.read_raw_fif(fullnameIn)

# Plot the power spectral density (PSD)
mne.viz.plot_raw_psd(rawIn, fmin=0.5, fmax=80, tmin=25, tmax=50, picks='eeg', dB=True)

# We can calculate the PSD and plot the PSD values and the frequencies.

rawSpectre = rawIn.compute_psd(method='multitaper', fmin=0.5, fmax=80, tmin=None, tmax=None, picks='eeg')
PSD, freqs = rawSpectre.get_data(exclude=(), return_freqs=True)
print(f'The PSD will be plotted for these {freqs}')

# We can plot the spectra by applying .plot() method.
rawSpectre.plot()
plt.ylabel(r'PSD ($\mu$v^2')

# We could also plot the spectrum of a subset of electrodes.
chanSelect = ['Fpz', 'Fz', 'FCz', 'Cz', 'CPz', 'Pz']
rawSpectre.plot(picks=chanSelect)

## We can also plot the topography of the activity in the different frequency bands
"""
We can plot the topographies because we added the correct montage to the dataset in script1. 

For EEG analyses we consider the following frequency bands:
- theta (4-7Hz)
- alpha (8-12Hz)
- beta (12-30Hz)
- gamma (>30Hz)
"""
# We start by defining the frequency bands.
fbands = {'Theta (4-7Hz)': (4,7), 'Alpha (8-12 Hz)': (8, 12), 'Beta (12-30 Hz)': (12, 30),
         'Gamma (30-45 Hz)': (30, 45)}
rawSpectre.plot_topomap(bands=fbands, ch_type='eeg')

## Based on the spectrum plotted, have we been able to determine any particularly noisy electrodes??
"""
We mark a channel as "bad" by adding it to the "bads" attribute of the .info object. 
The following gives an example of this, supposing we decide that Fpz and Oz are noisy electrodes.
"""
badChannels = ['PO4']
rawIn.info['bads'] = badChannels


















