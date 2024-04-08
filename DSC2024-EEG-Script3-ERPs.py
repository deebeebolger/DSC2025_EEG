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
"""

## Description of the dataset.
"""
The following  will use the data from the Three Stimulus Auditory Oddball Task. James F Cavanagh and Davin Quinn (2021). EEG: Three-Stim Auditory Oddball and Rest in Acute and Chronic TBI. OpenNeuro. [Dataset] doi: 10.18112/openneuro.ds003522.v1.1.0

Reference: Cavanagh JF, Wilson JK, Rieger RE, Gill D, Broadway JM, Story Remer JH, Fratzke V, Mayer AR, Quinn DK. ERPs predict symptomatic distress and recovery in sub-acute mild traumatic brain injury. Neuropsychologia. 2019 Sep;132:107125. doi: 10.1016/j.neuropsychologia.2019.107125. Epub 2019 Jun 19. PMID: 31228481; PMCID: PMC6702033.

EEG was recorded from the following three groups of participants while they performed a three-stimulus auditory oddball task:

Control participants (group1)
Participants with sub-acute mild TBI (Traumatic Brain Injury) (Group0)
Participants with chronic TBI (group2)
Three sessions of recording were carried out: Session 1: 3 to 14 days following injury Session 2: an average of 2 months post-injury. Session 3: an average of 4 months after session 1.

In this task, the participants were presented with three different auditory stimuli:

a standard stimulus (presented 80% of the time) - trigger code **1**
a novel, non-target stimulus (presented 10% of the time) - trigger code **2**
a novel target stimulus (presented 10% of the time) - trigger code **3**
"""


import mne
import matplotlib.pyplot as plt
import os
import numpy as np

fname = 'sub-004_ses-01_task-ThreeStimAuditoryOddball_eeg_segment1.set'
filepath = 'data'
fullpath = os.path.join(filepath, fname)
rawIn = mne.io.read_raw_eeglab(fullpath, preload=True)

## ---------------- Let's take a look at the dataset information.--------------------------
"""
- How many channels does the dataset contain?
- Does the dataset include any external electrodes?
- What sampling frequency was applied when the data was recorded?
This information is contained in the **info** object. 
"""
channels = rawIn.info['ch_names']
chanNumber = len(channels)
sfreq = rawIn.info['sfreq']

print(f'The number of channels is {chanNumber}.\n')
print(f'The sampling frequency is {sfreq}Hs.\n')


### Stop and think!
"""
- Has this dataset already been high-pass filtered to take out the DC offset (0Hz component)?
- Where might we look to find out?
- Can you find out what high-pass filter was applied (the cutoff frequency (hz))?
"""
# Let's visualize the imported data...

mne.viz.plot_raw(rawIn, scalings='auto', remove_dc=False)


### ----------What do we need to do to remove the 0Hz (or DC component)?
"""
- High pass filter the data. 
We will *filter out* those frequencies below 0.1Hz, in doing so we 
remove the 0Hz so that all the EEG signals have a mean of zero.
"""

rawInFilt = rawIn.copy().filter(0.1, None,
                                fir_design='firwin')  # Notice that we created a copy of the origin rawIn data before filtering.

mne.viz.plot_raw(rawInFilt, scalings='auto', remove_dc=False)  # Visualize in Channels X Time format.

### --------We need to re-reference the data.-----------------
"""
What can we use as the reference with this data?
"""

rawInRef = rawInFilt.copy().pick_types(eeg=True, exclude=['bads', 'eog']).set_eeg_reference(ref_channels='average')
mne.viz.plot_raw(rawInRef, scalings='auto', remove_dc=False)


### -----------------Creating events from annotations------------------
"""
Extracting the event data from the raw dataset; this information is called "annotations"
 If we look in the annotations attribute of the rawIn object, we will see that we already have information
 regarding the triggers that mark the time of onset of the stimuli. 
 Here we will create "events" based on these annotations using the *.events_from_annotations()* method.
 We need this event information when we segment the continuous data.
"""
events, eventid = mne.events_from_annotations(rawInRef)
print(events)
print(f'The eventid is {eventid}.\n')

# Let's carry out segmentation of the continuous
# We will define the time limit before (tmin) and after (tmax) the T0, this will decide the length of each epoch.

tmin, tmax = [-0.2, 1]  # The time limits defined in seconds.

# Call of function to segment the data into epochs.
"""
We define the baseline as baseline=(tmin, 0), which means that we will normalise the 
post-stimulus interval (0 to 1seconds) in relation to the data that is -0.2seconds to 0 
before the stimulus. 
"""
epochData = mne.Epochs(rawInRef, events, event_id=eventid, tmin=tmin, tmax=tmax, reject=None, baseline=(tmin, 0),
                       preload=True)

# Let's plot the segmented (or epoched) data. Each segment defines one epoch that is centered around a stimulus.

epochData.plot()

"""
We will plot the epochs that correspond to the condition: 
"""
epochData['3'].plot(events=events, event_id=eventid, butterfly=False)
epochData['4'].plot(events=events, event_id=eventid, butterfly=False)
cond3 = epochData['3']
cond4 = epochData['4']

condERP3 = cond3.average()
condERP4 = cond4.average()

# Now we can plot and compare the evoked activity of both conditions.

mne.viz.plot_compare_evokeds(dict(standardTone=condERP3, novelTone=condERP4), legend='upper left', show_sensors=None)

