"""docstring"""
balance=500

def is_valid_operation(balance, request):
    result = False
    if request < 0:
        print "Request value must be greater than 0"
    elif balance >= request:
        result = True
    elif request > balance:
        print "balance is not sufficient"
    return result

def output_msg(msg):
    if msg > 0:
        print 'Give {}'.format(msg)


def withdraw(balance, request):
    bank_note_values = [100, 50, 20, 10, 5, 1]
    if is_valid_operation(balance, request):
        for value in bank_note_values:
            while request >= value:
                output_msg(value)
                request -= value
                balance -= value
        balance -= request
    return balance

balance = withdraw(balance,333)


            
            
            
        

