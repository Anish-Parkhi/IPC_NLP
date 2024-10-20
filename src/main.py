from fastapi import FastAPI, Request
from categorize import categorize_article, ipc_sections
from preprocess import preprocess_text
from fetch_articles import fetch_articles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.post("/categorize")
async def categorize_text(request: Request):
    data = await request.json()
    query = data.get('text', '')
    
    # Fetch news articles related to the query
    articles = fetch_articles(query)

    # List to hold categorized articles
    categorized_articles = []

    # Process each article and categorize it
    for article in articles:
        content = preprocess_text(article.get('content', ''))
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')
        url = article.get('url', '#')
        
        category = categorize_article(content, ipc_sections)

        categorized_articles.append({
            "title": title,
            "description": description,
            "url": url,
            "category": category
        })

    return {"query": query, "articles": categorized_articles}
