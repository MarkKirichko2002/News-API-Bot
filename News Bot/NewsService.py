import requests
class NewsService:

    def currentCategory(self, id)-> str:
        match id:
            case 1:
                return "general"
            case 2:
                return "technology"
            case 3:
                return "sport"
            case 4:
                return "business"
            case 5:
                return "science"

    def fetchNews(self, category) -> []:
        arr = []
        url = f"https://newsapi.org/v2/top-headlines?country=ru&category={category}&apiKey=6b44da51f545440a81fd0ec4d6fc441a"
        response = requests.get(url)
        for i in response.json()["articles"]:
            article = i["title"]
            arr.append(article)
        return arr