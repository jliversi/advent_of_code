# i know that doing this with that tree is silly
# i just wanted to make a tree in python

from math import floor

inputs = []

with open('input.txt','r') as f:
  for l in f:
    inputs.append(l)

class BTreeNode:
  def __init__(self, val, parent=None, left=None, right=None):
    self.val = val
    self.parent = parent
    self.left = left
    self.right = right

  def addRight(self,right):
    self.right = right
    right.parent = self

  def addLeft(self,left):
    self.left = left
    left.parent = self

  def navToVal(self,nav_string, vert=True):
    if vert:
      bottom = 'F'
      top = 'B'
    else:
      bottom = 'L'
      top = 'R'
    cur_node = self
    for char in nav_string:
      if char == bottom:
        cur_node = cur_node.left
      else:
        cur_node = cur_node.right
    return cur_node.val

def build_tree(start,end,parent=None):
  root = BTreeNode(range(start,end + 1),parent)
  if len(root.val) > 1:
    mid = floor((end + start)/2)
    root.left = build_tree(start,mid,root)
    root.right = build_tree(mid+1,end,root)
  else:
    root.val = start

  return root


VERT_TREE = build_tree(0,127)
HORZ_TREE = build_tree(0,7)

def find_id(bp):
  row_data = bp[:7]
  col_data = bp[7:]

  row = find_row(row_data)
  col = find_col(col_data)
  return (row * 8) + col

def find_row(row_data):
  return VERT_TREE.navToVal(row_data)

def find_col(col_data):
  return HORZ_TREE.navToVal(col_data, False)

ids = set()
for ele in inputs:
  ele_id = find_id(ele.strip('\n'))
  ids.add(ele_id)

missing = []
for i in range(0,1024):
  if i not in ids:
    missing.append(i)

print(missing)