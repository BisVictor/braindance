import wikipediaapi
import wikipedia

def get_article(word):
    wikipedia.set_lang("ru")
    page2 = wikipedia.page(word)
    user_agent = "MyWikipediaApp/1.0 (xcatcherx@gmail.com)"  # Замените на свои данные
    wiki = wikipediaapi.Wikipedia(
        language="ru", 
        user_agent=user_agent
    )    
    page = wiki.page(word)
    if page.exists():
        print(f"Всё ОК. Мы на нужном URL. Запрос: {word}")
        image_url = page2.images
        print(image_url[0])
        
    else:
        print(f"Мы не на нужной странице! Запрос: {word}")

get_article("Химия")