"""
## Student Task 2

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
- sub-004-ses-01_task-ThreeStimAuditoryOddball_eeg.edf
- sub-004-ses-02_task-ThreeStimAuditoryOddball_eeg.edf

You will work from data from sessions 2 of the study.
-----------------*******-----""--------------*****------------------*****------------------******------------------
Load in the dataset, sub-004_ses-02_task-ThreeStimAuditoryOddball_eeg.edf and carry out the following steps.

A.
1. Print the most important information concerning the EEG data to the screen. Important information means that information
which you will need to visualize, process or interpret the data.
2. Visualize all channels in such a way that you scroll through and explore the data across time.
                    - Note down the times (onset and offset) of any very noisy intervals.
                    - Are there only scalp "eeg" channels? What other channels are present in the data?
4. Remove the DC offset and check that it has been removed.
5. Reconstruct the time vector (in seconds) and plot the raw data of a selection of **frontal electrodes**.
6. If required, downsample the data. Presuming that we are interested in frequencies up 40Hz, what is the lowest sampling
frequency that we can apply?
7. Lowpass filter the data, applying a cutoff of 40Hz. Compare the Cz signal before and after filtering.
8. Annotate the continuous data, marking the following:
    - muscular artifacts
    - very large eye blinks
9. Note two time intervals presenting these artifacts and display the following figures:
    - the time course of the above artifacts; pick channels that best present the artifact.
    - the spectrum of these artifacts
    - the topography of the artifacts
10. Can you identify any particularly noisy electrodes using temporal and spectral visualizations?
11. Re-reference the data to the average reference, leaving out any band electrodes.

B.
Try to create a way of automatically detecting eye-blink artifacts.
You will need to consider:
 - the amplitude of the eye-blinks,
 - how long an eye-blink lasts for and
 - on which electrodes the eye-blinks typically occur.

 C. (If you have time)
 Epoch the continuous data that has been at least:
 - high pass filtered
 - referenced
 Take into account the following :
    - the baseline needs to 0.2seconds long and before the stimulus.
    - the total duration of the epoch needs to 1.2seconds.

Three conditions will be defined:
- novel tone : 1
- standard tone : 2
- target tone : 3

Plot and the compare the ERPs (evoked data) of the three types of tones.
"""
# Don't forget to import the necessary packages.
import mne
import pandas as pd
import os


# Load in the rawdata (*.edf dataset)

# Some code to help with the segmentation.
# You will segment the rawdata that has been highpass filterd and re-referenced at least,
# rawdataRef.
fpath = 'data'
fname_event = 'sub-004_ses-02_task-ThreeStimAuditoryOddball_events.csv'
fullpath  = os.path.join(fpath, fname_event)
event_data = pd.read_csv(fullpath, sep=';', header=None)
annotations = mne.Annotations(event_data[0], event_data[1], event_data[2])

rawdataRef.set_annotations(annotations)
events, event_id = mne.events_from_annotations(rawdataRef)

# We define two conditions as a dictionary.
event_dict = {'Novel Tone': 1, 'Standard Tone': 2, 'Target Tone': 3}

