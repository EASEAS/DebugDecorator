import functools

path = "/home/erik/Documents/python/"

def debug(filePath=None,returnValueLog=False):
    
    #function to log output to file or stdout
    #if no path is given for log, log is stdout
    def logOutput(logFilePath=None,stringToLog=[]):
        if (logFilePath == None):
            print(''.join(stringToLog))
        else:    
            f = open(logFilePath + "log.txt", 'a')
            f.write(''.join(stringToLog))
            f.write('\n')
            f.close()
    def decorator(func):

        #enable debugging of wrapper metadata
        @functools.wraps(func)
        
        #wrapper for arbitrary argument function
        def wrapper(*args,**kwargs):
            
            logOutput(filePath, ['Trace: calling function ',\
                                    func.__name__,' with arguments: args(',\
                                    str(args),'), kwargs (' ,str(**kwargs), ')' ])

            #get return from function passed to decorator
            functionReturn = func( *args, **kwargs)
            
            #Add return value from function to log if needed 
            if (returnValueLog):
                logOutput(filePath,['Returned value: ',str(functionReturn)])
            return functionReturn
        return wrapper
    return decorator

def complexFunc(*args, **kwargs):
    ret = 1
    for a in args:
        ret *= a
    return ret 
@debug (None, True)
def simpleFunc(value):
    return value**2


x = complexFunc(1,3,7,10,123)
y = simpleFunc(x)
