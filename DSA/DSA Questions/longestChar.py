'''Write a code to print the continous words fromm the list with are same in all the string inside a list'''

ls=[]
def string(strs):
    ans = ""
    default= strs[0]
    for i in range(len(default)):
        char = default[i]
        for words in strs:
            if i >= len(words) or words[i] != char:
                return ans

        ans += char

    return ans

ran = int(input('Enter how many words in list: '))
for i in range(ran):
    a=input("Enter the words: ")
    ls.append(a)

print(string(ls))