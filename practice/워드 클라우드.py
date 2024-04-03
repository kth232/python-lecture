import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud

# 위키백과 사전의 컨텐츠 제목을 명시해 준다
wiki = wikipedia.page('bigdata analysis')
# 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
text = wiki.content
# 워드 클라우드를 생성하기 위해 위의 코드를 삽입할 것
wordcloud = WordCloud(width = 500, height = 500).generate(text)

plt.figure(figsize=(40, 30))
# 화면에 이미지를 그려준다
plt.imshow(wordcloud) 
plt.show()
