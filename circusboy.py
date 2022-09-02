
from baseplot import BasePlot
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter
import numpy as np

class CircusBoy(BasePlot):

    def __init__(self, figsize=(6,4), fontsize=12, dpi=400, baseFont=['Helvetica','Hiragino Maru Gothic Pro'],titleFont = 'Roboto Slab',textFont = 'Georgia', grey=[0.55,0.55,0.55]):

        super().__init__(figsize=figsize, fontsize=fontsize, dpi=dpi,
        baseFont=baseFont,titleFont =titleFont,textFont = textFont, grey=grey)
        
        self.circusboy_rc()

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
            return self._fig, self._ax
        else:
            return self._fig

        return fig, ax

    def circusboy_rc(self):
            
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
        plt.rcParams['ytick.color'] = self.grey
        plt.rcParams['ytick.labelcolor'] = self.grey
        plt.rcParams['lines.linewidth'] = 2
        
        plt.rcParams['axes.labelcolor'] = self.grey
        
        from cycler import cycler
        plt.rcParams["axes.prop_cycle"] = cycler('color', [np.array([145,49,41])/255, np.array([34,65,111])/255, np.array([120,186,117])/255, np.array([233,180,99])/255, '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

        plt.rcParams['axes.edgecolor'] = self.grey
        plt.rcParams['figure.edgecolor'] = self.grey

    def set_xYear(self,ax):
        yearformatter = matplotlib.dates.AutoDateFormatter(matplotlib.dates.AutoDateLocator())
        def my_format_function(x, pos=None):
            x = matplotlib.dates.num2date(x)
            fmt = r'%Y'
            label = r"`"+x.strftime(fmt).removeprefix("20")
            return label
        yearformatter.scaled[365.] = my_format_function
        ax.xaxis.set_major_formatter(yearformatter)
        return ax

    def set_xQuarter(self, ax):
        formatter = matplotlib.dates.AutoDateFormatter(matplotlib.dates.AutoDateLocator())
        def my_format_function(x, pos=None):
            x = matplotlib.dates.num2date(x)
            print(x.month)
            fmt = r'%Y %m'
            label = r'`'+x.strftime(fmt).removeprefix('20')
            return label
        formatter.scaled[365.] = my_format_function
        ax.xaxis.set_major_formatter(formatter)
        return ax

    def set_xMonth(self,ax):
        formatter = matplotlib.dates.AutoDateFormatter(matplotlib.dates.MonthLocator())
        def my_format_function(x, pos=None):
            x = matplotlib.dates.num2date(x)
            fmt = r'%B'
            label = x.strftime(fmt)
            return label
        formatter.scaled[30.] = my_format_function
        ax.xaxis.set_major_formatter(formatter)
        return ax

    def set_yLabel(self,ax, yLabel='', currency=''):
        def yformatter(x,pos=None):
            nlabels = len(ax.yaxis.get_ticklabels())
            #print(x,pos)
            if x == 0:
                label = r'0'
            else:
                label =  r'{0:.1f}'.format(x).removesuffix('.0')
            if pos == nlabels-2:
                return  currency + label + yLabel
            else: 
                return label
        ax.yaxis.set_major_formatter(FuncFormatter(yformatter))
        return ax

    def set_yTickLabels(self,ax):
        for label in ax.yaxis.get_ticklabels():
            label.set_verticalalignment('bottom')
            label.set_horizontalalignment('left')

        # Create offset transform by fontsize/3 points in y direction
        dx = 0/72.; dy = (self.fontsize/3)/72. 
        offset = matplotlib.transforms.ScaledTranslation(dx, dy, ax.figure.dpi_scale_trans)
        # apply offset transform to all y ticklabels.
        for label in ax.yaxis.get_majorticklabels():
            label.set_transform(label.get_transform() + offset)
        
        return ax

    def set_titleSubtitle(self,ax,title,subtitle=None):
        if title is not None:
            if subtitle is None:
                ax.figure.suptitle(title, x=0,y=1.1, fontsize=self.titlesize,ha='left',va='bottom', transform=ax.transAxes,fontdict={'family':self.titleFont})
            else:
                subtitle_nlines = 1 + subtitle.count('\n')
                lineheight = self.fontsize
                gap = 2/3*self.fontsize
                pad = 1.5*self.fontsize

                ax.set_title(subtitle, x=0., y=1.0, fontsize=self.subtitlesize,ha='left',va='bottom', fontdict={'family':self.textFont}, wrap=True, pad=pad)

                ax.annotate(title, (0,1), (0, pad+gap+subtitle_nlines*lineheight), fontsize=self.titlesize,xycoords='axes fraction', textcoords='offset points', va='bottom', ha='left', family=self.titleFont)

