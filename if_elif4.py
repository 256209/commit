def bill(slices):
    print("${}".format(120.00* slices if slices %2 == 0 else 123.00 * slices))
slice = int(input())
bill(slice)