def two_fer(name="you"):
    
    if name:
        return "One for {x}, one for me.".format(x=name)
    elif not name:
        return "One for {x}, one for me.".format(x='you')
