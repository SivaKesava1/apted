import unittest
import json
import os

from helpers import Tree

import collections
import pdb



x =  {
        "testID" : 1,
        "t1" : "{f{a}{e{c{b}}{d}}}",
        "t2" : "{f{a}{c{e{b}{d}}}}",
        "d" : 2
    }

x = collections.OrderedDict(sorted(x.items()))
child_trees = []
for k,v in x.items():
    if isinstance(v,list):
        print("List")
    elif isinstance(v,dict):
        print("Dict")
    else:
        child_trees.append(Tree.from_text("{"+str(k)+"{"+str(v)+"}"+"}"))    
        
    

pdb.set_trace()
tu = tuple(child_trees)

tree1 = Tree.from_text("{f{a}{e{c{b}}{d}}}")
t = Tree("Root",tree1)
t = Tree("Root",tu)
tree2 = Tree.from_text("{f{a}{e{c{b}}{d}}}")

# apted = APTED(tree1, tree2, )
# ted = apted.compute_edit_distance()
# mapping = apted.compute_edit_mapping()
