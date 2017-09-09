import pandas as pd
import os

def fileExist(filename, userHandles):
    res = userHandles[userHandles == filename]
    if len(res) >0:
        return res.index[0]
    else:
        return None

path = 'friend-lists/'
print('Loading file names...')
filenames = os.listdir(path)
filenames = [filename[:-4] for filename in filenames]
print('Loading csv...')
c = pd.read_csv("user_id_name.csv")
print('Removing user-id.txt...')
filenames = [filename for filename in filenames if filename.isupper() or filename.islower()]
print('user-name.txt: '+str(len(filenames)))

print('Renaming ...')

for filename in filenames:
    ind = fileExist(filename,c['user_handle'])
    if ind != None:
        targetName = path +str( c['user_id'][ind])+'.txt'
        if os.path.exists(targetName) == False:
            print(c['user_handle'][ind]+' to '+str(c['user_id'][ind]))
            os.rename(path+c['user_handle'][ind]+'.txt',targetName)
        else:
            print('Existing '+targetName+' and remove NAME.txt')
            os.remove(path+c['user_handle'][ind]+'.txt')
       # os.rename(path+c['user_handle'][ind]+'.txt',path+c['user_id'][ind]+'.txt')
