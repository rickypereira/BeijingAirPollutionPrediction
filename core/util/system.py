from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil
import csv
import multiprocessing


def list_files(dir_name):
    return [f for f in listdir(dir_name) if isfile(join(dir_name, f))]


def write_dict_to_csv(dict, fname):
    with open(fname, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])


def remove_dir(path):
    if exists(path):
        shutil.rmtree(path)


def recreate_dir(path):
    remove_dir(path)
    makedirs(path)


def num_cores():
    return multiprocessing.cpu_count()
