from fetch_articles import fetch_articles
from preprocess import preprocess_text
from categorize import categorize_article, ipc_sections

def display_results(articles):
    for article in articles:
        title = article.get('title')
        description = article.get('description')
        content = preprocess_text(article.get('content', ''))
        category = categorize_article(content, ipc_sections)
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Category: {category}")
        print('-' * 50)

def main():
    query = input("Enter a crime term: ")
    articles = fetch_articles(query)
    display_results(articles)

if __name__ == "__main__":
    main()
