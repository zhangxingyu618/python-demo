import re
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt

file = open(r'C:/Users/Lenovo/Desktop/harry-potter.txt', 'r', encoding='UTF-8')
text = file.read()
file.close()
cut_text = " ".join(jieba.cut(text))

word1 = cut_text.split()
# word1 = [re.sub("[\， \。 \ !\： \？ ]", '', word) for word in words]

words_index = set(word1)
dic = {index: word1.count(index) for index in words_index}
image = Image.open('C:/Users/Lenovo/Desktop/danghui.jpg')
graph = np.array(image)
print(dic)

wc = WordCloud(background_color='White', mask=graph,)
wc.generate_from_frequencies(dic)
wc.to_file(r"C:/Users/Lenovo/Desktop/danghui2.jpg")

plt.imshow(wc)
plt.axis("off")
plt.show()