"""docstring"""
balance=500
def withdraw(balance,request):
    pnv = [100,50,20,10,5]
    if request > balance:
        print 'Balance is not sufficient'
        return
    
    for e in pnv:
        while request >= e:
            print 'Give ' + str(e)
            request -= e
            balance -= e
    if request > 0:
        print 'Give ' + str(request)
    balance -= request
    return balance

balance = withdraw(balance,500)
print "balance: " + str(balance)

            
            
            
        

