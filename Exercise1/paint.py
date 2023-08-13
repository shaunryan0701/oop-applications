class Paint:
    
    def __init__(self, buckets, colour):
        self.buckets = buckets
        self.colour = colour

    def total_price(self):
        if self.colour == 'white':
          return self.buckets * 1.99
        else:
          return self.buckets * 2.19