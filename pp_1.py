string='''mother theresa institute of computer applications ...!!!'''
wordslist=string.split(' ')
print(wordslist)
wordslist=[i.strip("\n") for i in wordslist]
print(wordslist)


ans={i:len(i) for i in wordslist}
print(ans)
