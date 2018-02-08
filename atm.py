"""docstring"""

def withdraw(request):
    pnv = [100,50,20,10,5]
    balance = 500
    if request > balance:
        print 'Balance is not sufficient'
        return
    
    for e in pnv:
        while request > e:
            print 'Give ' + str(e)
            request -= e
            balance -= e
    if request > 0:
        print 'Give ' + str(request)
    balance -= request
    print
    print 'Your balance is: ' + str(balance)

withdraw(127)

            
            
            
        

