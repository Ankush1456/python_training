def subseq(processed, unprocessed):
    if len(unprocessed) ==0:
        if len(processed) ==0:
            return 0
        return 1
    ch = unprocessed[0]

    left= subseq(processed+ch, unprocessed[1:] )
    right = subseq(processed, unprocessed[1:])

    return left + right

print(subseq("","abc"))



#def ret_subseq(processed, unprocessed):
 #   if len(unprocessed) ==0:
  #      if len(processed) ==0:
   #         return []
        #return [processed]
    #ch = unprocessed[0]
    #acc =[]

    #acc.extend(ret_subseq(processed+ch, unprocessed[1:] ))
    #acc.extend(ret_subseq(processed, unprocessed[1:]))

    #return acc

#print(ret_subseq("","abc"))

