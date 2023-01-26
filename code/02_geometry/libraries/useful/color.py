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

Created on 28.09.2016

@author: rustr
'''

def convert_rgb_to_grey(r, g, b):
    ''' converts r, g, b values to a single grey value'''
    grey = 0.2989 * r + 0.5870 * g + 0.1140 * b
    # decide yourself if you need to convert grey to integer
    return grey