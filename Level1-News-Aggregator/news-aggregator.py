from flask import Flask,render_template,request
from newsapi import NewsApiClient
 
 
app = Flask(__name__)
 
yourAPIKEY = '82c6e4822af74084958f8ccb601aeff6'

newsapi = NewsApiClient(api_key=yourAPIKEY)

@app.route('/')
def home():
    return render_template('index.html',news='')
 
@app.route('/results/',methods=['POST']) 
def get_results():
    keyword = request.form['keyword']  

    news = newsapi.get_top_headlines(q=keyword,
                                     language='en',
                                     country='in')
    return render_template('index.html',news=news['articles'])

if __name__ == "__main__":
    app.run()