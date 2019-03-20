import numpy as np 

def figsize(scale=1):
    '''Create nicely proportioned figure

    This function calculates the optimal figuresize for any given scale
    (the ratio between figuresize and textwidth. A figure with scale 1
    covers the entire writing area). Therefor it is important to know 
    the textwidth of your target document. This can be obtained by using
    the command "\the\textwidth" somewhere inside your document.
    '''

    width_pt  = 373.44                        # textwidth from latex
    in_per_pt = 1.0/72.27                     # Convert pt to inch
    golden    = 1.61803398875                 # Aesthetic ratio 
    width  = width_pt * in_per_pt * scale     # width in inches
    height = width / golden                   # height in inches
    return [width,height]

import matplotlib as mpl

mpl.use('pgf')

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


plt.style.use('TeX')

def newfig(scale=1,ratio=None):
    '''Create a new figure object

    We use the function figsize to create a figure of corresponding size.
    If the option ratio is choosen, the width of the plot is still taken
    from figsize but the ratio of the figure is determined by ratio.
    '''

    size = figsize(scale)
    if not ratio:
        fig = plt.figure(figsize=size)
    else:
        fig = plt.figure(figsize=(size[0],ratio*size[0]))

    return fig

# showcase
fig = newfig(scale=1)
ax  = fig.add_subplot(111)

x = np.linspace(0,2*np.pi)
y = np.sin(x)

ax.plot(x,y)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$\sin(x)$')

plt.savefig('plot.pdf',bbox_inches='tight')
plt.savefig('plot.pgf',bbox_inches='tight')
