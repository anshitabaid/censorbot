from __future__ import print_function
import sys
from PIL import Image
import random

'''infile = sys.argv [1:][0]'''
for i in range (1,25):
    try:
        file = "img" + str(i) + ".jpg"
        im= Image.open ('data/'+file)
        left=random.randint (0, im.size[0])
        upper=random.randint (0, im.size[1])
        '''
        right=random.randint (0, im.size[1])
        lower=random.randint (0, im.size[0])
        print (left, upper, right, lower)
        '''
        '''box=(left, left, right, right)'''
        offset1 = random.randint (1,im.size[0]-left)
        offset2 = random.randint (1, im.size[1]-upper)
        box=(left, upper, left+offset1, upper+offset2)
        color=(255,40,40)
        im.paste(color, box)
        '''im.show()'''
        im.save ('modified/'+file)
    except IOError:
        print ("Cannot read file img" + str(i) + '.jpg')
        