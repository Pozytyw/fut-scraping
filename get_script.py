# function for get script from file

def getScript(path):
    file = open(path)
    script = file.read()
    file.close()
    return script
