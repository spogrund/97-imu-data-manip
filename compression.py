import zlib
import sys
import binascii
import gzip
import os


def compresshexarray(anarray):
   z = anarray
   x = []
   for i in z:
      x.append(zlib.compress(i))
 
   return x 


def testsize(anarray):
   x = 0
   for i in anarray:
      x  = x + sys.getsizeof(i)
   return x   
    
def hexarray (anarray):
   z = anarray
   x = []
   for i in z:
      x.append(float2hex(i))
   return x   
    
    
def float2hex(s):
   return binascii.hexlify(s)

def hex2float(h):
   return binascii.unhexlify(h)

def compressgz(x):
   os.system('gzip --keep ' + x)
  # with open(os.path.join(os.path.dirname(__file__), x), 'rb') as src, gzip.open(os.path.join(os.path.dirname(__file__), y), 'wb') as dst:
      #   dst.writelines(src)   
         
def uncompress(x):
   #with gzip.open(os.path.join(os.path.dirname(__file__), x), 'rb') as src, open(os.path.join(os.path.dirname(__file__), y), 'w') as dst:
       #  dst.writelines(src)
   filename = '/Users/jakeburditt/Desktop/3097/'+x
   os.system('gunzip --keep ' + x)