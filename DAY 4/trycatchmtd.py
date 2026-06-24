fname = input("Enter a file name you want open")
f = open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/test.txt","+r")
f.write("I love coding\nI love Python")
#f.seek(0)
print(f.read())
print("File Name is:",f.name)
print(f.tell())
print(f.closed)
try:
    with open("/workspaces/ACE-BOOTCAMP-JUN-2026/DAY 4/test.txt",'r') as f:
        print(f.read())
except Exception as e:
    print(e)

    
    print(f.closed)