
from baseplot import BasePlot
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter
import numpy as np

class GrayLady(BasePlot):

    def __init__(self, figsize=(6,4), fontsize=12, dpi=400, copyrightedFonts=False):

        self.copyrightedFonts = copyrightedFonts

        grey = [0.55,0.55,0.55]
        if self.copyrightedFonts:
            super().__init__(figsize, fontsize, dpi,baseFont = 'NYTFranklin Light',titleFont = 'NYTCheltenham',textFont =  'NYTImperial',grey=grey)
        else:
            super().__init__(figsize, fontsize, dpi,baseFont = 'Helvetica',titleFont = 'Roboto Slab',textFont =  'Georgia',grey=grey)

        self.graylady_rc()

    def handlers(self, withAx=True):
        
        self._fig = plt.figure(figsize=self.figsize)
        self._ax = None
        if withAx:
            ax= plt.gca()
            self._ax = ax
            ax.spines['left'].set_color('none')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.spines['bottom'].set_color(self.grey)
            ax.yaxis.grid(color = self.grey,linestyle = (0,(0.2,3)), dash_capstyle = 'round')
            ax.set_axisbelow(True)
            self.set_yTickLabels(ax)
            return self._fig, self._ax
        else:
            return self._fig

        return fig, ax

    def graylady_rc(self):
            
        golden = (1 + 5 ** 0.5) / 2
        plt.rcParams['xtick.direction'] = 'out'
        plt.rcParams['xtick.major.size'] = self.fontsize/2
        plt.rcParams['xtick.minor.size'] = plt.rcParams['xtick.major.size']/golden
        plt.rcParams['xtick.major.pad'] = plt.rcParams['xtick.major.size']/2
        plt.rcParams['xtick.minor.pad'] = plt.rcParams['xtick.major.size']/2
        plt.rcParams['xtick.color'] = self.grey
        plt.rcParams['xtick.labelcolor'] = self.grey

        plt.rcParams['ytick.direction'] = 'out'
        plt.rcParams['ytick.major.pad'] = -1
        plt.rcParams['ytick.minor.pad'] = -1
        plt.rcParams['ytick.major.size'] = 0
        plt.rcParams['ytick.minor.size'] = 0
        plt.rcParams['ytick.labelcolor'] = self.grey

        plt.rcParams['lines.linewidth'] = 2
        
        from cycler import cycler
        plt.rcParams["axes.prop_cycle"] = cycler('color', [np.array([145,49,41])/255, np.array([34,65,111])/255, np.array([120,186,117])/255, np.array([233,180,99])/255, '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

        plt.rcParams['axes.edgecolor'] = self.grey
        plt.rcParams['figure.edgecolor'] = self.grey


## OBSOLETE
## For NYTFranklin Light to work add the following to .matplotlib/fontlist-v330.json 
# {
#   "fname": "/Users/sam/Library/Fonts/franklin-normal-300.ttf",
#   "name": "NYTFranklin Light",
#   "style": "normal",
#   "variant": "normal",
#   "weight": 300,
#   "stretch": "normal",
#   "size": "scalable",
#   "__class__": "FontEntry"
# },
