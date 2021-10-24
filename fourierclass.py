import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft
import warnings
warnings.filterwarnings("ignore")




def fourier(anarray = [-8.801926e-02,1.5987283,1,0,0,0,0,0] ):
    y = anarray
    fft_vals = fft(y)
    freqs = fftfreq(len(y))
    plt.figure(1)
    plt.plot(freqs, fft_vals, label = " not true fft")
    #plt.show()    
    return fft_vals
#print(fourier())

#def fourierpadded(anarray = [0,1,1,0,0,0,0,0] ):
#    x = anarray
#    N = len(x)
#    v_padded = [x, zeros(7*N)]
#    fft_vals = fft(v_padded)
#    freqs = fftfreq(len(v_padded))
#    plt.figure(1)
#    plt.plot(freqs, fft_vals, label = " not true fft")
#   #plt.show()    
#    return fft_vals
   
   
def invfourier(anarray):
    
    y = anarray
    inverse = np.real(ifft(y))
  
    n = inverse.tolist()
    
  #  inversefouriervals = np.array(ifft(y),dtype=float)    
 #   x = inversefouriervals.real
    return n
    

#def invfourierpadded(anarray):
#    x = anarray
  #  inverse = np.real(ifft(x))
#    n=len(inverse)
#    i =(n/8)+1
#    j = int(i)
#    return inverse[0:j]
    
    


    
    
    
    
    
#n = 1000
#Lx = 100
#omg = 2.0*np.pi/Lx
#x = np.linspace(0,Lx,n)
#y = np.cos(5*omg*x)

#freqs = fftfreq(n)
#mask = freqs>0
#fft_vals = fft(y)
#fft_theoretical = 2.0*np.abs(fft_vals/n)

#plt.figure(1)
#plt.plot(freqs, fft_theoretical, label = "true fft")
#plt.show()
#plt.close('all')