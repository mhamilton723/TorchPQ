from .BaseIndex import BaseIndex

class IVFPQRIndex(BaseIndex):
  def __init__(self):
    super(IVFPQRIndex, self).__init__()

  def train(self, x):
    pass
  
  def encode(self, x):
    pass

  def decode(self, x):
    pass
  
  def add(self, x, ids=None):
    pass

  def remove(self, ids=None, address=None):
    pass

  def search(self, queries, k=1):
    pass