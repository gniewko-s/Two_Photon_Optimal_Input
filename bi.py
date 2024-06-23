import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(1,2,figsize = (16,8))

Gamma_e = 1; Gamma_f = 1

def plots():

	X = np.linspace(-.2,1.2,141)
	X,Y = np.meshgrid(X,X)
	Z = np.exp((Gamma_f-Gamma_e)/2*X + Gamma_e/2*Y) * (X>0) * (X<1) * (Y<X) * (Y>0)

	ax[0].contour(X,Y,Z, 50)
	ax[0].set_title(r'$p(t_1,t_2)$')
	ax[0].set_xlabel(r'$t_1$')
	ax[0].set_ylabel(r'$t_2$')
	ax[0].set(xticks=[0,1],xticklabels=[r'$t_0$',r'$t$'])
	ax[0].set(yticks=[0,1],yticklabels=[r'$t_0$',r'$t$'])


	X = np.linspace(-2,2,401)
	X,Y = np.meshgrid(X,X)

	Z = (Gamma_f**2 + (X+Y)**2) * (X**2 + Gamma_e**2 / 4)
	Z = Z**-.5

	ax[1].contour(X,Y,Z, 30)
	ax[1].set_title(r'$p(\omega_1,\omega_2)$')
	ax[1].set_xlabel(r'$\omega_1 - \omega_0$')
	ax[1].set_ylabel(r'$\omega_2 - \omega_0$')
	ax[1].set(xticks=[-1,0,1],xticklabels=[r'$-\frac{2\pi}{t-t_0}$','0',r'$\frac{2\pi}{t-t_0}$'])
	ax[1].set(yticks=[-1,0,1],yticklabels=[r'$-\frac{2\pi}{t-t_0}$','0',r'$\frac{2\pi}{t-t_0}$'])
	
plots()
s = fig.text(.45, .95, r'$\Gamma_e = %3.2f, \ \ \Gamma_f = %3.2f$' % (Gamma_e, Gamma_f), fontsize=20)

fig.subplots_adjust(bottom=0.15)
slider1 = Slider(ax = fig.add_axes([0.1, 0.05, 0.8, 0.02]), label='$G_e$', valmin=-.5, valmax=.5, valinit=0)
slider1.valtext.set_text(1)

def update(val: float):
	global Gamma_e, Gamma_f
	Gamma_e = 10 ** (slider1.val / 2); Gamma_f = 10 ** ( - slider1.val / 2);
	slider1.valtext.set_text('%3.2f' % 10**val)
	ax[0].clear()
	ax[1].clear()
	plots()
	s.set_text(r'$\Gamma_e = %3.2f, \ \ \Gamma_f = %3.2f$' % (Gamma_e, Gamma_f))
	
slider1.on_changed(update);

plt.subplots_adjust(wspace=.5)
plt.subplots_adjust(hspace=.5)
plt.show()
