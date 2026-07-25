'''Write a program to convert roman number into normal numbers. Take input from the user'''

rom=input("Enter the roman number: ")
up=rom.upper()
def convert(up):
    romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans=0
    for words in range(len(up)):
        if words+1 < len(up):
            if romans[up[words]] < romans[up[words+1]]:
                  ans -= romans[up[words]]
            else:
                ans += romans[up[words]]
            
        else:
            ans += romans[up[words]]

    return ans
print(convert(up))