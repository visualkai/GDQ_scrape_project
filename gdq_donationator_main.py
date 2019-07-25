import requests as requests, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s : %(message)s')

main =[] 		#stores page data to compare to alt
alt=[0]			#stores page data to compate to main, initailized as [0] to prevent the program from ending too soon
pageturner = 1  #tracks what gdq page currently on
altr = 1 		#tracks where to hold page info

def fileSave(entries):
    """Appends file with selected text""" 
    fs = open('GDQ_donation_pull.txt', 'ab')
    for item in entries:fs.write(item.encode()+('\r\n').encode())
    fs.close()
    

while main != alt:
    if alt == 0:
        del alt[0]

    pagepull = requests.get('https://gamesdonequick.com/tracker/donations/?page=%d' % pageturner)
    pagepull.raise_for_status()
    tempSoup = bs4.BeautifulSoup(pagepull.text, features='lxml')
    type(tempSoup)
    stew = tempSoup.select('td')
    newHtml = []
    for line in stew:
        bowl = line.getText()[1:-1]
        newHtml.append(bowl)

    if altr == 1:
        main = newHtml
    elif altr == -1:
        alt = newHtml
    else:
        Print('Error with Alternator')

    altr *= -1/
    pageturner += 1
    fileSave(newHtml)
input('Enter To Close')


