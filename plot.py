import seaborn           as sns
import matplotlib.pyplot as plt



#from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})

from pprint import pprint

colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
pal    = sns.xkcd_palette(colors)

amber= sns.xkcd_palette(['amber'])

purple = sns.xkcd_palette(['dusty purple'])


def barsave(df, metric, s):
    if s:
        pal = amber
        s = 'sorted'
    else:
        pal = purple
        s = 'unsorted'
    sns.barplot(x=metric, y='problem', palette=pal, data=df)
    plt.tight_layout()
    plt.savefig('plots/{}_{}.png'.format(metric, s))
    plt.clf()

def barplot(df):
    sns.set(font_scale=.5, rc={'figure.figsize':(11,11)})
    #pprint(list(df.columns.values))
    for metric in ['total_typing_time', 'time_to_understand']:
        barsave(df, metric, False)

        df2  = df.groupby('problem', as_index=False)[metric].mean()
        df2  = df2.sort_values(metric).reset_index(drop=True)
        barsave(df2, metric, True)
    sns.set(font_scale=1)

def plot(df):
    barplot(df)
