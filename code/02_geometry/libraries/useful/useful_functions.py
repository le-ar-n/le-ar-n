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

Created on 15.09.2016

@author: rustr
'''

def map_range(value, fromMin, fromMax, toMin, toMax):
    """ A simple, but very practical function: bring a value within the range of (fromMin, fromMax) 
    to the range of (toMin, toMax): make a linear interpolation. """
    fromSpan = fromMax - fromMin
    toSpan = toMax - toMin
    valueScaled = float(value - fromMin)/float(fromSpan)
    return toMin + (valueScaled * toSpan)

def clamp(value, minv, maxv):
    ''' The value is constrained to be within the range of (minv, maxv)'''
    value = min([value, maxv])
    value = max([value, minv])
    return value

def flatten_list(alist):
    ''' If there are nested lists in this list, flatten them and return a 1D list.'''
    flattened_list = []
    
    def recall(l, list_to_append):
        if type(l) == list or type(l) == tuple:
            for x in l:
                list_to_append += recall(x, [])
        else:
            # item
            list_to_append += [l]
        return list_to_append
    
    return recall(alist, flattened_list)

