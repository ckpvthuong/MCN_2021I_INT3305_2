import numpy
class Node():
  def __init__(self, symbol=None, leftNode=None, rightNode=None):
    self.symbol = symbol
    self.leftNode = leftNode
    self.rightNode = rightNode

class PrefixCodeTree:
  def __init__(self):
    self.HEAD = Node()

  def insert(self,codeword, symbol):
    codeLength = len(codeword)
    point = self.HEAD
    ite = 0

    while True:
      node = self.__createNode(point, codeword[ite])
      if ite + 1 < codeLength:
        ite += 1
        point = node
        continue
      else:
        node.symbol = symbol
        break

  def decode(self, encodedData, datalen):
    bits = self.__toBitArray(encodedData)
    point = self.HEAD
    ite = 0
    output = ""

    while ite < datalen:
      if bits[ite] == 0:
        point = point.leftNode
        if point.leftNode is None and point.rightNode is None:
          output += point.symbol
          ite += 1
          point = self.HEAD
          continue
        else:
          ite += 1
          continue
      else:
        point = point.rightNode
        if point.rightNode is None and point.leftNode is None:
          output += point.symbol
          ite += 1
          point = self.HEAD
          continue
        else:
          ite += 1
          continue

    return output

  def __createNode(self,parent, br):
    rtnode = None
    if br == 0:
      if parent.leftNode is None: 
        newnode = Node()
        parent.leftNode = newnode
        rtnode = newnode
      else:
        rtnode = parent.leftNode
    else:
      if parent.rightNode is None: 
        newnode = Node()
        parent.rightNode = newnode
        rtnode = newnode
      else:
        rtnode = parent.rightNode
    return rtnode

  def __toBitArray(self,bytearr):
    str = ""
    for i in bytearr:
      str+= '{0:08b}'.format(i)
    return list(map(int, list(str)))

  