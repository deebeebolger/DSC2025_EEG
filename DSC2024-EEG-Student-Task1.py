"""
## Student Task 1

For this task you will use the data from the Three Stimulus Auditory Oddball Task.
James F Cavanagh and Davin Quinn (2021). EEG: Three-Stim Auditory Oddball and Rest in Acute and Chronic TBI.
OpenNeuro. [Dataset] doi: 10.18112/openneuro.ds003522.v1.1.0

Reference:
Cavanagh JF, Wilson JK, Rieger RE, Gill D, Broadway JM, Story Remer JH, Fratzke V, Mayer AR, Quinn DK.
ERPs predict symptomatic distress and recovery in sub-acute mild traumatic brain injury. Neuropsychologia. 2019 Sep;132:107125.
doi: 10.1016/j.neuropsychologia.2019.107125. Epub 2019 Jun 19. PMID: 31228481; PMCID: PMC6702033.

EEG was recorded from the following three groups of participants while they performed a three-stimulus auditory oddball task:
- Control participants (group1)
- Participants with sub-acute mild TBI (Traumatic Brain Injury) (Group0)
- Participants with chronic TBI (group2)

Three sessions of recording were carried out:
Session 1: 3 to 14 days following injury
Session 2: an average of 2 months post-injury.
Session 3: an average of 4 months after session 1.

In this task, the participants were presented with three different auditory stimuli:
- a standard stimulus (presented 80% of the time)
- a novel, non-target stimulus (presented 10% of the time)
- a novel target stimulus (presented 10% of the time)

The datasets related to this study are in the data folder and are entitled:
- **sub-004_ses-01_task-ThreeStimAuditoryOddball_eeg_segment1.set** and corresponding associated **sub-004_ses-01_task-ThreeStimAuditoryOddball_eeg_segment1.fdt** file
- **sub-004_ses-02_task-ThreeStimAuditoryOddball_eeg_segment1.set** and its corresponding **sub-004_ses-02_task-ThreeStimAuditoryOddball_eeg_segment1.fdt file**

For this task, you will work from data from sessions 1 of the study, so you will load in the file: **sub-004_ses-01_task-ThreeStimAuditoryOddball_eeg_segment1.set**
-----------------*******-------------------*****------------------*****------------------******------------------

Task 1 Instructions

Using the script **DSC2024-EEG-Script1_students** as a guide carry out the following:

- To get you started, the code is provided for loading in and visualizing the raw data.
- Extract the following dataset information:
    - the sampling frequency (Hz)
    - the names and the type of the channels
    - the number of sample points
    - the time vector
- Determine and display the temporal resolution of the dataset.
- Do you need to remove the DC component? Do this if needed.
- What reference will you apply to the data? Plot the referenced data.
- Can you spot any artifacts in the data? Can you identify the artifact?
- Present a **temporal** and **spatial** visualization of the artifact. For the temporal visualization you can plot one or several individual electrodes.

"""

# Put your code in cells here. Maybe a cell per answer...
# Don't forget to import the required packages.
# The matplotlib widget line faciltates the presentation of interactive plots.

import mne
import os
import matplotlib.pyplot as plt


# Help for loading in the *.set file:
filename = 'sub-004_ses-01_task-ThreeStimAuditoryOddball_eeg_segment1.set' # This .set file will automatically look for its corresponding *.fdt file
filepath = 'data'
fullpath = os.path.join(filepath, filename)
rawIn = mne.io.read_raw_eeglab(fullpath, preload=True)
rawIn.plot()



