import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

# load the dataset
ratings = pd.read_csv( "food_rating.csv", sep="," )

g = sns.barplot( x="Country", y="Average Rating", data=ratings )
g.set_xticklabels( g.get_xticklabels(), rotation=90 )
plt.show()