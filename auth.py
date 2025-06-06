class Authentication:
  def __init__(self):
    self.__admin = 'admin'
    self.__password = 'password'
    
  def check_authentication(self,admin,password):
    if self.__admin == admin and self.__password == password:
      return True
    return False
  