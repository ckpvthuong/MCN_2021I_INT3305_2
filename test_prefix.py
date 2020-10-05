from prefixcodetree import *
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}

codeTree = PrefixCodeTree()
for symbol in codebook:
  codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)
print(message == 'x4x1x2x3x1x1x4x4x2x2')



