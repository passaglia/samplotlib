import numpy as np 
import matplotlib.pyplot as plt
import matplotlib

############################################
## Script which sets Matplotlib RC params ##
############################################

class BasePlot():

    def __init__(self, figsize=(6,4), fontsize=10, dpi=400,baseFont='Helvetica', cjkFont='Hiragino Maru Gothic Pro', titleFont = 'Roboto Slab',textFont = 'Georgia', grey=[0,0,0]):
        ## Set basic variables of the plot
        self.figsize = figsize
        self.fontsize = fontsize
        self.dpi = dpi

        self.grey=grey

        self.baseFont = baseFont
        self.titleFont = titleFont
        self.textFont = textFont
        self.cjkFont = cjkFont

        ## Set all the rc params
        self.default_rc()

    def handlers(self, withAx=True):
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
        %\setCJKmainfont{Hiragino Kaku Gothic Pro}
        %\setCJKmainfont{Hiragino Maru Gothic Pro}
        \newcommand\stringWithFont[2]{\newfontfamily\temporary{#1} \temporary{#2}}

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

        """+ (r"\setmainfont{%s}" % (self.baseFont)) + (r"\setCJKmainfont{%s}" % (self.cjkFont)) 
        
        plt.rcParams['pgf.rcfonts'] = False
        plt.rcParams["pgf.preamble"] =  plt.rcParams['text.latex.preamble']

        from cycler import cycler
        plt.rcParams["axes.prop_cycle"] = cycler('color', [np.array([145,49,41])/255, np.array([34,65,111])/255, np.array([120,186,117])/255, np.array([233,180,99])/255, '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
        '#bcbd22', '#17becf'])

    def stringWithFont(self, font, string):
        return r'\stringWithFont{%s}{%s}' % (font, string)

    def set_byline(self,ax, byline, pad=0):
        #ax.annotate(byline, (1,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points', va='top', ha='right', family=self.textFont, fontsize=self.fontsize-2)
        ax.annotate(self.stringWithFont(self.textFont, byline) , (1,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points', va='top', ha='right', fontsize=self.fontsize-2)

    def set_source(self, ax, source, loc='inside', pad=0):
        if loc == 'inside':
            #sourcelabel = ax.text(x=0, y=0,s=source, transform=ax.transAxes, ha='left', va='baseline',color=self.grey, fontdict={'family':self.textFont})
            sourcelabel = ax.text(x=0, y=0,s=self.stringWithFont(self.textFont, source), transform=ax.transAxes, ha='left', va='baseline',color=self.grey)
            dx = 30/72.; dy = pad+(self.fontsize/3)/72. 
            offset = matplotlib.transforms.ScaledTranslation(dx, dy, ax.figure.dpi_scale_trans)
            sourcelabel.set_transform(sourcelabel.get_transform() + offset)
        elif loc == 'outside':
            #ax.annotate(source, (0,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points',color=self.grey, va='top', ha='left', family=self.textFont, fontsize=self.fontsize-2)
            ax.annotate(self.stringWithFont(self.textFont, source), (0,0), (0, -2.5*self.fontsize-pad), xycoords='axes fraction', textcoords='offset points',color=self.grey, va='top', ha='left', fontsize=self.fontsize-2)


    def set_titleSubtitle(self,ax,title,subtitle=None):
        if title is not None:
            if subtitle is None:
                # ax.figure.suptitle(title, x=0,y=1.1, fontsize=self.titlesize,ha='left',va='bottom', transform=ax.transAxes,fontdict={'family':self.titleFont})
                ax.figure.suptitle(self.stringWithFont(self.titleFont, title), x=0,y=1.1, fontsize=self.titlesize,ha='left',va='bottom', transform=ax.transAxes)
            else:
                subtitle_nlines = 1 + subtitle.count('\n')
                lineheight = self.fontsize
                gap = 2/3*self.fontsize
                pad = 1.5*self.fontsize

                # ax.set_title(subtitle, x=0., y=1.0, fontsize=self.subtitlesize,ha='left',va='bottom', fontdict={'family':self.textFont}, wrap=True, pad=pad)
                ax.set_title(self.stringWithFont(self.textFont, subtitle), x=0., y=1.0, fontsize=self.subtitlesize,ha='left',va='bottom', wrap=True, pad=pad)

                # ax.annotate(title, (0,1), (0, pad+gap+subtitle_nlines*lineheight), fontsize=self.titlesize,xycoords='axes fraction', textcoords='offset points', va='bottom', ha='left', family=self.titleFont)
                ax.annotate(self.stringWithFont(self.titleFont, title), (0,1), (0, pad+gap+subtitle_nlines*lineheight), fontsize=self.titlesize,xycoords='axes fraction', textcoords='offset points', va='bottom', ha='left')


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
            if x == 0:
                label = r'0'
            else:
                label =  r'{0:.1f}'.format(x).removesuffix('.0')
            if pos == nlabels-2:
                return  currency + label + yLabel
            else: 
                return label
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(yformatter))
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
