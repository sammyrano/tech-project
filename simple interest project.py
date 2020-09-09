def invest(principal, noOfYear):

    if (noOfYear==1):
        y= 'year'
    else:
        y= 'years'
        
    if noOfYear==3 or noOfYear==4 or noOfYear==5 :
        rate = 2.5

    elif noOfYear > 10:
        rate=5

    elif noOfYear < 10 :
        rate = 3.5

    else: 
        rate = 1.5

    interest= (principal*rate*noOfYear)/100
    
    print('Your interest with us after ', noOfYear, y , ' is ', interest, ' and total payable amount is ', interest+principal )

invest(11000, 8)
