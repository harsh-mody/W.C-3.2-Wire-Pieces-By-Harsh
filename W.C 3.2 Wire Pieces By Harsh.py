n = int(input("Please Enter The Value Of Length Of Wire : "))
x = int(input("Please Enter The Value Of X,Y or Z in INCREASING ORDER : "))
y = int(input("Please Enter The Value Of X,Y or Z in INCREASING ORDER : "))
z = int(input("Please Enter The Value Of X,Y or Z in INCREASING ORDER : "))
if n % x == 0 and n % y == 0 and n % z == 0:
    maxNumberOfPieces = max(n/x, (n - n/x)/y, (n - n/x - n/y)/z)
    print(maxNumberOfPieces)
elif n % x == 0:
    maxNumberOfPieces = max(n/x, 0)
    print(maxNumberOfPieces)
elif n % y == 0:
    maxNumberOfPieces = max(n/y, 0)
    print(maxNumberOfPieces)
elif n % z == 0:
    maxNumberOfPieces = max(n/z, 0)
    print(maxNumberOfPieces)
elif n % x == 0 and n % y == 0:
    maxNumberOfPieces = max(n/x, (n - (n/x))/y)
    print(maxNumberOfPieces)
elif n % y == 0 and n % z == 0:
    maxNumberOfPieces = max(n/y, (n - (n/y))/z)
    print(maxNumberOfPieces)
elif n % x == 0 and n % z == 0:
    maxNumberOfPieces = max(n/x, (n - (n/x))/z)
    print(maxNumberOfPieces)
else:
    print(-1)