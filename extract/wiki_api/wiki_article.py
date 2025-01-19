import wikipediaapi
import wikipedia

def get_article(word):
    wikipedia.set_lang("ru")
    page2 = wikipedia.page(word)
    user_agent = "MyWikipediaApp/1.0 (email@gmail.com)" 
    wiki = wikipediaapi.Wikipedia(
        language="ru", 
        user_agent=user_agent
    )    
    page = wiki.page(word)
    image_url = None
    if page.exists():
        print(f"Всё ОК. Мы на нужном URL. Запрос: {word}")
        #print(page.title)
        page_text = page.text
        page_text_split = page_text.split('\n')
        #print(page_text_split[0])
        
        image_url = page2.images
        #print(image_url[0])
        
    else:
        print(f"Мы не на нужной странице! Запрос: {word}")
    
    json_object = {"title": page.title,
                        "img_src": image_url[0],
                        "text": page_text_split[0]} # возвращает первую картинку
    return json_object

    

get_article("физика")