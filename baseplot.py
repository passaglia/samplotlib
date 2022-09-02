import numpy as np 
import matplotlib.pyplot as plt
import matplotlib

############################################
## Script which sets Matplotlib RC params ##
############################################

class BasePlot():

    def __init__(self, figsize=(6,4), fontsize=10, dpi=400,baseFont=['Helvetica','Hiragino Maru Gothic Pro'],titleFont = 'Roboto Slab',textFont = 'Georgia', grey=[0,0,0]):
        ## Set basic variables of the plot
        self.figsize = figsize
        self.fontsize = fontsize
        self.dpi = dpi

        self.grey=grey

        self.baseFont = baseFont
        self.titleFont = titleFont
        self.textFont = textFont

        ## Set all the rc params
        self.default_rc()

    def handlers(self, withAx=True):
        ## Return the fig and axis handlers ##
        ## Set all the rc params
        #self.set_rc()
        ## Generate the figure with our w/o an axis
        self._fig = plt.figure(figsize=self.figsize)
        self._ax = None
        if withAx:
            self._ax = plt.gca()
            return self._fig, self._ax
        else:
            return self._fig

    def default_rc(self):
        # https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files
        matplotlib.use('pgf')
        golden = (1 + 5 ** 0.5) / 2

        plt.rcParams['figure.figsize'] = self.figsize
        plt.rcParams['font.size'] = self.fontsize
        plt.rcParams['font.family'] = self.baseFont

        plt.rcParams['axes.labelsize'] = plt.rcParams['font.size']
        self.titlesize = 1.5*self.fontsize
        self.subtitlesize = self.titlesize-4
        plt.rcParams['axes.titlesize'] = self.titlesize
        plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
        plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
        plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
        plt.rcParams['axes.axisbelow'] = False
        
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

        BGColor='#FDFDFE'
        plt.rcParams['axes.facecolor'] = BGColor
        plt.rcParams['figure.facecolor'] = BGColor
        plt.rcParams['savefig.facecolor'] = BGColor
        plt.rcParams['axes.edgecolor'] = 'black'
        plt.rcParams['figure.edgecolor'] = 'black'
        plt.rcParams['axes.labelcolor'] = "black"

        plt.rcParams['xtick.major.size'] = 3
        plt.rcParams['xtick.minor.size'] = plt.rcParams['xtick.major.size']/golden
        plt.rcParams['xtick.major.pad'] = 5
        plt.rcParams['xtick.minor.pad'] = 5
        plt.rcParams['xtick.major.width'] = 1
        plt.rcParams['xtick.minor.width'] = 1
        plt.rcParams['xtick.color'] = 'black'
        plt.rcParams['xtick.labelcolor'] = 'black'
        
        plt.rcParams['ytick.major.size'] = 3
        plt.rcParams['ytick.minor.size'] = plt.rcParams['ytick.major.size']/golden
        plt.rcParams['ytick.major.pad'] = 5
        plt.rcParams['ytick.minor.pad'] = 5
        plt.rcParams['ytick.major.width'] = 1
        plt.rcParams['ytick.minor.width'] = 1
        plt.rcParams['ytick.color'] = 'black'
        plt.rcParams['ytick.labelcolor'] = 'black'

        plt.rcParams['legend.frameon'] = False
        plt.rcParams['legend.loc'] = 'upper left'
        plt.rcParams['axes.linewidth'] = 1
        plt.rcParams['lines.linewidth'] = 1
        plt.rcParams['figure.autolayout'] = True
        plt.rcParams['savefig.dpi'] = self.dpi
        plt.rcParams['text.usetex'] = True
        plt.rcParams['text.latex.preamble'] =  r"""
        \usepackage{xeCJK}
        %\setCJKmainfont{Hiragino Maru Gothic Pro}
        %\setCJKmainfont[Scale=0.9]{Hiragino Mincho Pro}
        %\setCJKmainfont{Hiragino Sans}
        \setCJKmainfont{Hiragino Kaku Gothic Pro}
        
        \usepackage{xcolor}
        \usepackage{amsmath}
        \usepackage[utf8]{inputenc}
        \usepackage{newunicodechar}
        \newunicodechar{￥}{\textyen}
        \DeclareTextCommandDefault{\textyen}{%
        \vphantom{Y}%
        {\ooalign{Y\cr\hidewidth\yenbars\hidewidth\cr}}%
        }

        \newcommand{\yenbars}{%
        \vbox{
            \hrule height.1ex width.4em
            \kern.15ex
            \hrule height.1ex width.4em
            \kern.3ex
        }%
        } 
        """
        
        plt.rcParams['pgf.rcfonts'] = True
        plt.rcParams["pgf.preamble"] =  plt.rcParams['text.latex.preamble']

        from cycler import cycler
        plt.rcParams["axes.prop_cycle"] = cycler('color', [np.array([145,49,41])/255, np.array([34,65,111])/255, np.array([120,186,117])/255, np.array([233,180,99])/255, '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
        '#bcbd22', '#17becf'])

    def set_byline(self,ax, byline, pad=0):
        ax.annotate(byline, (1,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points', va='top', ha='right', family=self.textFont, fontsize=self.fontsize-2)

    def set_source(self, ax, source, loc='inside', pad=0):
        if loc == 'inside':
            sourcelabel = ax.text(x=0, y=0,s=source, transform=ax.transAxes, ha='left', va='baseline',color=self.grey, fontdict={'family':self.textFont})
            dx = 30/72.; dy = pad+(self.fontsize/3)/72. 
            offset = matplotlib.transforms.ScaledTranslation(dx, dy, ax.figure.dpi_scale_trans)
            sourcelabel.set_transform(sourcelabel.get_transform() + offset)
        elif loc == 'outside':
            ax.annotate(source, (0,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points',color=self.grey, va='top', ha='left', family=self.textFont, fontsize=self.fontsize-2)
