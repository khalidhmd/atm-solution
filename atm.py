"""docstring"""
balance=500

def is_valid_operation(balance, request):
    result = False
    if request < 0:
        print "Request value must be greater than 0"
    elif balance>=request:
        result=True
    elif request > balance:
        print "balance is not sufficient"
    return result


def withdraw(balance, request):
    pnv = [100,50,20,10,5]
    if is_valid_operation(balance, request):
        for e in pnv:
            while request >= e:
                print 'Give ' + str(e)
                request -= e
                balance -= e
        if request > 0:
            print 'Give ' + str(request)
        balance -= request
    return balance

balance = withdraw(balance,-1)
print "balance: " + str(balance)

            
            
            
        

