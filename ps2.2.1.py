
import urllib2

#f = open("directory","w")
f = open("fcc.txt","w")
f.write("*****")
f.close()
#f = open("C:/Users/yourusername/Desktop/fcc.txt", "a")
f = open("fcc.txt", "a") 
#constants
namesign = '<td scope="row" id=name-cell-'
emailsign = '<td style="padding-top: 8px;" id=email-cell-'
emailsignend = '><img alt="'
phonesign = 'td id=phone-cell-'
powsign = '<td id=dept-cell-'
contchec = True
letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
fsearchurl = "https://www.fcc.gov/about-fcc/finding-people-fcc?name="
for x in range(0, len(letterlist)):
    s1 = letterlist[x]
    for y in range(0, len(letterlist)):
        contchec = True
        s2 = letterlist[y]
        urap = (str(s1) + str(s2))
        tfsearchurl = fsearchurl + urap
        print(tfsearchurl)
        #response = urllib2.request.urlopen(tfsearchurl)
        response = urllib2.urlopen(tfsearchurl)
        html = response.read()

        polishtml = str(html)
    
        polishtml = polishtml[41677:]
        contcount = 0
        while(contchec == True):
            namecheck = namesign + str(contcount) + ">"
            emailcheck = emailsign + str(contcount) + emailsignend
            phonecheck = phonesign + str(contcount) + ">"
            powcheck =  powsign + str(contcount) + ">"
            if(namecheck in polishtml):
                
                nametcount = polishtml.find(namecheck)
                emailtcount = polishtml.find(emailcheck)
                phonetcount = polishtml.find(phonecheck) 
                powtcount = polishtml.find(powcheck)
                print(nametcount, emailtcount, phonetcount, powtcount, contcount)
                contcount = contcount + 1
            else:
                contchec = False
            
            
        f.write(polishtml)
        print("___________________________")
f.close()
        
       
