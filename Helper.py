import matplotlib.pyplot as plt

import seaborn as sns

sns.set_style("whitegrid")

colors = ["#BC9F8B", "#B5CFB7", "#C5705D", "#ACE1AF", "#B3C8CF"]

def barplot(result, **barlimit):
  """
  >>> title = "Top 5 Highest Sales Customers"
  >>> xlabel = "Customer"
  >>> ylabel = "Total Sales"
  >>> barplot(saleport, title=title, xlabel=xlabel, ylabel=ylabel)
  """
  if "color" not in barlimit.keys():
    barlimit["color"] = colors
  bar = result.plot.bar(rot=0, **barlimit)
  for container in bar.containers:
    bar.bar_label(container, fmt="%1.1f")

def pieplot(result, **pieargs):
  """
  >>> title = "% of Total Sales in Ship Mode"
  >>> ratori = origin.groupby("customer")["sales"].sum()
  >>> pieplot(
    ratori, title=title,
    autopct='%1.1f%%', startangle=90,
    wedgeprops=dict(width=0.4), pctdistance=0.8
  )
  """
  if "colors" not in pieargs.keys():
    pieargs["colors"] = colors
  pieargs["ylabel"] = ""
  plot = result.plot.pie(**pieargs);
