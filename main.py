from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from GoogleNews import GoogleNews

app = FastAPI(title="Galatasaray Haber API")

# CORS izinleri (frontend ile çalışması için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
async def get_galatasaray_news():
    googlenews = GoogleNews(lang='en', region='US')
    googlenews.search('Galatasaray')
    results = googlenews.result()
    
    # Sadece önemli alanları seçiyoruz
    news_list = []
    for item in results:
        news_list.append({
            "title": item.get("title"),
            "date": item.get("date"),
            "desc": item.get("desc"),
            "link": item.get("link"),
            "media": item.get("media"),
        })
    
    return {"news": news_list}
