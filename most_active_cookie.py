import sys

def mostActive(filename,spec,time):
    cookieCount = []

    cookies = open(filename,'r')
    for line in cookies:
        words = line.split(',')
        if time in words[1]: #Date match
            found = False
            for i in range(0,len(cookieCount)): #check if we have already found this cookie
                if cookieCount[i][0] == words[0]:
                    cookieCount[i][1] = cookieCount[i][1] + 1
                    found = True
                    break
            
            if not found: #if first time seeing the cookie
                cookieCount.append([words[0],1])

    mostFreq = 0
    for i in range(0,len(cookieCount)): #find largest number of cookie appearances
        if cookieCount[i][1] > mostFreq:
            mostFreq = cookieCount[i][1]

    for i in range(0,len(cookieCount)): #print all cookies that have most appearances
        if cookieCount[i][1] == mostFreq:
            print(cookieCount[i][0])

if __name__ == "__main__":

    if (len(sys.argv) != 4):
        print('Error: incorrect number of args')
        exit()

    mostActive(sys.argv[1],sys.argv[2],sys.argv[3])



#python most_active_cookie.py cookie_log.csv -d 2018-12-08