import pandas as pd
import matplotlib.pyplot as plt

pokemon_dataset = pd.read_csv(r"F:\Stuff\Škola\UJEP\MSW\Vizualizace dat\Pokemon.csv")


#PRVNÍ GRAF
#Spojí sloupce Type 1 a Type 2 do jednoho a spočítá jejich počet v datasetu
type_counts = pd.concat([pokemon_dataset["Type 1"], pokemon_dataset["Type 2"]]).value_counts()
types = type_counts.index.tolist()

#Vytvoří koláčový graf
plt.pie(type_counts, labels = types, autopct = "%1.1f%%", textprops = {"fontsize": 7})

plt.title("Rozdělení typů Pokémonů")

plt.tight_layout()
plt.show()


#DRUHÝ GRAF
#Vezme sloupce Generation a Legendary a spočítá kolikrát se v jaké generaci objevilo True/False
generation_legendary_counts = pokemon_dataset.groupby(["Generation", "Legendary"]).size().unstack()

#Vytvoří skládaný sloupcový graf
ax = generation_legendary_counts.plot(kind = "bar", stacked = True)

plt.title("Počet legendárních vs. obyčejných pokémonů v každé generaci")
plt.xlabel("Generace")
plt.ylabel("Počet")

#Přídá přesný počet do sloupců a upraví čísla generací
for container in ax.containers:
    ax.bar_label(container, label_type = "center", fontsize = 8)
plt.xticks(rotation = 0)

#Posune legendu
ax.legend(title = "Legendary", loc = "center left", bbox_to_anchor = (1, 0.5))

plt.tight_layout()
plt.show()


#TŘETÍ GRAF
#Vezme sloupce Type 1 a Type 2, vytvoří unikátní skupinky těchto dvou hodnot a spočítá počet každé do sloupce "Sum"
type_combinations_counts = pokemon_dataset.groupby(["Type 1", "Type 2"]).size().reset_index(name = "Sum")

type_combinations_counts = type_combinations_counts.sort_values("Sum", ascending = True)
top_10_combinations = type_combinations_counts.head(10)

#Vytvoří sloupcový graf
plt.bar(top_10_combinations["Type 1"] + " - " + top_10_combinations["Type 2"], top_10_combinations["Sum"])

plt.title("Top 10 Nejčastějších typů kombinací")
plt.xlabel("Typy kombinací")
plt.ylabel("Počet")

#Otočí a posune jména kombinací
plt.xticks(rotation = 45, ha = "right")

plt.tight_layout()
plt.show()


#ČTVRTÝ GRAF
#Vyberu si dva sloupce, které chci mezi sebou analyzovat
x_stat = "Attack"
y_stat = "Defense"

#Vytvoří graf rozptylu
plt.scatter(pokemon_dataset[x_stat], pokemon_dataset[y_stat])

plt.title(f"{x_stat} vs {y_stat} rozptyl")
plt.xlabel(x_stat)
plt.ylabel(y_stat) 

plt.tight_layout()
plt.show()


#PÁTÝ GRAF
#Vypočítá celkovou sumu u statů v každé generaci
generation_sum_stats = pokemon_dataset.groupby("Generation")["Total"].sum()

#Vypočítá celkový počet pokemonů v každé generaci
generation_pokemon_count = pokemon_dataset["Generation"].value_counts().sort_index()

#Vytvoří "pozadí" a osu
fig1, ax1 = plt.subplots()

ax1.stackplot(generation_sum_stats.index, generation_sum_stats.values, labels = ["Součet všech statů"])
ax1.set_xlabel("Generace")
ax1.set_ylabel("Součet všech statů")

#Vytvoří osu na druhé straně
ax2 = ax1.twinx()
ax2.plot(generation_pokemon_count.index, generation_pokemon_count.values, color = "red", marker = "o", label = "Počet Pokémonů")
ax2.set_ylabel("Počet Pokémonů")

#Zkombinuje legendu pro obě osy
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc = "lower center", bbox_to_anchor = (0.49, -0.4))

plt.title("Součet všech statů a Počet Pokémonů v každé generaci")

plt.tight_layout()
plt.show()