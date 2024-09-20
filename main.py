# Use the NewsAPI and the request module to fetch the daily news related to different topics.
# Go to https://newsapi.org/ and explore the various options to build your application
import newsapi
import time


def repetition(which_func, headlines):
    data = "news" if which_func == "headline_loader()" else "metadata"
    repeat = str(input(f"\nWould you like to read more {data}?\nEnter 'Yes' or 'No':\n")).lower()
    if repeat == "yes":
        if which_func == "headline_metadata_loader()":
            headline_metadata_loader(headlines)
        elif which_func == "headline_loader()":
            take_info()
    elif repeat == "no":
        if which_func == "headline_metadata_loader()":
            repetition("headline_loader()", headlines)
        elif which_func == "headline_loader()":
            print("\nThank You! Have A Good Day.\nBYE BYE")
            exit()
    else:
        print("Please enter valid information.")


def headline_metadata_loader(headlines):
    which_headline = str(input(
        "\nWhich headline do you want to see the metadata of? For the meatadata of all headlines, enter command \"All\". To skip enter command \"Skip\".\nEnter the headline number: "))
    if which_headline.lower() == "skip":
        repetition("headline_loader()", headlines)
    elif which_headline.lower() == "all":
        print("Collecting metadata...")
        for i, j in enumerate(headlines):
            time.sleep(2)
            print(f"\nHEADLINE NUMBER {i + 1}")
            for key, value in dict(j).items():
                print(f"{str(key).upper()} : {value}")
        repetition("headline_metadata_loader()", headlines)
    elif int(which_headline) != -1:
        print("Collecting metadata...")
        time.sleep(1)
        for i, j in enumerate(headlines):
            if int(which_headline) == i + 1:
                print(f"\nHEADLINE NUMBER {which_headline}")
                for key, value in dict(j).items():
                    print(f"{str(key).upper()} : {value}")
        repetition("headline_metadata_loader()", headlines)


def headline_loader(keyword, language, category, country, pagesize):
    global top_headlines
    if country is not None and pagesize is not None:
        top_headlines = news_api.get_top_headlines(q=keyword, language=language, category=category, country=country,
                                                   page_size=pagesize, page=1)
    elif country is None and pagesize is not None:
        top_headlines = news_api.get_top_headlines(q=keyword, language=language, category=category, page_size=pagesize,
                                                   page=1)
    elif country is not None and pagesize is None:
        top_headlines = news_api.get_top_headlines(q=keyword, language=language, category=category, country=country,
                                                   page=1)
    elif country is None and pagesize is None:
        top_headlines = news_api.get_top_headlines(q=keyword, language=language, category=category, page=1)

    headlines = list(top_headlines.values())[2]
    time.sleep(1)
    if headlines:
        for i, j in enumerate(headlines):
            print(f"\nHEADLINE NUMBER {i + 1}")
            for ind, jnd in enumerate(list(dict(j).items())):
                if ind == 2 or ind == 3 or ind == 7:
                    print(f"{str(list(jnd)[0]).upper()} : {list(jnd)[1]}")
            time.sleep(2)
        metadata = str(input(
            "\nIf you want to see the metadeta of any headline then enter command \"Metadata\". To skip enter command \"Skip\".\nEnter command: "))
        if metadata.lower() == "metadata":
            headline_metadata_loader(headlines)
        elif metadata.lower() == "skip":
            repetition("headline_loader()", headlines)
    else:
        print("SORRY! No Results Found!\nLet's try it again.".center(180))
        take_info()


