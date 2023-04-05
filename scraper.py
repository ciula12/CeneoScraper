import requests
from bs4 import BeautifulSoup

def get_sth(ancestor,selector = None, atribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector: 
            return ancestor[atribute]
        if atribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
    
#product_code = input("Podaj kod produktu: ")
product_code = "143471602"
print(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")

all_opinions = []

for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "score": opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased": opinion.select_one("div.review-pz").text.strip(),
        "published_at": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchased_at": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "thumbs_up": opinion.select_one("button.vote-yes > span").text.strip(),
        "thumbs_down": opinion.select_one("button.vote-no > span").text.strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "pros": [pros.text.strip() for pros in opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")],
        "cons": [cons.text.strip() for cons in opinion.select("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item")],
    }
    all_opinions.append(single_opinion)

print(all_opinions)




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