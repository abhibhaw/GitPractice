def git_opeation():
 print("I am adding example.py file to the remote repository.")
git_opeation()
# for print somthing
print("hello world")   

def num(l):
    number=[]
    for i in range(1,len(l)+1):
        a=l.pop()
        number.append(a)
    return number

n=list(range(1,5))
print(num(n))
