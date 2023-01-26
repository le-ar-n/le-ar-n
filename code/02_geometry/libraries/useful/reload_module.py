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

Created on 16.09.2016

@author: kathrind
'''
import sys

def import_or_reload(module_name, *names):
    """ # use instead of: from dfly_parser import parseMessages
    import_or_reload("dfly_parser", "parseMessages")
    """
    
    if module_name in sys.modules:
        reload(sys.modules[module_name])
    else:
        __import__(module_name, fromlist=names)

    for name in names:
        globals()[name] = getattr(sys.modules[module_name], name)

def reload_mas_lib():
    ''' Reload all mas_lib modules'''
    
    modules_to_pop = []
    for mod in sys.modules:
        if mod[:7] == "mas_lib":
            modules_to_pop.append(mod)
    
    for mod in modules_to_pop:
        if mod in sys.modules:
            sys.modules.pop(mod)
            print "%s unloaded." % mod
