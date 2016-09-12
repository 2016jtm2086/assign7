str1 = raw_input(" Provide string srting : ") # providing the string
word_freq = {}
from collections import Counter

print ("top 3 frequent words:")
lis = sorted(Counter(str1.split()).items(),key=lambda (i,j):(-j,i))[:3]
for word,freq in lis:
    print word, freq #printing top three repeatin word

    def perms(s):       # calculating permutations of different strins
            if(len(s)==1): return [s]
            result=[]
            for i,v in enumerate(s):
                result += [v+p for p in perms(s[:i]+s[i+1:])]
            return result
    print('\n'.join(perms(word))) #printing the result
