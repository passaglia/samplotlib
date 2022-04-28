import numpy as np 
import matplotlib.pyplot as plt
import matplotlib

#Colors
ColorsOrangeRed = "#ff4500"
ColorsRoyalBlue = "#4169e1"
ColorsMediumSeaGreen = "#3CB371"
ColorsMarcoPurple = "#2A2E8B"
ColorsMarcoBlue = "#0099CC"
ColorsMarcoGreen = "#00DD34"
ColorsMarcoRed = "#CB0F28"
ColorsMarcoPink="#f24a61"
ColorsMarcoYellow = "#FFA500"
ColorsSamBurntOrange= "#CC8400"
ColorsSamLightRed="#E3112D"

#width = 3.277
width = 3.40457
doublewidthtwocolumn = 7.05826
doublewidthonecolumn = 6.50127
middlewidth = (doublewidthonecolumn+width)/2

#BGColor = '#FAFAFA'
BGColor='#FDFDFE'

widthToHeightratio = 1.618

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
    
    plt.rcParams['pgf.rcfonts'] = True
    plt.rcParams["pgf.preamble"] =  plt.rcParams['text.latex.preamble']

    fig = plt.figure(figsize=figsize)
    ax = plt.gca()

    if style == 'nyt':
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.yaxis.grid(alpha=.5)
        plt.rcParams['lines.linewidth'] = 2

    if withAx:
        return fig, ax
    else:
        return fig


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

# import numpy as np
# import matplotlib.pyplot as plt
# import samplot
# fig, ax = samplot.init_plotting((5,5), withAx=True)
# leftfunction = lambda x: -x
# rightfunction = lambda x: x**2
# location = 2 
# width = 1
# interpolatedfunction = tanh_step(leftfunction, rightfunction, location, width)
# x = np.linspace(-5, 8, 100)
# ax.plot(x, leftfunction(x))
# ax.plot(x, rightfunction(x))
# ax.plot(x, interpolatedfunction(x))
# fig.savefig('./test.pdf')
# plt.close('all')

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

"""

Module containing beautiful color schemes and some color utilities.

Authors:
    Giulia Longhi, gllonghi@yahoo.it (color schemes)
    Marco Raveri, mraveri@uchicago.edu (code)

"""

# ******************************************************************************

import math
import numpy as np

# ******************************************************************************
# Definition of the color maps:

# ------------------------------------------------------------------------------

the_gold_standard = { 0: (203.0/255.0, 15.0/255.0, 40.0/255.0),
                      1: (255.0/255.0, 165.0/255.0, 0.0),
                      2: (42.0/255.0, 46.0/255.0, 139.0/255.0),
                      3: (0.0/255.0, 153.0/255.0, 204.0/255.0),
                      4: (0.0/255.0, 221.0/255.0, 52.0/255.0),
                      5: (0.0, 0.0, 0.0),
                      6: (0.0, 0.75, 0.75),
                    }

# ------------------------------------------------------------------------------

spring_and_winter = {
                    0: (93./255., 50./255., 137./255.),
                    1: (197./255., 43./255., 135./255.),
                    2: (237./255., 120./255., 159./255.),
                    3: (241./255., 147./255., 130./255.),
                    4: (113./255., 187./255., 220./255.),
                    5: (24./255., 120./255., 187./255.),
                    }

# ------------------------------------------------------------------------------

winter_and_spring = { 0: (24./255., 120./255., 187./255.),
                      1: (113./255., 187./255., 220./255.),
                      2: (241./255., 147./255., 130./255.),
                      3: (237./255., 120./255., 159./255.),
                      4: (197./255., 43./255., 135./255.),
                      5: (93./255., 50./255., 137./255.),
                    }

# ------------------------------------------------------------------------------

summer_sun = { 0: (234./255., 185./255., 185./255.),
               1: (234./255., 90./255., 103./255.),
               2: (255./255., 231./255., 76./255.),
               3: (249./255., 179./255., 52./255.),
               4: (55./255., 97./255., 140./255.),
               5: (82./255., 158./255., 214./255.),
             }

# ------------------------------------------------------------------------------

summer_sky = { 0: (82./255., 158./255., 214./255.),
               1: (55./255., 97./255., 140./255.),
               2: (249./255., 179./255., 52./255.),
               3: (255./255., 231./255., 76./255.),
               4: (234./255., 90./255., 103./255.),
               5: (234./255., 185./255., 185./255.),
             }

# ------------------------------------------------------------------------------

autumn_fields = { 0: (50./255., 138./255., 165./255.),
                  1: (16./255., 135./255., 98./255.),
                  2: (198./255., 212./255., 60./255.),
                  3: (255./255., 251./255., 73./255.),
                  4: (237./255., 118./255., 40./255.),
                  5: (142./255., 26./255., 26./255.),
                }

# ------------------------------------------------------------------------------

autumn_leaves = { 0: (142./255., 26./255., 26./255.),
                  1: (237./255., 118./255., 40./255.),
                  2: (255./255., 251./255., 73./255.),
                  3: (198./255., 212./255., 60./255.),
                  4: (16./255., 135./255., 98./255.),
                  5: (50./255., 138./255., 165./255.),
                }

# ******************************************************************************
# definition of color interpolation utilities:

def color_linear_interpolation( rgb_1, rgb_2, alpha ):
    """
    This function performs a linear color interpolation in RGB space.
    alpha has to go from zero to one and is the coordinate.
    """
    _out_color = []
    for _a,_b in zip(rgb_1,rgb_2):
        _out_color.append( _a +(_b-_a)*alpha )
    return tuple(_out_color)

# ******************************************************************************
# definition of the color helper:

def nice_colors( num, colormap='the_gold_standard', interpolation_method='linear', output_format='RGB' ):
    """
    This function returns a color from a colormap defined above, according to the
    number entered.

    :param num: input number. Can be an integer or float.
        If the number is integer the function returns one of the colors in the
        colormap. If the number is a float returns the shade combining the two
        neighbouring colors.
    :type num: :class:`int` or :class:`float`

    :param colormap: a string containing the name of the colormap.
    :type colormap: :class:`string`

    :param interpolation_method: the method to interpolate between colors.
        Legal choices are:
            interpolation_method='linear', linear interpolation;
        Further interpolation methods will be added in the future.
    :type interpolation_method: :class:`string`

    :param output_format: output format of the color.
        Legal choices are:
            output_format='HEX'
            output_format='RGB' (default)
    :type output_format: :class:`string`

    :return: string with HEX color or tuple with RGB coordinates

    """
    # get the colormap:
    try:
        _cmap = globals()[str(colormap)]
    except:
        raise ValueError('Requested color map ('+str(colormap)+') does not exist.')
    # get the indexes of the color map:
    _idx_low = int( math.floor(num%len(_cmap)) )
    _idx_up  = int( math.floor((_idx_low+1)%len(_cmap)) )
    # perform color interpolation:
    if interpolation_method=='linear':
        _t = num%len(_cmap)-_idx_low
        _out_color = color_linear_interpolation(_cmap[_idx_low],_cmap[_idx_up],_t)
    else:
        raise ValueError('Requested color interpolation method ('+str(interpolation_method)+') does not exist.')
    # choose the output format:
    if output_format=='HEX':
        _out_color = '#%02x%02x%02x' % tuple( [ _c*255. for _c in _out_color] )
    elif output_format=='RGB':
        pass
    else:
        raise ValueError('Requested output format ('+str(output_format)+') does not exist.')
    #
    return _out_color
