# Repository for BIDSification of the Spinal Cord Datasets

This repository is intended to provide several useful tools to generate a BIDS-compliant dataset from the current PACS output.

The scripts are intended to be executed in the following way:

1. Parse the dataset and aggregate information from both, NIFTIs and their side-car jsons.
```
python3 parse_database.py --input_directory raw_dataset_directory --output_directory . --filename dataset_description.csv
```
2. Use the parsed dataset description file (e.g. dataset_desctiption.csv) to leverage the information and generate a BIDS compliant database.

```
python3 parse_database.py --input_directory raw_dataset_directory --output_directory . --dataset_description dataset_description.csv
```
