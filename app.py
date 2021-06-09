import requests

url = input('Input link (the last part): ')
url = url.lower()
printfail = input('Do you want to print failed attempts (y/n)? ')
printfail = printfail.lower()
correcturl = False
truelink = ''

def permute(inp):
    possble = []
    n = len(inp)
  
    mx = 1 << n
  
    inp = inp.lower()
     
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
  
        temp = ""
        for i in combination:
            temp += i
        possble.append(temp)
    return possble

posurls = (permute(url))

for posurl in posurls:
    page = requests.get("https://discord.com/api/v9/invites/" + posurl + "?with_counts=true&with_expiration=true")
    if (page.status_code == 404):
        if (printfail == 'y'):
            print(f'{posurl} - Failed')
    elif (page.status_code == 200):
        print(f'{posurl} - Success!')
        correcturl = True
        truelink = f'\nhttps://discord.com/invite/{posurl} is the right url!'
        break

if (correcturl == True):
    print(truelink)
else:
    print("Hmmmm.... This doesn't seem like a discord link... Check the link that you've inputed.")
