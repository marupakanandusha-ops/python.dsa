class Queue:
  def __init__(self,cap=5):
    self._a=[None for _ in range(cap)]
    self._front=0
    self._rare=-1
    self._c=0
  def peek(self):
    if self._c==0:
      return "No elements"
    return self._a[self._front]
  def enqueue(self,data):
    if self._c==len(self._a):
      print("overflow")
      return
    self._a[self._c]=data
    self._c+=1
  def rare(self):
    return self._a[self._c-1]
  def dequeue(self):
    if self._c==0:
      print("underflow")
      return 
      temp=self._a[self._front]
      for i in range(1,self._c):
          self._a[i-1]=self._a[i]
      self._a[self._c-1]=None
      self._c-=1
      return temp 
  def isempty(self):
    return self._c==0 
  def isfull(self):
    return self._c==len(self._a) 


    
queue = Queue() 
queue.enqueue(30)
queue.enqueue(10)
queue.enqueue(70)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.isempty()
queue.isfull()
print(queue.peek())
print(queue.rare())