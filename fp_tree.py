import FPgrowth
rootNode = FPgrowth.treeNode('pyramid',9, None)
rootNode.children['eye']=FPgrowth.treeNode('eye', 13, None)
rootNode.children['phoenix']=FPgrowth.treeNode('phoenix', 3, None)
rootNode.disp()