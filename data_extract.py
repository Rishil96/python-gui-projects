import pandas as pd

# Read kanji table from webpage
kanji_table = pd.read_html("https://jlptsensei.com/learn-japanese/top-100-most-frequent-kanji-characters/")
kanji_table = kanji_table[0]

# 2 ways to read kanji in Japanese is Onyomi and Kunyomi
# Onyomi: is the Chinese-derived pronunciation of a kanji character
# Kunyomi: is the native Japanese reading of a kanji character

# Write the kanji table in CSV file
kanji_table.to_csv("kanji.csv")
