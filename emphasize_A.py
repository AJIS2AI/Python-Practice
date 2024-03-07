def solution(myString):
    myString = myString.lower()
    myString = myString.replace('a', 'A')
    return myString

str = input("Enter the string.")
print(solution(str))
