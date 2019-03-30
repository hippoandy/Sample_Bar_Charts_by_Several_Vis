import matplotlib.pyplot as plt
import pandas as pd

# load the dataset
df = pd.read_csv( "food_rating.csv", sep="," )

df.set_index('Country')[ [ 'Average Rating' ] ].plot.bar()
plt.show()