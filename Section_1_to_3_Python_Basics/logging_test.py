from logger import logging

def add(a,b):

    logging.debug("the addition operation is taking place")
    return a + b

logging.debug("The addition funciton is called")
add(10,15)