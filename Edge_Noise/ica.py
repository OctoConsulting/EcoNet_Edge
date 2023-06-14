#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
notes: 
n_components is determined by the mixing matrix if one is provided
'''

from sklearn.decomposition import FastICA
import numpy as np
from scipy.io import wavfile
import sys
import os
import wave


def ica(input_file, output_folder, mixing, n_components):
    #Sprint('starting ica method')
    #sig, rate = librosa.load(input_file, mono=False)
    rate, sig = wavfile.read(input_file, 'r')
    if len(sig.shape) == 1:
        wavfile.write(os.path.join(output_folder, f'component{0}_{input_file.split(".")[0]}.wav'), rate, component.astype('int'))
    #sig = np.ndarray(sig)
    sig = sig.T
    #print(type(rate), type(sig), sig.shape)
     


    ica = FastICA(n_components=n_components, whiten='unit-variance', w_init=mixing)
    result = ica.fit_transform(sig.T).T
    for i,component in enumerate(result): 
        wavfile.write(os.path.join(output_folder, f'component{i}_{input_file.split(".")[0]}.wav'), rate, component.astype('int'))
        break
    global output_file
    output_file = os.path.join(output_folder, f'component{0}_{input_file.split(".")[0]}.wav')
        

if __name__ == '__main__':
    # check that there are two valid command line arguments
    if len(sys.argv) < 2:
        #print('usage: ica.py <input_file> <output_folder> <optional: mixing matrix to use or the number of components>')
        print('input usage: ica.py <input_file>')
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print('can\'t find input file')
        exit(1)
    if not os.path.exists('./ica_output_files'):
        print('output folder doesn\'t exist, creating it...')
        os.mkdir('./ica_output_files')
    n_components = None
    if len(sys.argv) == 4:
        # either specify components or initial mixing matrix 
        if sys.argv[3].isdigit():
            mixing=None
            n_components = int(sys.argv[3])
        elif not os.path.exists(sys.argv[3]):
            print('can\'t find matrix file')
            exit(1)
        else:
            mixing = np.load(sys.argv[3])
            n_components = mixing.shape[0]
    else: 
        try: 
            mixing = np.load('./mixing_array__small_sample_result.npy')
        except Exception as e: 
            mixing = np.array([[-200.92057392,  -32.07238278 ,  91.17172426,   81.1902078 ],[ 157.54245494, -208.08384312,   50.65676267 , -54.6570847 ],[-356.20569032,    4.66884308 ,  33.0661547,   -68.214475  ],[  13.12248818,  -85.02972371 , -45.90997451 , 137.41773449]])


        n_components = mixing.shape[0]

    ica(sys.argv[1], './ica_output_files', mixing, n_components)
    sys.out.write(output_file)
