import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(1,2,figsize = (16,8))

Gamma_e = 1; Gamma_f = 1

def plots():

	t0 = -4; t = 0
	X = np.linspace(t0,t,201)
	X,Y = np.meshgrid(X,X)
	N = 4 / (Gamma_e * Gamma_f)
	Z = np.exp((Gamma_f-Gamma_e)/2*X + Gamma_e/2*Y) * (X>t0) * (X<t) * (Y<=X)  + \
		np.exp((Gamma_f-Gamma_e)/2*Y + Gamma_e/2*X) * (Y>t0) * (Y<t) * (X<Y)
	Z **= 2
	Z /= N

	a1 = ax[0].contourf(X,Y,Z, 50)
	ax[0].set_title(r'$p(t_1,t_2)$')
	ax[0].set_xlabel(r'$t_1$')
	ax[0].set_ylabel(r'$t_2$')
	ax[0].set(xticks=[t0,t],xticklabels=[r'$-4$',r'$0$'])
	ax[0].set(yticks=[t0,t],yticklabels=[r'$-4$',r'$0$'])
	

	X = np.linspace(-2,2,401)
	X,Y = np.meshgrid(X,X)

	Z = (Gamma_e**2 + (X+Y)**2) / ((Gamma_e**2/2-X*Y)**2 + (Gamma_e/2 * (X+Y))**2) / ( (X+Y)**2 + Gamma_f**2/4 ) / (4*np.pi)**2

	a2 = ax[1].contourf(X,Y,Z, 30)
	ax[1].set_title(r'$p(\omega_1,\omega_2)$')
	ax[1].set_xlabel(r'$\frac{\omega_1 - \omega_{0}}{\Gamma_f}$')
	ax[1].set_ylabel(r'$\frac{\omega_2 - \omega_{0}}{\Gamma_f}$')
	ax[1].set(xticks=[-1,0,1],xticklabels=[r'$-1$',r'$0$',r'$1$'])#[r'$-\frac{2\pi}{t-t_0}$','0',r'$\frac{2\pi}{t-t_0}$'])
	ax[1].set(yticks=[-1,0,1],yticklabels=[r'$-1$',r'$0$',r'$1$'])#[r'$-\frac{2\pi}{t-t_0}$','0',r'$\frac{2\pi}{t-t_0}$'])
	
	return a1, a2
	
a1, a2 = plots()
c1 = fig.colorbar(a1)
c2 = fig.colorbar(a2)
s = fig.text(.45, .95, r'$\Gamma_e = %3.2f\ \Gamma_f$' % (Gamma_e), fontsize=20)

fig.subplots_adjust(bottom=0.15)
slider1 = Slider(ax = fig.add_axes([0.1, 0.05, 0.8, 0.02]), label='$G_e$', valmin=-.5, valmax=.5, valinit=0)
slider1.valtext.set_text(1)

def update(val: float):
	global Gamma_e, Gamma_f, c1, c2
	Gamma_e = 10 ** (slider1.val); Gamma_f = 1;
	slider1.valtext.set_text('%3.2f' % 10**val)
	c1.remove()
	c2.remove()
	a1, a2 = plots()
	c1 = fig.colorbar(a1)
	c2 = fig.colorbar(a2)
	s.set_text(r'$\Gamma_e = %3.2f\ \Gamma_f$' % (Gamma_e))
	
slider1.on_changed(update);

plt.subplots_adjust(wspace=.5)
plt.subplots_adjust(hspace=.5)
plt.show()
