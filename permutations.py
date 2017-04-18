#Code wars Kata, goal to find all the permutations of a string and return them as a list
# I know there is a shortcut for this, I'm also sure I used the longest way possible.


def permutations(str):
    strings = []
    perm = len(str)
    x = perm-1
    def perm(l):     #determines number of possible permutations for a l length string
        x = 1
        for i in range(l,0,-1):
            x = x * i
        return x
    def perms(l):  #determines the number of purmutations of an 1 length + 2 lenth etc up to l length
        x = 0
        for i in range (l,0,-1):
            x = x + perm(i)
        return x

    for i in range(len(str)):
        strings.append(str[:i+1])
    for i in range(perms(len(str))):
        if i > 0:
            try:  # if there are double letters, the possible combinations are too long.
                it = strings[i]
            except IndexError:
                pass
            sl = it[:-1]
            new = it[-1:]
            for j in range(len(it)):
                newst = sl[:j]+new+sl[j:]
                if newst not in strings:
                    strings.append(newst)
    permutations = []
    for i in strings:
        if len(i) == len(str):
            permutations.append(i)
    return permutations

    #The following is all failed trials.

    #for i in range(len(strings)):
        #it = strings[i]
        #for j in range(len(it)+1):
    #        new = it[:j]+it[j+1:]
    #        print new
            #
            #new = it[:j]+it[j+1:]
            #print new
            #for k in range(len(new)+1):
            #    print new[:k]+str[j]+new[k:]



        #for j in range(len(new)):
        #    nlst = []
        #    nlst.append(new[:j]+new[j+1:])
        #    for k in nlst:
        #        print k
        #for j in range(len(new)):
        #    print new[:j]+str[i]+new[j:]


    #print strings




#Test run
    #for i in range(len(str)):
    #    new = str[:i]+str[i+1:]
    #    for j in range(len(new)+1):
    #        print new[:j]+str[i]+new[j:]













str = "abc"
print permutations(str)
#permutations('a'


#); # ['a']
#permutations('ab'); # ['ab', 'ba']
#permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# 1234, 1243, 1423 1432,
#ab = ab, ba
#abc = abc, acb, bac, bca, cab, cba
#abcd = abcd, abdc,
#>>> hash = "355879ACB6"
#>>> hash = hash[:4] + '-' + hash[4:]
#>>> print hash
#3558-79ACB6
