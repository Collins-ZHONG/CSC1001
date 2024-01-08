def isAnagram(s1, s2):
    
    """
    Write a function that checks whether two words are anagrams. 
    Two words are anagrams if they contain the same letters.
    You can write a program to change the 'result' to Ture or False 
    For example, silent and listen are anagrams, and the result = True.
    """
    
    # initialize result
    result = True

    ############## Start your codes ##############
    s1=str(s1)
    s2=str(s2)
    l1=[]
    l2=[]
    for s11 in s1:
        l1.append(s11)
        #print(l1)############# check ########
    l1.sort()
    for s22 in s2:
        l2.append(s22)
    l2.sort()
    
    if l1!=l2:
        result=False
    ##############  End your codes  ##############

    return result
        

if __name__ == '__main__':

    # Example test cases
    # Note: there will be more test cases in scoring
    s1 = ["listen", "car", "anagram", "a", "ttttttta"]
    s2 = ["slient", "rat", "nagaram", "an", "tatttttt"]
    
    for i in range(5):
        print(isAnagram(s1[i], s2[i]))

    # The display of output will be:
    # True
    # False
    # True
    # False
    # True
