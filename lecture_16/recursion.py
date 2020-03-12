#def fibo(n):

   # if n<2:
     #   return n

   # first = fibo(n-1)
   # second = fibo(n-2)
   # return first + second


#print (fibo(5))

#def subseq(processed, unprocessed):

 #   if len(unprocessed) ==0:
  #      print(processed)
   #     return

    #ch = unprocessed[0]
    #subseq(processed + ch, unprocessed[1:])
    #subseq(processed , unprocessed[1:])

#subseq("", "abc")

def permute(processed, unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return

    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        permute(processed + ch, rec_unprocessed)

permute("", "abc")








