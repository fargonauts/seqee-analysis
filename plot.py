import seaborn           as sns
import matplotlib.pyplot as plt

from pprint import pprint

colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
pal    = sns.xkcd_palette(colors)

amber= sns.xkcd_palette(['amber'])

purple = sns.xkcd_palette(['dusty purple'])

def barplot(df):
    #pprint(list(df.columns.values))
    for metric in ['total_typing_time', 'time_to_understand']:
        df2  = df.groupby('problem', as_index=False)[metric].mean()
        df2  = df2.sort_values(metric).reset_index(drop=True)
        sns.barplot(x=metric, y='problem', palette=amber,  data=df2)
        plt.savefig('plots/{}_{}.png'.format(metric, 'sorted'))
        plt.clf()
        sns.barplot(x=metric, y='problem', palette=purple, data=df)
        plt.savefig('plots/{}_{}.png'.format(metric, 'unsorted'))
        plt.clf()

def plot(df):
    barplot(df)
