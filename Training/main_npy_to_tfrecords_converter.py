
''' Script that converts npy files into TFRecords files '''
import sys
import os
sys.path.append(os.getcwd())

from Settings.arguments import arguments
from Training.tfrecords_converter import TFRecordsConverter

BATCH_SIZE = 1024

NPY_DIR_TRAIN = os.path.join(arguments.data_path, 'npy')

TFRECORDS_DIR_TRAIN = os.path.join(arguments.data_path, 'tfrecords')

def main():
    print('Initializing TFRecords Converter...')
    converter = TFRecordsConverter(BATCH_SIZE)
    print('Converting NPY to TFRecords...')
    converter.convert_npy_to_tfrecords(NPY_DIR_TRAIN, TFRECORDS_DIR_TRAIN)
    print('Done!')




main()
