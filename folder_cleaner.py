
# print(chr(ord('e')+1))

import os

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove('hh.py')

createFolder('Images')
createFolder('Docs')
createFolder('Media')
createFolder('Songs')
createFolder('Others')


imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt", ".docx", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

songExts = [".mp3"]
songs = [file for file in files if os.path.splitext(file)[1].lower() in songExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in songExts) and os.path.isfile(file):
        others.append(file)



move('Images', images)
move('Docs', docs)
move('Media', medias)
move('Others', others)
move('Songs', songs)

