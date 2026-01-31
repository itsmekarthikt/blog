def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_unique_substring("abcdabcbb"))  # Output: 3

"""---------------------------------------------------------------------------------------------------------------"""
def fibnaci(n):

    if n<0:
        return "Invalid number"
    
    elif n==0:
        return 0

    
    elif n==2 or n==1:
        return 1
    
    else:
        return fibnaci(n-1)+fibnaci(n-2)
    

print(fibnaci(9))

"""---------------------------------------------------------------------------------------------------------------"""

def sort_lis(lst):
    l=[]
    for i in lst:
        c=''
        for j in i:
            if j.isdigit():
                c=c+j
        l.append((int(c),i))
        l.sort(key=lambda x:x[0])

    return [i[1] for i in l]

    

        



lt=['sam200','karthik0','gokul300']
print(sort_lis(lt))

"""---------------------------------------------------------------------------------------------------------------"""

def string_counter(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i] +=1
        else:
            dic[i]=1

    return(dic)

print(string_counter("karthik"))

def sort_by_digit(input):
    l=[]
    for i in input:
        c=''
        for j in i:
            if j.isdigit():
                c=c+j

        l.append((int(c),i))
        l.sort(key=lambda x:x[0])

    return [i[1] for i in l]


print(sort_by_digit(['karthik200','gokul300','dhanvika400']))


s="karthik"
s.upper()
print(s)
            



                



















