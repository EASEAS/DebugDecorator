# DebugDecorator
A python decorator function to enable debugging of function calls


Add the @debug('path/to/log/', bool ) decorator to any function to log arguments.

Logging can be send to the file in a path or it can be sent to stdout if 
no path is specified.

An extra field is given to the decorator that specifies if the return value 
shall be logged
