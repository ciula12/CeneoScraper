import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(",",".")))

opinions_count = len(opinions.index)
pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
cons_count = sum([False if len(p)==0 else True for p in opinions.cons])
avg_score = opinions.score.mean()


#print(opinions)
#print(f"Pros: {pros_count}")
#print(cons_count)
#print(opinions.score)

print(f"Dla produktu {product_code} dostępnych jest {opinions_count} opinii.\nDla {pros_count} dostępna jest lista zalet, a dla {cons_count} dostępna jest lista wad.\nŚredia ocen produktu to {round(avg_score,2)}.")

#histogram ocen
score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value = 0)
score.plot.bar()
plt.xticks(rotation = 0)
score.plot.bar(color="pink")
plt.title("Histogram ocen")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
for index, value in enumerate(score):
    plt.text(index, value+0.4, str(value), ha="center")
#plt.show()
try:
    os.mkdir("./plots")
except FileExistsError:
    pass
plt.savefig(f"./plots/{product_code}_score.png")
plt.close()

#udział poszczególnych rekomendacji w liczbie opinii
recommendation = opinions["recommendation"].value_counts(dropna = False).sort_index()
print(recommendation)
recommendation.plot.pie(
    label="", 
    autopct="%1.1f%%",
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"],
    colors = ["crimson", "forestgreen", "grey"]
    )
plt.legend(bbox_to_anchor=(1,1))
plt.savefig(f"./plots/{product_code}_recommendation.png")
plt.close()