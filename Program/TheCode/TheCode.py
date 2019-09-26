from PIL import Image
import os
#import sys
import time

frames = []
GIFSettingsFile = open("GIFSETTINGS.txt", 'r')

GIFName = GIFSettingsFile.readline()
GIFName = GIFName[0:len(GIFName) - 1]
print("Filnavn sat til: " + GIFName)

GIFDuration = GIFSettingsFile.readline()
GIFDuration = GIFDuration[0:len(GIFDuration) - 1]
print("Duration sat til: " + GIFDuration)

GIFLoop = GIFSettingsFile.readline()
print("Loop setting sat til: " + GIFLoop)
GIFSettingsFile.close()

directory = os.fsencode("Images to GIF")

for file in os.listdir(directory):
    frames.append(Image.open("Images To GIF/" + os.fsdecode(file)))
    #sys.stdout.write('\r' + str(len(frames)) + " / " + str(len(os.listdir(directory))))

time.sleep(2)
print("\nFærdige med at hente filer")
print("Begynder convertering til GIF (Dette kan godt tage 1 min)")
frames[0].save(GIFName + ".gif",
               format='GIF',
               append_images = frames[1:],
               save_all = True,
               duration = int(GIFDuration),
               loop = int(GIFLoop))

print("\nDONE (Lukker om 5 sec)")
time.sleep(5)
