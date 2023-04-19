import requests
import json
from bs4 import BeautifulSoup

def get_element(ancestor,selector = None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector: 
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None

selectors = {
    "opinion_id": [None, "data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "purchased": ["div.review-pz"],
    "published_at": ["span.user-post__published > time:nth-child(1)","datetime"],
    "purchased_at": ["span.user-post__published > time:nth-child(2)","datetime"],
    "thumbs_up": ["button.vote-yes > span"],
    "thumbs_down": ["button.vote-no > span"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item",None, True],
    "cons": ["div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item",None, True]
}
    
#product_code = input("Podaj kod produktu: ")
product_code = "96693065"
print(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
all_opinions = []   
while(url):
    print(url)
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_element(opinion,*value)
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+get_element(page, "a.pagination__next", "href")
    except TypeError:
        url = None

print(len(all_opinions))
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4,ensure_ascii=False)



'''
opinia							opinion		        div.js_product-review
identyfikator opinii			opinion_id	        ["data-entry-id"]
autora							author		        span.user-post__author-name
rekomendację					recommendation	    span.user-post__author-recomendation > em
liczbę gwiazdek					score   		    span.user-post__score-count
czy opinia jest 
potwierdzona zakupem			purchased	        div.review-pz
data wystawienia opinii		    published_at    	span.user-post__published > time:nth-child(1)["datetime"]
data zakupu produktu			purchased_at    	span.user-post__published > time:nth-child(2)["datetime"]
ile osób uznało opinię 
za przydatną			        thumbs_up	        button.vote-yes > span
ile osób uznało opinię 
za nieprzydatną			        thumbs_down     	button.vote-no > span]
treść opinii					content     		div.user-post__text
listę wad						cons	        	div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item
listę zalet						pros		        div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item
'''