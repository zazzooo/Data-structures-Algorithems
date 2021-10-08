import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

plates_request = pd.read_csv('applications.csv', sep = ',')

print(plates_request.head(10))

plates_request['reviewer_comments'] = plates_request['reviewer_comments'].astype('str')
plates_request['status'] = plates_request['status'].astype('str')
denied = plates_request[plates_request['status']=='N']
plates = " ".join(review for review in denied.reviewer_comments)

wordcloud_plates = WordCloud(background_color="white").generate(plates)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud_plates, interpolation='bilinear')
plt.axis("off")
plt.show()
