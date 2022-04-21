import random
import time

artists = ['vanessa','joshua','skrillex','ved', 'brackets','footballs','coding','chairs','shofas','fungs']
Vsongs = ['b','w','e','g','wineers','n','s','t','y','u','i','p']
Jsongs = ['q','w','e','r','y','u','o','t','a','s']
Ssongs = ['q','w','e','r','y','u','o','t','a','s']
VedSongs = ['q','w','e','r','y','u','o','t','a','s']
Bsongs = ['q','w','e','r','y','u','o','t','a','s']
Fsongs = ['q','w','e','r','y','u','o','t','a','s']
Csongs = ['q','w','e','r','y','u','o','t','a','s']
ChairSongs = ['q','w','e','r','y','u','o','t','a','s']
ShofaSongs = ['q','w','e','r','y','u','o','t','a','s']
FungSongs = ['q','w','e','r','y','u','o','t','a','s']
currentartist = random.choice(artists)

def choices():
    if currentartist in ['vanessa']:
        currentsongs = [random.choice(Vsongs),random.choice(Vsongs)]
    elif currentartist in ['joshua']:
        currentsongs = [random.choice(Jsongs),random.choice(Jsongs)]
    elif currentartist in ['skrillex']:
        currentsongs = [random.choice(Ssongs),random.choice(Ssongs)]
    elif currentartist in ['ved']:
        currentsongs = [random.choice(VedSongs),random.choice(VedSongs)]
    elif currentartist in ['chair']:
        currentsongs = [random.choice(ChairSongs),random.choice(ChairSongs)]
    elif currentartist in ['brackets']:
        currentsongs = [random.choice(Bsongs),random.choice(Bsongs)]
    elif currentartist in ['footballs']:
        currentsongs = [random.choice(Fsongs),random.choice(Fsongs)]
    elif currentartist in ['fungs']:
        currentsongs = [random.choice(FungSongs),random.choice(FungSongs)]
    elif currentartist in ['shofas']:
        currentsongs = [random.choice(ShofaSongs),random.choice(ShofaSongs)]
    elif currentartist in ['coding']:
        currentsongs = [random.choice(Csongs),random.choice(Csongs)]

    return currentsongs

currentsongs = choices()
songplaying = random.choice(currentsongs)
currentsongs.remove(songplaying)
print('now playing:',songplaying)
time.sleep(5)
songplaying = random.choice(currentsongs)
print('now playing:',songplaying)
