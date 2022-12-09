'''
. . . . . . . . . . . . . . . . . . . . . 
.                                       .
.    <<      ><      ><       >< <<     .
.    < ><   ><<     ><<<    ><    ><<   .
.    << >< > ><    ><  ><     ><        .  
.    <<  ><  ><   ><<<<<><      ><      .
.    <<      >< ><<     ><< ><    ><<   .
.    <<      ><><<       ><<  >< <<     .
.                                       .
.             DFAB 2016/17              .
. . . . . . . . . . . . . . . . . . . . . 

Created on 21.09.2016

@author: rustr
'''

import pickle

def read_file_to_string(afile):
    with file(afile) as f:
        afile_str = f.read()
    return afile_str

def read_file_to_list(afile):
    return [line for line in open(afile, "r").readlines()]

def save_pickle_file(pickle_file, data):
    pkl = open(pickle_file, "wb" )
    pickle.dump(data, pkl)
    pkl.close()
    
def read_pickle_file(pickle_file):
    pkl = open(pickle_file, "rb" )
    data = pickle.load(pkl)
    pkl.close()
    return data

