import numpy as np 
import matplotlib.pyplot as plt
import matplotlib

############################################
## Script which sets Matplotlib RC params ##
############################################

def init_plotting(figsize=(6,4), fontsize=None, withAx = True, style=None):

    if fontsize is None:
        if style == 'nyt':
            fontsize=14
        else:
            fontsize=10

    plt.rcParams['figure.figsize'] = figsize
    plt.rcParams['font.size'] = fontsize
    #plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Computer Modern Roman'
    # plt.rcParams['font.family'] = 'sans-serif'
    # plt.rcParams['font.family'] = 'Helvetica'

    plt.rcParams['axes.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['axes.titlesize'] = 1.5*plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['axes.axisbelow'] = False
    
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    #BGColor = '#FAFAFA'
    BGColor='#FDFDFE'
    plt.rcParams['axes.facecolor'] = BGColor
    #plt.rcParams['axes.edgecolor'] = BGColor
    plt.rcParams['figure.facecolor'] = BGColor
    #plt.rcParams['figure.edgecolor'] = BGColor
    plt.rcParams['savefig.facecolor'] = BGColor
    #plt.rcParams['figure.edgecolor'] = BGColor

    plt.rcParams['xtick.major.size'] = 3
    plt.rcParams['xtick.minor.size'] = plt.rcParams['xtick.major.size']/widthToHeightratio
    plt.rcParams['xtick.major.pad'] = 5
    plt.rcParams['xtick.minor.pad'] = 5
    plt.rcParams['xtick.major.width'] = 1
    plt.rcParams['xtick.minor.width'] = 1
    plt.rcParams['ytick.major.size'] = 3
    plt.rcParams['ytick.minor.size'] = plt.rcParams['ytick.major.size']/widthToHeightratio
    plt.rcParams['ytick.major.pad'] = 5
    plt.rcParams['ytick.minor.pad'] = 5
    plt.rcParams['ytick.major.width'] = 1
    plt.rcParams['ytick.minor.width'] = 1
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.loc'] = 'upper left'
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['savefig.dpi'] = 400
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble'] =  r"""
    \usepackage{xcolor}
    \usepackage{amsmath}
    \def\yen{{\setbox0=\hbox{Y}Y\kern-.97\wd0\vbox{\hrule height.1ex
    width.98\wd0\kern.33ex\hrule height.1ex width.98\wd0\kern.45ex}}}    
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
    
    # plt.rcParams['pgf.rcfonts'] = True
    # plt.rcParams["pgf.preamble"] =  plt.rcParams['text.latex.preamble']

    fig = plt.figure(figsize=figsize)

    if withAx:
        ax = plt.gca()
        if style == 'nyt':
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.yaxis.grid(alpha=.5)
            plt.rcParams['lines.linewidth'] = 2
        return fig, ax
    else:
        return fig


################################################################
## Script generates plots of fixed physical size  ##############
################################################################

#width = 3.277
width = 3.40457
doublewidthtwocolumn = 7.05826
doublewidthonecolumn = 6.50127
middlewidth = (doublewidthonecolumn+width)/2

widthToHeightratio = 1.618

pointToInches = 1/72.
RightInches = 1 * pointToInches
topInches = 1.5* pointToInches
GapInches = .2

def MakeSingleAxFig(LeftInches=.48, BottomInches=.38, RightInches=RightInches,ratio=widthToHeightratio,fontsize=10, TopInches = topInches, width=width):
    PlotWidthInches = width - LeftInches - RightInches
    PlotHeightInches = PlotWidthInches/ratio
    height = BottomInches+PlotHeightInches+TopInches
    fig = init_plotting((width,height),fontsize=fontsize, withAx=False)
    ax = fig.add_axes([LeftInches/width, BottomInches/height,PlotWidthInches/width, PlotHeightInches/height])
    return fig, ax

def MakeDoubleAxFig(LeftInches=.48, BottomInches=.38,GapInches=.2,ratio=widthToHeightratio, fontsize=10, TopInches=topInches):
    PlotWidthInches = width - LeftInches - RightInches
    PlotHeightInches = PlotWidthInches/ratio
    height = BottomInches+2*PlotHeightInches+TopInches + GapInches
    fig = init_plotting((width,height),fontsize=fontsize, withAx=False)
    topAx = fig.add_axes([LeftInches/width, (BottomInches+PlotHeightInches+GapInches)/height,PlotWidthInches/width, PlotHeightInches/height])
    botAx = fig.add_axes([LeftInches/width, (BottomInches)/height,PlotWidthInches/width, PlotHeightInches/height])
    return fig, topAx, botAx

def MakeDoubleWideFig(LeftInches=.48, BottomInches=.38, RightInches=RightInches,ratio=widthToHeightratio, fontsize=10,  TopInches=topInches):
    return MakeSingleAxFig(LeftInches, BottomInches,RightInches,ratio,fontsize,TopInches, width=doublewidthtwocolumn)

def MakeDoubleWideDoubleAxFig(LeftInches=.48, BottomInches=.38,ratio=widthToHeightratio, GapInches =.2, LeftAxFrac = .5 , fontsize=10, TopInches=topInches, width=doublewidthtwocolumn):
    LeftPlotWidthInches = (width - LeftInches - RightInches- GapInches) * LeftAxFrac
    RightPlotWidthInches = (width - LeftInches - RightInches- GapInches) * (1-LeftAxFrac)
    PlotHeightInches = (LeftPlotWidthInches+RightPlotWidthInches+GapInches)/ratio
    height = BottomInches+PlotHeightInches+TopInches
    fig = init_plotting((width, height),fontsize=fontsize, withAx=False)
    combinedAx = fig.add_axes([LeftInches/width, BottomInches/height,(LeftPlotWidthInches+GapInches+RightPlotWidthInches)/width, PlotHeightInches/height])
    leftAx = fig.add_axes([LeftInches/width, BottomInches/height,LeftPlotWidthInches/width, PlotHeightInches/height])
    rightAx = fig.add_axes([(LeftInches+LeftPlotWidthInches+GapInches)/width, BottomInches/height,RightPlotWidthInches/width, PlotHeightInches/height])

    combinedAx.spines['top'].set_color('none')
    combinedAx.spines['bottom'].set_color('none')
    combinedAx.spines['left'].set_color('none')
    combinedAx.spines['right'].set_color('none')
    combinedAx.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
    # combinedAx.set_xticklabels([])
    # combinedAx.set_yticklabels([])
    
    return fig, leftAx, rightAx, combinedAx

def MakeDoubleWideDoubleAxVerticalFig(LeftInches=.48, BottomInches=.38, ratio=widthToHeightratio, GapInches=.2):
    PlotWidthInches = doublewidth - LeftInches - RightInches
    PlotHeightInches = PlotWidthInches/ratio
    height = BottomInches+2*PlotHeightInches+TopInches + GapInches
    fig = init_plotting((doublewidth,height),fontsize=10, withAx=False)
    combinedAx = fig.add_axes([LeftInches/doublewidth, BottomInches/height, PlotWidthInches/doublewidth, (2*PlotHeightInches+GapInches)/height])
    topAx = fig.add_axes([LeftInches/doublewidth, (BottomInches+PlotHeightInches+GapInches)/height,PlotWidthInches/doublewidth, PlotHeightInches/height])
    botAx = fig.add_axes([LeftInches/doublewidth, (BottomInches)/height,PlotWidthInches/doublewidth, PlotHeightInches/height])

    combinedAx.spines['top'].set_color('none')
    combinedAx.spines['bottom'].set_color('none')
    combinedAx.spines['left'].set_color('none')
    combinedAx.spines['right'].set_color('none')
    combinedAx.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
    # combinedAx.set_xticklabels([])
    # combinedAx.set_yticklabels([])
    return fig, topAx, botAx, combinedAx

################################################################
## Random junk  ################################################
################################################################

def add_arrow(line, position=None, direction='right', size=15, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle="->", color=color),
        size=size,
        zorder = -1
    )