def take_info():
    # global pagesize, country, category, language

    category_dict = {"Business": 1, "Entertainment": 2, "General": 3, "Health": 4, "Science": 5, "Sports": 6,
                     "Technology": 7}
    countries_dict = {"ae": "United Arab Emirates", "ar": "Argentina", "at": "Austria", "au": "Australia",
                      "be": "Belgium", "bg": "Bulgaria", "br": "Brazil", "ca": "Canada", "ch": "Switzerland",
                      "cn": "China", "co": "Colombia", "cu": "Cuba", "cz": "Czech Republic", "de": "Germany",
                      "eg": "Egypt", "fr": "France", "gb": "United Kingdom", "gr": "Greece", "hk": "Hong Kong",
                      "hu": "Hungary", "id": "Indonesia", "ie": "Ireland", "il": "Israel", "in": "India", "it": "Italy",
                      "jp": "Japan", "kr": "Korea Republic", "lt": "Lithuania", "lv": "Latvia", "ma": "Morocco",
                      "mx": "Mexico", "my": "Malaysia", "ng": "Nigeria", "nl": "Netherlands", "no": "Norway",
                      "nz": "New Zealand", "ph": "Philippines", "pk": "Pakistan", "pl": "Poland", "pt": "Portugal",
                      "ro": "Romania", "rs": "Serbia", "ru": "Russian Federation", "sa": "Saudi Arabia", "se": "Sweden",
                      "sg": "Singapore", "si": "Slovenia", "sk": "Slovak Republic", "th": "Thailand", "tr": "Turkey",
                      "tw": "Taiwan", "ua": "Ukraine", "us": "United States", "ve": "Venezuela", "za": "South Africa"}

    # Taking keyword input
    keyword = str(input("KEYWORD:\nEnter a keyword to search for: "))

    # Taking language input

    time.sleep(1)
    print("\nLANGUAGE:\nDo you want to specify a language? (Y/N)")
    input_flag = str(input())
    language = 'en' if input_flag.upper() == 'N' else inputLanguage()
    print(language)

    # Taking category input

    time.sleep(1)
    print("\nCATEGORY:\nDo you want to specify a category? (Y/N)")
    input_flag = str(input())
    category = None if input_flag.upper() == 'N' else inputCategory()

    for key, value in category_dict.items():
        print(f"For {key}, enter {value}")
    category_given = str(input("\nEnter the category to search in: "))
    try:
        while int(category_given) not in category_dict.values():
            print("Please enter a valid value.")
            category_given = input("Enter the category to search in: ").lower()
        for key, value in category_dict.items():
            if category_given.lower() == str(value).lower():
                category = str(key).lower()
    except Exception as e:
        print("VALUE ERROR. The category is set to \"General\" by default.")
        category = "general"

    #Taking country input

    time.sleep(1)
    print("\nCOUNTRY:\nAvailable Countries:", ', '.join(countries_dict.values()), "\n")
    country_given = str(input("Enter the country to search for: ")).lower()
    n = 0
    while country_given.title() not in countries_dict.values() and n < 4:
        print("Please enter a valid country.")
        country_given = str(input("Enter the country to search for: ")).lower()
        n += 1
    for key, value in countries_dict.items():
        if country_given.lower() == str(value).lower():
            country = str(key)
    if n == 4:
        print("VALUE ERROR. Country is set to default.")
        country = None

    #Taking number of news input
    time.sleep(1)
    print("\nNUMBER OF RESULTS:")
    pagesize_given = (input("Enter the number of results you want (Min: 2, Max: 50) : "))
    n1 = 0
    try:
        while (int(pagesize_given) < 2 or int(pagesize_given) > 51) and (n1 < 4):
            print("Please enter a valid value.")
            pagesize_given = (input("Enter the number of results you want (Min: 2, Max: 50) : "))
            n1 += 1
        if (int(pagesize_given) >= 2 and int(pagesize_given) <= 51):
            pagesize = int(pagesize_given)
        elif (int(pagesize_given) < 2 or int(pagesize_given) > 51) and (n1 == 4):
            print("VALUE ERROR. The number of results is set to default.")
            pagesize = None
    except Exception as e:
        print("VALUE ERROR. The number of results is set to default.")
        pagesize = None

    print("\nPlease Wait, Generating Headlines...")
    #Calling other function to generate headlines
    headline_loader(keyword, language, category, country, pagesize)


def inputLanguage():
    language_dict = {'Arabic': 'ar', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hebrew': 'he',
                     'Italian': 'it', 'Dutch': 'nl', 'Norwegian': 'no', 'Portuguese': 'pt', 'Russian': 'ru',
                     'Swedish': 'sv', 'Chinese': 'zh'}
    print("\nAvailable Languages:", ', '.join(language_dict.keys()), "\n")

    language_given = input("Enter the language to get results in: ").lower()

    try:
        while language_given.capitalize() not in language_dict.keys():
            print("Please enter a valid language.")
            language_given = input("Enter the language to get results in: ").lower()
        for key, value in language_dict.items():
            if language_given.lower() == str(key).lower():
                return value
    except Exception as e:
        print("VALUE ERROR. The language is set to \"English\" by default.")
        return 'en'


news_api = newsapi.NewsApiClient(api_key="7b8252e5a19d4283bb74bfe824d282c9")
take_info()
