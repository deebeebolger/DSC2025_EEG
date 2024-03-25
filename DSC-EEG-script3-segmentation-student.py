## Segmenting the continuous data to look at **evoked** activity
"""
We have been looking at the continuous data. But in cognitive science, we most often want to study the EEG activity
in relation to a stimulus presented during an experiment.
We call the activity that is elicited by a stimulus, the **evoked** activity.

This type of EEG activity can only be obtained if we apply an experimental protocol in which stimuli are repeatedly
presented at regular intervals; these repeated stimulus presentations are referred to as **trials**.
To study this evoked activity, we create segments or epochs of data around each stimulus: the time of presentation of the stimulus
is referred to as the T0 point and a time interval before and after this T0 is defined.
The time interval preceding the T0 (stimulus presentation point) is called the **baseline**.
The time interval following the T0 point is called the **post-stimulus interval** and it is in this interval that we study
the change in activity that has been evoked by the stimulus.

The changes in EEG activity evoked by the stimulus are called the "event-related potentials" (ERPs).
These are essentially deflections (positive or negative) in activity that can be characterised by:
- their latency: when after the stimulus (or event) they appear
- their amplitude in micro-volts
- their polarity (are they positive or negative going)

Thanks to the huge number of ERP studies carried out over the years, researchers have been to attribute certain deflections
to certain cognitive phenomenon. For example, semantic processing has been found to be reflected by an erp called the N400...
a negative-going ERP that emerges around 400ms after the stimulus. In general, the greater the amplitude of the N400, the more
a stimulus is semantically "unexpected".

For this example we will use a dataset from the following study:
Oostenveld, R., Schoffelen, J.-M., & Simanova, I. (2021). FieldTrip tutorial - CuttingEEG 2021 (1.1)
[Data set]. Zenodo. https://doi.org/10.5281/zenodo.5531370

The study investigated semantic processing of stimuli presented as pictures (black line drawings on white background),
visually displayed text or as auditory presented words. Stimuli consisted of concepts from three semantic categories:
two relevant categories (animals, tools) and a task category that varied across subjects, either clothing or vegetables.

The EEG data was recorded using the Brain Vision system and is in the Brain Vision format, which includes the following files:
A text header file (.vhdr) containing meta data.
A text marker file (.vmrk) containing information about events in the data.
A binary data file (.eeg) containing the voltage values of the EEG.

"""
import mne
import os
import pandas as pd

fname = 'sub-02_task-language_eeg.vhdr'  # This contains the header file.
fpath = os.path.join('data', 'sub-02', 'eeg')
fullpath = os.path.join(fpath, fname)
rawIn = mne.io.read_raw_brainvision(fullpath, preload=True)
sfreq = rawIn.info['sfreq']

# Has this dataset already been high-pass filtered to take out the DC offset (0Hz component)?
# Where might we look to find out?
# Can you find out what high-pass filter was applied (the cutoff frequency (hz))?


mne.viz.plot_raw(rawIn, scalings='auto', remove_dc=False)

# Extracting the event data from the raw dataset; this information is called "annotations"
# We will integrate extra information about the events in th dataset into our dataset.
EventFile = 'sub-02_task-language_eve.csv'
fullpath_events = os.path.join(fpath, EventFile)
eventsIn = pd.read_csv(fullpath_events, sep=';', header=0)  # Open up the event information using pandas.
events, eventid = mne.events_from_annotations(rawIn)
eventsIn = eventsIn.drop(['onset', 'duration', 'sample'], axis=1)
eventsIn_dict = eventsIn.to_dict()
eventsCat = eventsIn_dict['category']

# Let's carry out segmentation of the continuous
"""
We will define the time limit before (tmin) and after (tmax) the T0, this will decide the length of each epoch.

"""
tmin, tmax = [-0.2, 1]  # The time limits defined in seconds.

# Call of function to segment the data into epochs.
"""
We define the baseline as baseline=(tmin, 0), which means that we will normalise the 
post-stimulus interval (0 to 1seconds) in relation to the data that is -0.2seconds to 0 
before the stimulus. 
"""
epochData = mne.Epochs(rawIn, events, event_id=eventid, tmin=tmin, tmax=tmax, reject=None, baseline=(tmin, 0),
                       preload=True)

# Let's plot those epochs that correspond to the "cow" stimulus. We know from the events file that S111 corresponds
# to the cow stimulus.
epochData['Stimulus/S111'].plot(events=events, event_id=eventid, butterfly=False)

# We will extract only those epochs that correspond to the "cow" and the "pen" stimuli.
# Then we will average across the epochs for each to compute the ERPs or the evoked activity.
epochCow = epochData['Stimulus/S111']
epochPen = epochData['Stimulus/S181']
evokedCow = epochCow.average()
evokedPen = epochPen.average()

# Now we can plot and compare the evoked activity of both.
mne.viz.plot_compare_evokeds(dict(cow=evokedCow, pen=evokedPen), legend='upper left', show_sensors='upper right')




