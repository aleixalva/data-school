# the languages of africa

## get the data

```Bash
wget https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-01-13/africa.csv -O africa.csv
```

## first exploration

Head of file:

```Bash
$ head africa.csv
language,family,native_speakers,country
ǂKxʼaoǁʼae,Kxʼa,5000,Namibia
ǂKxʼaoǁʼae,Kxʼa,5000,Botswana
Abon,Niger–Congo,800,Cameroon
Abron,Niger–Congo,1393000,Ghana
Abron,Niger–Congo,1393000,Ivory Coast
Acheron,Niger–Congo,20000,Sudan
Adara,Niger–Congo,300000,Nigeria
Afar,Afroasiatic,2500000,Ethiopia
Afar,Afroasiatic,2500000,Djibouti
```

or with Pandas (Python):

```Python
df = pd.read_csv("africa.csv")
print (df.head(10))
```

### Number of rows:

```Bash
$ cat africa.csv | wc -l
797
# beware, this counts the header, so it's 796
```

```Python
print(df.shape)
(796,4)

print(df.shape[0])
796
```

### How many different languages?

```Bash
$ tail -n +2 africa.csv | cut -d, -f1 | sort | uniq | wc -l
502
```

Steps:

- tail -n +2 prints from line 2 onwards (so we ignore headers) 
- cut takes the first column
- sort alphabetically
- uniq eliminates adjacent duplicates
- wc counts lines

Alternative using `sort -u` instead of `sort | uniq`:

```Bash
$ tail -n +2 africa.csv | cut -d, -f1 | sort -u | wc -l
502
```

In Pandas, notice the difference between these commands:

```Python
print(df['language'].value_counts())
language
Soninke      13
Arabic       12
Fulani       11
Mooré         9
Fang          7
             ..
Yela-Kela     1
Yemba         1
Zhire         1
Zhoa          1
Zulu          1
Name: count, Length: 502, dtype: int64

print(df['language'].nunique())
502
```

How many countries?

```Bash
$ tail -n +2 africa.csv | cut -d, -f4 | sort -u | wc -l
52
# subtract 1 (headers)
```
```Python
print(df['country'].nunique())
51
```

### Which language has the largest number of native speakers?

```Bash
$ mlr --csv stats1 -a sum -f native_speakers -g language \
    then sort -nr native_speakers_sum africa.csv | head -n 2
language,native_speakers_sum
Arabic,1800000000
```

This adds `native_speakers` grouped by `language`, and then sorts it numerically using a newly created field called `native_speakers_sum` (mlr creates it).

Pandas:

```Python
speakers_by_language = (
    df.groupby("language")["native_speakers"]
    .sum()
    .sort_values(ascending=False)
)
speakers_by_language.head(1)

language
Arabic    1800000000
```

### Which family has the most languages in the dataset?

Or, in other words, which family contains the largest number of distinct languages in this dataset?

```Bash
$ mlr --csv cut -f language,family then sort -f family \
    then uniq -f language,family \
    then stats1 -a count -f language -g family \
    then sort -nr language_count africa.csv
family,language_count
Niger–Congo,383
Nilo-Saharan,70
Afroasiatic,17
Ubangian,6
Afro-Asiatic,4
Indo-European,4
Khoe–Kwadi,4
Kxʼa,4
Arabic-based,2
English,2
French,2
Austronesian,1
Kongo-based,1
Language,1
Mande,1
Portuguese,1
Tuu,1
```

Notice a problem: there is a coexistence of `Afroasiatic` and `Afro-Asiatic`. We can deal with that first:

```Bash
$ sed 's/Afro-Asiatic/Afroasiatic/' africa.csv > africa2.csv
$ mlr --csv cut -f language,family then sort -f family \
    then uniq -f family,language \
    then  stats1 -a count -f language -g family then \
    sort -nr language_count  africa2.csv
family,language_count
Niger–Congo,383
Nilo-Saharan,70
Afroasiatic,21
Ubangian,6
Indo-European,4
Khoe–Kwadi,4
Kxʼa,4
Arabic-based,2
English,2
French,2
Austronesian,1
Kongo-based,1
Language,1
Mande,1
Portuguese,1
Tuu,1
```

Python:

```Python
df.groupby("family")["language"].nunique().sort_values(ascending=False)

family
Niger–Congo      383
Nilo-Saharan      70
Afroasiatic       17
Ubangian           6
Khoe–Kwadi         4
Kxʼa               4
Afro-Asiatic       4
Indo-European      4
French             2
English            2
Arabic-based       2
Language           1
Mande              1
Austronesian       1
Portuguese         1
Tuu                1
Kongo-based        1
Name: language, dtype: int64
```

Again, the same problem with "Afroasiatic". Replace first:

```Python
df["family"]=df["family"].str.replace("Afro-Asiatic","Afroasiatic", regex=True)
```

Then repeat the command:

```Python
df.groupby("family")["language"].nunique().sort_values(ascending=False)

family
Niger–Congo      383
Nilo-Saharan      70
Afroasiatic       21
Ubangian           6
Indo-European      4
Khoe–Kwadi         4
Kxʼa               4
Arabic-based       2
English            2
French             2
Austronesian       1
Kongo-based        1
Language           1
Mande              1
Portuguese         1
Tuu                1
Name: language, dtype: int64
```

### Which countries have the greatest number of distinct languages?

```Bash
$ mlr --csv cut -f language,country then uniq -f language,country \
    then stats1 -a count -f language -g country \
    then sort -nr language_count africa.csv | head
country,language_count
Cameroon,95
Congo,79
Nigeria,73
Sudan,40
Burkina Faso,36
Ghana,34
Namibia,24
Chad,24
South Sudan,23
```

Python:

```Python
languages_per_country = (
    df.groupby("country")["language"]
    .nunique()
    .sort_values(ascending=False)
)

languages_per_country.head(10)

country
Cameroon        95
Congo           79
Nigeria         73
Sudan           40
Burkina Faso    36
Ghana           34
Chad            24
Namibia         24
South Sudan     23
Mali            22
Name: language, dtype: int64

### Which language occurs in the greatest number of countries?

```Bash
$ mlr --csv cut -f country,language \
    then uniq -f country,language \
    then stats1 -a count -f country -g language \
    then sort -nr country_count africa.csv | head
language,country_count
Arabic,12
Fulani,10
Mooré,8
Soninke,8
Gourmanché,6
Lozi,6
Bariba,5
Khwe,5
Mampruli,5
```

Python:

```Python
countries_per_language = (
    df.groupby("language")["country"]
    .nunique()
    .sort_values(ascending=False)
)

countries_per_language.head(10)

language
Arabic        12
Fulani        10
Mooré          8
Soninke        8
Lozi           6
Gourmanché     6
Portuguese     5
Khwe           5
Swahili        5
Bariba         5
Name: country, dtype: int64
```

### Which language family has the largest total number of native speakers represented?
