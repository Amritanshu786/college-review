def pyramid():
    even = 1
    space =4
    for i in range(1,6):
        k = 0
        x =0
        for j in range(1,even+1):
            if(j<=i):
                k= k+1
            else:
                k = k - 1
            if (k%2==0 or k==1 and x!=k):
                print(k,end="")
        print()
        even = even + 2
pyramid()
