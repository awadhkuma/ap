ln = []
while True:
    a = input("Enter a number (or No to stop): ")
    if a == "No":
        ln.sort()
        print(ln)
        print(ln[-2])
        break
    else:
        ln.append(int(a))