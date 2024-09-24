import newsapi
import time, inflect


def repetition(which_func, headlines):
    data = "news" if which_func == 0 else "details"
    repeat = str(input(f"\nWould you like to read more {data}? (Y/n)\n")).lower()

    if repeat == "y":
        headline_details_loader(headlines) if which_func == 1 else take_info()
    elif repeat == "n":
        repetition(0, headlines) if which_func == 1 else print("\nThank You! Have A Good Day.\nBYE BYE")
    else:
        print("Please enter valid information.")
        repetition(which_func, headlines)


def headline_details_loader(headlines):
    def headline_details_loop(i,j):
        print(f"\nHEADLINE NUMBER {i + 1}")
        for ind, jnd in enumerate(list(dict(j).items())):
            if ind == 0:
                print(f"{str(list(jnd)[0]).upper()} : {list((dict(list(jnd)[1])).values())[1]}")
            else:
                print(f"{str(list(jnd)[0]).upper()} : {list(jnd)[1]}")

    which_headline = str(input(
        "\nWhich headline do you want to see the details of? For the details of all headlines, enter \"all\". To skip enter \"s\".\nEnter the headline number: "))

    if which_headline.lower() == "s":
        repetition(0, headlines)
    else:
        print("Collecting details...")

        for i, j in enumerate(headlines):
            time.sleep(1)
            if which_headline.isdigit() and int(which_headline) == i + 1:
                headline_details_loop(i, j)
            elif which_headline.lower() == "all":
                headline_details_loop(i, j)
        repetition(1, headlines) if which_headline.isdigit() else repetition( 0, headlines)


def print_headlines(headlines):
    for i, j in enumerate(headlines):
        print(f"\nHEADLINE NUMBER {i + 1}")
        for ind, jnd in enumerate(list(dict(j).items())):
            if ind == 2 or ind == 3 or ind == 7:
                # print(f"{str(list(jnd)[0]).upper()} : { list((dict(list(jnd)[1])).values())[1]}")
                print(f"{str(list(jnd)[0]).upper()} : {list(jnd)[1]}")
        time.sleep(2)
    metadata = str(input(
        "\nDo you want to see the details of any headline? (Y/n)\n-->: "))
    if metadata.lower() == "y":
        headline_details_loader(headlines)
    elif metadata.lower() == "n":
        repetition(0 , headlines)


def headline_loader(keyword, language, category, country, pagesize):
    params = { 'q': keyword, 'language': language, 'page': 1 }

    if category is not None:
        params['category'] = category

    if country is not None:
        params['country'] = country

    if pagesize is not None:
        params['page_size'] = pagesize

    # Calling the API
    top_headlines = news_api.get_top_headlines(**params)

    headlines = list(top_headlines.values())[2]

    time.sleep(1)
    if headlines:
        print_headlines(headlines)
    else:
        print("SORRY! No Results Found!\nLet's try it again.".center(180))
        take_info()


def take_info():
    language_dict = {'Arabic': 'ar', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hebrew': 'he', 'Italian': 'it', 'Dutch': 'nl', 'Norwegian': 'no', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Chinese': 'zh'}
    category_dict = {"Business": 1, "Entertainment": 2, "General": 3, "Health": 4, "Science": 5, "Sports": 6, "Technology": 7}
    countries_dict = { "United Arab Emirates": "ae", "Argentina": "ar", "Austria": "at", "Australia": "au", "Belgium": "be", "Bulgaria": "bg", "Brazil": "br", "Canada": "ca", "Switzerland": "ch", "China": "cn", "Colombia": "co", "Cuba": "cu", "Czech Republic": "cz", "Germany": "de", "Egypt": "eg", "France": "fr", "United Kingdom": "gb", "Greece": "gr", "Hong Kong": "hk", "Hungary": "hu", "Indonesia": "id", "Ireland": "ie", "Israel": "il", "India": "in", "Italy": "it", "Japan": "jp", "Korea Republic": "kr", "Lithuania": "lt", "Latvia": "lv", "Morocco": "ma", "Mexico": "mx", "Malaysia": "my", "Nigeria": "ng", "Netherlands": "nl", "Norway": "no", "New Zealand": "nz", "Philippines": "ph", "Pakistan": "pk", "Poland": "pl", "Portugal": "pt", "Romania": "ro", "Serbia": "rs", "Russian Federation": "ru", "Saudi Arabia": "sa", "Sweden": "se", "Singapore": "sg", "Slovenia": "si", "Slovak Republic": "sk", "Thailand": "th", "Turkey": "tr", "Taiwan": "tw", "Ukraine": "ua", "United States": "us", "Venezuela": "ve", "South Africa": "za" }

    # Taking keyword input
    keyword = str(input("KEYWORD:\nEnter a keyword to search for: "))

    # Taking language input
    language = inputParameter(language_dict, 'language', 'en')

    # Taking category input
    category = inputParameter(category_dict, 'category')

    # Taking country input
    country = inputParameter(countries_dict, 'country')

    # Taking number of news input
    print("\nNUMBER OF RESULTS:")
    pagesize = int(input("Enter the number of results you want (Min: 2, Max: 50) : "))
    if not (2 <= pagesize <= 51):
        n1 = 0
        while int(pagesize) < 2 or int(pagesize) > 51 and n1 < 4:
            pagesize = (input("Please enter a valid value.\nEnter the number of results you want (Min: 2, Max: 50) : "))
            n1 += 1
    else:
        print("VALUE ERROR. The number of results is set to default.")
        pagesize = None

    print("\nPlease Wait, Generating Headlines...")

    # Calling other function to generate headlines
    headline_loader(keyword, language, category, country, pagesize)


def inputParameter(item_dict, item_word, default=None):

    print("\n" + str(item_word).upper() + ":\nDo you want to specify a " + item_word + "? (Y/N)")
    input_flag = str(input())
    if input_flag.upper() == 'Y':
        print("\nAvailable " + inflect.engine().plural(item_word).capitalize() + ": ")
        for key,value in item_dict.items():
            print(f"{key} : {value}")

        while True:
            input_given = input("Enter the " + item_word + " code to get results in: ").lower()
            if input_given == 's':
                break

            if input_given in str(item_dict.values()):
                if item_word != "category":
                    return input_given
                return list(item_dict.keys())[int(input_given)-1].lower()
            else:
                print("Please enter a valid " + item_word + " (or enter s to skip).")

    if item_word == "language":
        print("Selected default language: English")
        return 'en'

    return default


try:
    with open("news_api_key.txt", 'r') as api_file:
        my_api_key = api_file.readline()
    news_api = newsapi.NewsApiClient(api_key=my_api_key)
    take_info()
except FileNotFoundError as e:
    print("Error fetching the API key.\n", e)