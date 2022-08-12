## TUMNIC BIDS Databases

In this repository, we detail the dataset description of both, Brain and Spinal Cord Multiple Sclerosis Databases.

Note:

As all studied data are kept privately, this repository does not (and should not) feature patient-related data and/or scans.

## Table of Contents

- [Dataset Generation](#dataset-generation)
  * [Background Information](#background-information)
  * [Brain Dataset](#brain-dataset)
  * [Current Dataset Structure:](#current-dataset-structure-)
  * [New BIDS-conform Dataset Structure:](#new-bids-conform-dataset-structure-)
  
- - -

## Dataset Generation
### Background Information 

In the future, all dataset generated by the Muehlau Lab at TUMNIC should adhere to the [BIDS] (https://bids-specification.readthedocs.io/en/stable/).

### Brain Dataset

The brain database has been curated by various PhD students at the TUM lab. It consists of T1w, T2w, Flair Scans of the brain, scanned with isotropic resolution.

### Current Dataset Structure:

```
├── m_031372
│   ├── 2021-12-17
│   │   ├── d2.nii
│   │   ├── f2.nii
│   │   ├── label
│   │   ├── LST_lga_rmsf2.mat
│   │   ├── masks
│   │   ├── mri
│   │   ├── mwples_lga_0.3_rmsf2.nii
│   │   ├── ples_lga_0.3_rmsf2.nii
│   │   ├── report
│   │   ├── rmsf2.nii
│   │   ├── sf2.nii
│   │   ├── st1_filled_lga_0.3_rmsf2.nii
│   │   ├── st1.nii
│   │   ├── surf
│   │   ├── t1.nii
│   │   ├── t2.nii
│   │   ├── t3.nii
│   │   ├── wples_lga_0.3_rmsf2.nii
│   │   ├── wrmsf2.nii
│   │   └── wst1_filled_lga_0.3_rmsf2.nii
│   ├── log_pipeline.txt
│   ├── log_quality.txt
│   └── LST_tlv.csv
└── m_031957
```


### New BIDS-conform Dataset Structure:

```

.
├── CHANGES.md
├── code
│   ├── cat12-v9.1.6
│   ├── freesurfer-v7.2
│   ├── samseg-v7.2
│   └── sct-v5.6
├── dataset_description.json
├── derivatives
│   └── labels
│       ├── cat12-v9.1.6
│       │   └── sub-123456
│       │       ├── ses-20220101
│       │       │   ├── anat
│       │       │   │   └── sub-123456_ses-20220101_T1w_lesions-manual.nii.gz
│       │       │   └── sub-123456_ses-20220101_scans.tsv
│       │       └── ses-20220202
│       │           ├── anat
│       │           │   └── sub-123456_ses-2022022_T1w_lesions-manual.nii.gz
│       │           └── sub-123456_ses-20220202_scans.tsv
│       ├── freesurfer-v7.2
│       │   └── sub-123456
│       │       ├── ses-20220101
│       │       │   ├── anat
│       │       │   │   └── sub-123456_ses-20220101_T1w_lesions-manual.nii.gz
│       │       │   └── sub-123456_ses-20220101_scans.tsv
│       │       └── ses-20220202
│       │           ├── anat
│       │           │   └── sub-123456_ses-2022022_T1w_lesions-manual.nii.gz
│       │           └── sub-123456_ses-20220202_scans.tsv
│       ├── samseg-v7.2
│       │   └── sub-123456
│       │       ├── ses-20220101
│       │       │   ├── anat
│       │       │   │   └── sub-123456_ses-20220101_T1w_lesions-manual.nii.gz
│       │       │   └── sub-123456_ses-20220101_scans.tsv
│       │       └── ses-20220202
│       │           ├── anat
│       │           │   └── sub-123456_ses-2022022_T1w_lesions-manual.nii.gz
│       │           └── sub-123456_ses-20220202_scans.tsv
│       └── sct-v5.6
│           └── sub-123456
│               └── ses-20220101
│                   ├── anat
│                   │   └── sub-123456_ses-20220101_T1w_lesions-manual.nii.gz
│                   └── sub-123456_ses-20220101_scans.tsv
├── LICENSE
├── participants.json
├── participants.tsv
├── README.md
├── sub-123456
│   ├── ses-20220101
│   │   ├── anat
│   │   │   ├── sub-123456_ses-20220101_T1w.json
│   │   │   ├── sub-123456_ses-20220101_T1w.nii.gz
│   │   │   ├── sub-123456_ses-20220101_T2w.json
│   │   │   └── sub-123456_ses-20220101_T2w.nii.gz
│   │   └── sub-123456_ses-20220101_scans.tsv
│   └── ses-20220202
│       ├── anat
│       │   ├── sub-123456_ses-20220202_T1w.json
│       │   ├── sub-123456_ses-20220202_T1w.nii.gz
│       │   ├── sub-123456_ses-20220202_T2w.json
│       │   └── sub-123456_ses-20220202_T2w.nii.gz
│       └── sub-123456_ses-20220202_scans.tsv


```
