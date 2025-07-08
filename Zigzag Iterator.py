from collections import deque
class ZigzagIteratork:
  def __init__(self,vectors):
    self.q=deque()
    self.vectors=vectors
    for i in range(len(self.vectors)):
      if self.vectors[i]:
        self.q.append((i,0,len(self.vectors)))

  def next(self):
    ind,st,end=self.q.popleft()
    if st+1<end:
      self.q.append((ind,st+1,end))
    return self.vectors[ind][st]

 def hasnext(self):
   return len(self.q)!=0
