import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import squarify

# Let's read and print the data from source
data = pd.read_csv("https://raw.githubusercontent.com/Abduvakhit/Python_Project_1/main/Billionaire.csv")
print(data.head())

# Check for null values in dataset and clean 
print(data.isnull().sum())
data = data.dropna()

# Clean NetWorth collumn and convert to float type
data["NetWorth"] = data["NetWorth"].str.strip("$")
data["NetWorth"] = data["NetWorth"].str.strip("B")
data["NetWorth"] = data["NetWorth"].astype(float)

# Plotting top10 billionaries by NetWorth
df = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.subplot(1, 3, 1)
plt.barh(df["Name"], df["NetWorth"], color=["#115f9a", "#1984c5", "#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9e52f", "#d0ee11", "#d0f400", "#FFFF00"])
plt.xlabel("NetWorth")
plt.rc('font', size=12)
plt.title("Top 10 Billionaries", fontsize=16)
for i, v in enumerate(df["NetWorth"]):
    plt.text(v+0.2, i, str(round(v, 2)), color='black', va="center", fontsize = 10)

# Plotting top 5 domains
a = data["Source"].value_counts().head()
index = a.index.str.title()
sources = a.values
custom_colors = ["#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9e52f"]
plt.subplot(2, 3, 3)
plt.pie(sources, labels=sources, colors=custom_colors, wedgeprops = {"edgecolor" : "white",
                      'linewidth': 2,
                      'antialiased': True})
plt.legend(index, frameon=False, bbox_to_anchor =(1, 0.5), loc='center left' , fontsize = 8)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Domains", fontsize=16)


# Top 5 Industries
a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
plt.subplot(2, 3, 6)
plt.pie(industries, labels=industries, colors=custom_colors, wedgeprops = {"edgecolor" : "white",
                      'linewidth': 2,
                      'antialiased': True})
plt.legend(index, frameon=False, bbox_to_anchor =(1, 0.5), loc='center left' , fontsize = 8)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)                      
plt.title("Top 5 Industries", fontsize=16)

# Top 5 Countries
a = data["Country"].value_counts().head()
index = a.index
Countries = a.values
plt.subplot(2, 3, 5)
squarify.plot(sizes = Countries, label = Countries, alpha = .8, color=custom_colors, pad=2)
plt.legend(index, frameon=False, bbox_to_anchor =(0.5,-0.2), loc='lower center', ncol=5, fontsize = 8)
plt.axis('off')
plt.title("Top 5 Countries", fontsize=16)


# Age vs NetWorth
plt.subplot(2, 3, 2)
plt.scatter(df["Age"],df["NetWorth"], color=["#115f9a", "#1984c5", "#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9e52f", "#d0ee11", "#d0f400", "#FFFF00"])
plt.title('Age vs NetWorth', fontsize=16)
plt.xlabel('Age')
plt.ylabel('NetWorth')
for i, txt in enumerate(df["Age"]):
    plt.annotate(int(txt), (df["Age"][i], df["NetWorth"][i]), fontsize = 8)

# Set the spacing between subplots
plt.subplots_adjust(left=0.124,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

# Create main title
plt.suptitle('Billionaires Analysis 2021', fontsize = 20)
plt.show()



