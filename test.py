from numpy import load

data = load('calibration.npz')
lst = data.files
for item in lst:
    print("IN ITEM "+item+" "+"\n")
    print("IN DATA "+str(data[item])+" "+"\n")