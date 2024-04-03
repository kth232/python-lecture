"""
t = "there's a reason some people are working to make it harder to vote, especially for people of color. It'vcruntime140.dll"
length = len(t.split(" "))
print('word count: ', length)
"""
"""
t =  "It's Not The Right Time To Conduct Exam. MY DREAM IN BOLD AND CAPITAL. NO EXAMS IN COVID!"
1 = t.lower()
"""
"""
import random
import string

src_str = string.ascii_letters + '0123456789'
n_digits = int(input("몇 자리 비밀번호를 원하십니까? "))

otp = ''
for i in range(n_digits):
    otp += str(random.randrange(len(src_str))
     otp += src_str[idx]
               
print(otp)
""" 
# 워드 클라우드 임포트 필요
import wikipedia


wiki = wikipedia.page('Artificial intelligence')
text = wiki.content

from wordcloud import WordCloud

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)

import matplotlib.pyplot as plt

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.show()

