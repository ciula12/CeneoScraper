# CeneoScraper

## Selektory CSS składowych opinii w ceneo
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

## Użyte biblioteki
- Requests
- BeautifulSoup
- Json 
- Os 
- Pandas 
- Numpy
- Matplolib