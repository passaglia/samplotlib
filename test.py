from samplot.utils import init_plotting, MakeSingleAxFig

fig, ax = MakeSingleAxFig()
ax.plot([10,15],[2,3])
fig.savefig('test.pdf')