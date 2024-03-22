"""
## Student Task 1

For this task, you will use the data recorded while participants completed a range of motor/imagery tasks.
The full details of the experimental task are available via this link :
[link to physionet data repository](https://physionet.org/content/eegmmidb/1.0.0/S002/#files-panel)

The reference related to the study is:

*Schalk, G., McFarland, D.J., Hinterberger, T., Birbaumer, N., Wolpaw, J.R. BCI2000: A General-Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering 51(6):1034-1043, 2004.*

### Dataset description

64-channel EEG was recorded while participants performed different motor/imagery tasks.
 Each subject performed 14 experimental runs: two one-minute baseline runs (one with eyes open, one with eyes closed), and three two-minute runs of each of the four following tasks:

- **Task 1** A target appears on either the left or the right side of the screen. The subject opens and closes the corresponding fist until the target disappears. Then the subject relaxes.

- **Task 2** A target appears on either the left or the right side of the screen. The subject imagines opening and closing the corresponding fist until the target disappears. Then the subject relaxes.

- **Task 3** A target appears on either the top or the bottom of the screen. The subject opens and closes either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.

- **Task 4** A target appears on either the top or the bottom of the screen. The subject imagines opening and closing either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.

For this task you have data from the two baseline runs and from Tasks 1 and 2 for a single participant.
The data is in .EDF+ format (European data format).
The EEGs were recorded from 64 electrodes as per the international 10-10 system (excluding electrodes Nz, F9, F10, FT9, FT10, A1, A2, TP9, TP10, P9, and P10)

The datasets are in the data folder, which can be accessed via this amubox link:

-----------------*******-------------------*****------------------*****------------------******------------------

Task 1 Instructions

Using the script **DSC2024-EEG-Script1_students** as a guide carry out the following:

- Load in one the datasets (**eyes open**) of one of the baseline runs and visualize the raw data.
- Extract the following dataset information:
    - the sampling frequency (Hz)
    - the names and the type of the channels
    - the time vector
- Determine and display the temporal resolution of the dataset.
- Do you need to remove the DC component? Do this if needed.
- What reference will you apply to the data? Plot the referenced data.
- Can you spot any artifacts in the data? Can you identify the artifact?
- Present a **temporal** and **spatial** visualization of the artifact. For the temporal visualization you can plot one or several individual electrodes.

- Load in the dataset corresponding to the second baseline run (**eyes closed**) and carry out the same visualisation and processing steps as for the first baseline run. Then compare the two datasets.

Do you notice any differences between the two?
If so, present figures that highlight these differences.
"""

# Put your code in here.
# Maybe seperate each answer by a divider ##--------------------## (for example)
# Don't forget to import the required packages.


# Help for loading in the *.edf file:
rawIn = mne.io.read_raw_edf(fullpath, preload=True)


