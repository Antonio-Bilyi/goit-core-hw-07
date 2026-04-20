from functools import wraps

def input_error(func):
    @wraps(func)

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError:
            return 'Give me name and phone please!'
        
        except KeyError:
            return 'OOOOps!'
        
        except IndexError:
            return 'Enter the argument for the command'
        
        except AttributeError:
            return 'Contact not found'
    
    return inner