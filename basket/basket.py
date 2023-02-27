


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overeided, as necessary
    """

    def __init__(self, request): #__init__ runs the function everytime the user goes to a new page 
# Using session to link the current user to a basket.  
        self.session = request.session
        basket = self.session.get('skey') #if the session key (skey) is already in the basket table 
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':1231231}  #create a new session skey in the basket table
        self.basket = basket