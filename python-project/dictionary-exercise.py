dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]

count ={True:0, False:0}
falsecount = 0
truecount = 0

for i in range(len(dabools)):
    if dabools[i] == True:
        truecount += 1
    else:
        falsecount += 1

count[True] = truecount
count[False] = falsecount

print(count)