def tanh_step(leftfunction, rightfunction, location, width):
    stepper = lambda x: 0.5+0.5*np.tanh((x-location)/width)
    return lambda x: (1-stepper(x))*leftfunction(x) + rightfunction(x)*stepper(x)

from matplotlib.legend_handler import HandlerBase
class legend_handler(HandlerBase):
    def create_artists(self, legend, orig_handle,
                       x0, y0, width, height, fontsize, trans):
        #print(orig_handle)
        colors =orig_handle[0]
        lss = orig_handle[1]
        lws = orig_handle[2]
        try:
            textlines = orig_handle[3]
        except IndexError:
            textlines = 1

        if len(colors)==len(lss) and len(lss)==len(lws):
            nlines = len(colors)
        else:
            raise Exception('weird input')
            # if min(len(colors), len(lss)) !=1:
            #     raise Exception('weird input')
            # else:
            #     nlines = max(len(colors), len(lss))
        #print(nlines)

        llist = []
        factor = 1/nlines
        #print(factor)
        #print('Length is', nlines)
        height *=textlines
        print("Height is", height)
        if nlines == 1:
            l = plt.Line2D([x0,y0+width], [.5*height,.5*height],
                                    color = colors[0], linestyle=lss[0],lw=lws[0])
            llist.append(l)
        else:
            for i in range(nlines):
                l = plt.Line2D([x0,y0+width], [(1-(i+1)*factor)*height,(1-(i+1)*factor)*height],
                                    color = colors[i], linestyle=lss[i],lw=lws[i])
                llist.append(l)
        return llist

import matplotlib.text as mtext
import matplotlib.transforms as mtransforms

#ra = RotationAwareAnnotation2("test label", xy=(.5,.5), p=(.6,.6), ax=ax,
#                             xytext=(2,-1), textcoords="offset points", va="top")
class RotationAwareAnnotation2(mtext.Annotation):
    def __init__(self, s, xy, p, pa=None, ax=None, **kwargs):
        self.ax = ax or plt.gca()
        self.p = p
        if not pa:
            self.pa = xy
        else:
            self.pa=pa
        kwargs.update(rotation_mode=kwargs.get("rotation_mode", "anchor"))
        mtext.Annotation.__init__(self, s, xy, **kwargs)
        self.set_transform(mtransforms.IdentityTransform())
        if 'clip_on' in kwargs:
            self.set_clip_path(self.ax.patch)
        self.ax._add_text(self)

    def calc_angle(self):
        p = self.ax.transData.transform_point(self.p)
        pa = self.ax.transData.transform_point(self.pa)
        ang = np.arctan2(p[1]-pa[1], p[0]-pa[0])
        return np.rad2deg(ang)

    def _get_rotation(self):
        return self.calc_angle()

    def _set_rotation(self, rotation):
        pass

    _rotation = property(_get_rotation, _set_rotation)

### Code to replace 10^0 with 1 in log plot tick marks. Call as:
# ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(samplot.myLogFormat))
def myLogFormat(y,pos):
    if y == 1:
        return '$1$'
    else:
        return r'$10^{' + '{:.0f}'.format(np.log10(y)) + '}$'
