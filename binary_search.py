class BinarySearch(list):
  
    
  def __init__(self,length,b):
      super(BinarySearch,self).__init__()
      
      for elem in range(1, length+1):
          self.append(elem * b) 
            
      self.length=len(self)
      
  def search(self, item):
      first = 0
      last = len(self)-1
      found = False
      counter=0
      
  
      while first <= last and not found:
            midpoint = (first + last) // 2
            if self[midpoint] == item:
                found = True
            else:
                counter += 1
                if item < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

               
                
      return {'count': counter, 'index': midpoint}
      
  