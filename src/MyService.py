import qi

class MyService:
  def __init__(self, *args, **kwargs):
    #define a signal 'onBang'
    self.onBang = qi.Signal()

  #define a bang method that will trigger the onBang signal
  def bang(self):
    #trigger the signal with 42 as value
    self.onBang(42)