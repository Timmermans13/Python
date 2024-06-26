coverage = {
    "length" : False,
    "in_array" : False,
    "not_in_array" : False,
}

def linearsearch(arr, x):
   for i in range(len(arr)):
      coverage["length"] = True
      if arr[i] == x:
         coverage["in_array"] = True
         return i
   coverage["not_in_array"] = True
   return -1

def resetDic():
    for i in coverage.keys():
        coverage[i] = False

def printCov():
    for branch, hit in coverage.items():
        if hit:
            print(branch, "was hit")
        else:
            print(branch, "was not hit")
    resetDic()

def firstTest():
   arr = ['t','u','t','o','r','i','a','l']
   x = 'a'
   print("element found at index "+str(linearsearch(arr,x)))

def secondTest():
   arr = ['t','u','t','o','r','i','a','l']
   x = 'z'
   result = linearsearch(arr,x)
   assert(result == -1)
   print("element found at index " + str(result))
   

firstTest()
secondTest()

printCov()
