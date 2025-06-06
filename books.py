class Books:
  def __init__(self,book_id,book_title,publish_date,author,publisher,book_price,purchase_date):
    self.book_id = book_id
    self.book_title = book_title
    self.publish_date = publish_date
    self.author = author
    self.publisher = publisher
    self.book_price = book_price
    self.purchase_date = purchase_date
    
  def __str__(self):
    return f"Book id:{self.book_id} | Book title:{self.book_title} "
  
  def to_dict(self):
    return self.__dict__
  
  @staticmethod  
  def from_dict(data):
    return Books(**data)
