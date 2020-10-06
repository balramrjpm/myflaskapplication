'''
Using pytest we are testing
'''

from mywebapp import indexpage

def test_mytest():
    assert indexpage() == "Wel Come"