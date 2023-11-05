import requests
def currentCategory(category) -> str:
        match category:
            case "главное":
                return "general"
            case "технологии":
                return "technology"
            case "спорт":
                return "sport"
            case "бизнес":
                return "business"
            case "наука":
                return "science"

def fetchNews(category) -> []:
        arr = []
        url = f"https://newsapi.org/v2/top-headlines?country=ru&category={category}&apiKey=6b44da51f545440a81fd0ec4d6fc441a"
        response = requests.get(url)
        arr = response.json()["articles"]
        return arr