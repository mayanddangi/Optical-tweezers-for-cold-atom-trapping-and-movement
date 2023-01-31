import numpy as np
import tqdm

def gaussian_beam(res1, res2, sigma):
    x, y = np.meshgrid(np.linspace(-1, 1, res1),np.linspace(-1, 1, res2))
    gauss = np.exp(-0.5*(1/sigma)*(x**2+y**2))
    return gauss
    
def GS(source, target, retrived_phase, it):
    A = np.exp(retrived_phase*1j)
    for i in tqdm.tqdm(range(0,it)):
        B = np.abs(source)*np.exp(1j*np.angle(A))
        C = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(B)))
        D = np.abs(target)*np.exp(1j*np.angle(C))
        A = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(D)))
        
    return np.angle(A)