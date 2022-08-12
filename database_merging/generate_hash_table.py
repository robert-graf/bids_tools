from pathlib import Path
import argparse
import os
import sys
import hashlib
import pandas as pd

# hash generation copied from https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

# parse command line arguments
parser = argparse.ArgumentParser(description='BIDSify the MS brain database.')
parser.add_argument('-i', '--input_directory', help='Folder of database.', required=True)
parser.add_argument('-o', '--output_directory', help='Folder of bids database', required=True)
parser.add_argument('-f', '--filename', type=str, default="dataset_description.csv")

args = parser.parse_args()
data_root = Path(args.input_directory)
file_names = []
hashes = []

if __name__ == '__main__':

    dirs = sorted(list(data_root.glob('*')))
    i = 0
    for dir in dirs:  # iterate over subdirs
        files = sorted(list(dir.rglob('*.nii.gz')))  # within raw data dir
        if len(files) > 0:  # skip root_dirs and empty dirs
            for file in files:
                print(f'{os.path.join(data_root, dir, file)}')

                BUF_SIZE = 65536 # BUF_SIZE is totally arbitrary

                md5 = hashlib.md5()
                sha1 = hashlib.sha1()

                with open(file, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        md5.update(data)
                        sha1.update(data)


                print("MD5: {0}".format(md5.hexdigest()))
                print("SHA1: {0}".format(sha1.hexdigest()))

                file_names.append(os.path.join(data_root, dir, file))
                hashes.append(sha1.hexdigest())
    
    # zip file names and hashes
    df = pd.DataFrame(
    {'name': file_names,
     'hash': hashes,
    })
    df.to_csv(os.path.join(args.output_directory, args.filename),header=None, index=False)
