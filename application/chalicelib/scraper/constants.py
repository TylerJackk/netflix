# ============ API URL ==========
UNGOS_BASE = "https://unogs.com/api/"
UNGOS_BASE_API = UNGOS_BASE + "title/"
DETAIL = UNGOS_BASE_API + "detail"
BGIMAGES = UNGOS_BASE_API + "bgimages"
GENRES = UNGOS_BASE_API + "genres"
PEOPLE = UNGOS_BASE_API + "people"
COUNTRIES = UNGOS_BASE_API + "countries"
EPISODES = UNGOS_BASE_API + "episodes"
STATIC_INFO = UNGOS_BASE + "static/all"
SEARCH = UNGOS_BASE + "search"

# ============ Cast Type ==========
ACTOR = "Actor"
CREATOR = "Creator"

# ============ Resource Type ==========
TV = "series"
MOVIE = "movie"

# ============ Spider Info ==========
HEADERS = {
    "authority": "unogs.com",
    "accept": "application/json",
    "x-requested-with": "XMLHttpRequest",
    "referrer": "http://unogs.com",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTcyMzcyMDYsIm5iZiI6MTU5NzIzNzIwNiwianRpIjoiYTM5MTk2MjAtNDgyOS00OGEzLWI3ZjItYWQwYmU0ODdiOGY3IiwiZXhwIjoxNTk3MzIzNjA2LCJpZGVudGl0eSI6IjE1OTcyMzcyMDYuNjMzIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.n3CkmoEktw30fyqxOtWuiE1BD4SHT5fjKpQ-qSjcTi4",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://unogs.com/search/?country_andorunique=or&start_year=1900&end_year=2020&end_rating=10&genrelist=&type=Series&audiosubtitle_andor=or&countrylist=78",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "cookie": "eucookie=stupideulaw; _ga=GA1.2.474332190.1597031572; countrylist=78; _gid=GA1.2.344253278.1597237206; authtoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTcyMzcyMDYsIm5iZiI6MTU5NzIzNzIwNiwianRpIjoiYTM5MTk2MjAtNDgyOS00OGEzLWI3ZjItYWQwYmU0ODdiOGY3IiwiZXhwIjoxNTk3MzIzNjA2LCJpZGVudGl0eSI6IjE1OTcyMzcyMDYuNjMzIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.n3CkmoEktw30fyqxOtWuiE1BD4SHT5fjKpQ-qSjcTi4",
}
DAILY_SCRAPE = "daily_scrape"
HISTORICAL_SCRAPE = "historical_scrape"

GENRE_ID_MAPPING = {
    "Dramas militares": 11,
    "Mockumentaries": 26,
    "Programas de TV y series": 83,
    "Sports Documentaries": 180,
    "Belgian Films": 262,
    "Independent Dramas": 384,
    "Anime Dramas": 452,
    "Gay & Lesbian Dramas": 500,
    "Films for ages 8 to 10": 561,
    "Children & Family Films": 783,
    "Steamy Dramas": 794,
    "Brazilian Films": 798,
    "Japanese Thrillers": 799,
    "Dark Comedies": 869,
    "Critically-acclaimed Independent Films": 875,
    "Critically-acclaimed Action & Adventure": 899,
    "Movies based on real life": 920,
    "Monster Films": 947,
    "Steamy Thrillers": 972,
    "British Comedies": 1009,
    "Biographical Movies": 1096,
    "Country & Western/Folk": 1105,
    "Travel & Adventure Documentaries": 1159,
    "Camp Films": 1252,
    "Dramas rom\\u00e1nticos": 1255,
    "Scandinavian Thrillers": 1321,
    "Acci\\u00f3n y aventuras": 1365,
    "Ciencia ficci\\u00f3n y fantas\\u00eda para TV": 1372,
    "Late Night Comedies": 1402,
    "Sci-Fi & Fantasy": 1492,
    "Action Sci-Fi & Fantasy": 1568,
    "Latin American Films": 1613,
    "Sci-Fi Horror Films": 1694,
    "Czech Movies": 1697,
    "Music": 1701,
    "Japanese Comedies": 1747,
    "British Thrillers": 1774,
    "Scandinavian Crime Films": 1884,
    "Korean Drama Movies": 1989,
    "Australian Comedies": 2030,
    "Acci\\u00f3n y aventuras militares": 2125,
    "Teen Movies": 2340,
    "Science & Nature Docs": 2595,
    "Action Anime": 2653,
    "Scandinavian Dramas": 2696,
    "Political Comedies": 2700,
    "Anime Sci-Fi": 2729,
    "Courtroom Dramas": 2748,
    "Mexican Dramas": 2757,
    "Spiritual Documentaries": 2760,
    "Japanese Dramas": 2893,
    "Anime Feature Films": 3063,
    "Biographical Dramas": 3179,
    "Soccer Non-fiction": 3215,
    "Independent Thrillers": 3269,
    "Rock & Pop": 3278,
    "Italian Comedies": 3300,
    "Alien Sci-Fi": 3327,
    "Romantic Gay & Lesbian Films": 3329,
    "Comedias adolescentes": 3519,
    "Biographical Documentaries": 3652,
    "Dramas basados en la vida real": 3653,
    "Social & Cultural Docs": 3675,
    "British Dramas": 3682,
    "African Films": 3761,
    "Romantic Films based on a book": 3830,
    "Sitcoms": 3903,
    "Sci-Fi Dramas": 3916,
    "Social Issue Dramas": 3947,
    "Chinese Films": 3960,
    "Critically Acclaimed Films": 3979,
    "Latin American Comedies": 3996,
    "Military Documentaries": 4006,
    "Crime Comedies": 4058,
    "Comedias independientes": 4195,
    "Italian Dramas": 4282,
    "Japanese Action & Adventure": 4344,
    "Misterios para TV": 4366,
    "Sports Films": 4370,
    "Brazilian Dramas": 4425,
    "Foreign Comedies": 4426,
    "Rockumentaries": 4649,
    "Animation": 4698,
    "Gay & Lesbian Documentaries": 4720,
    "Cult Sci-Fi & Fantasy": 4734,
    "Psychological Horror Films": 4809,
    "Miniseries": 4814,
    "African-American Comedies": 4906,
    "Satires": 4922,
    "Dramas baseados em livros": 4961,
    "Showbiz Dramas": 5012,
    "Indian Dramas": 5051,
    "Foreign Documentaries": 5161,
    "Australian Films": 5230,
    "Eastern European Films": 5254,
    "Sports Comedies": 5286,
    "Historical Documentaries": 5349,
    "Films for ages 5 to 7": 5455,
    "Comedias rom\\u00e1nticas": 5475,
    "Bollywood Films": 5480,
    "Psychological Thrillers": 5505,
    "Animal Tales": 5507,
    "Chinese Dramas": 5572,
    "TV Sketch Comedies": 5610,
    "Korean Films": 5685,
    "Raunchy Comedies": 5756,
    "Drama": 5763,
    "Crime Films": 5824,
    "Middle Eastern Movies": 5875,
    "Gay & Lesbian Films": 5977,
    "Japanese Sci-Fi & Fantasy": 6000,
    "Polish Thrillers": 6047,
    "British Crime Films": 6051,
    "Hip-Hop": 6073,
    "Polish Comedies": 6102,
    "Argentinian Films": 6133,
    "Goofy Comedies": 6197,
    "Critically Acclaimed Dramas": 6206,
    "Films for ages 2 to 4": 6218,
    "Polish Films": 6299,
    "Tearjerkers": 6384,
    "Comedias": 6548,
    "Dramas pol\\u00edticos": 6616,
    "Korean Comedies": 6626,
    "Martial Arts, Boxing & Wrestling": 6695,
    "Anime Series": 6721,
    "Latin American Dramas": 6763,
    "Films for ages 0 to 2": 6796,
    "Special Interest": 6814,
    "Documentaries": 6839,
    "Italian Thrillers": 6867,
    "Crime Dramas": 6889,
    "Creature Features": 6895,
    "Sci-Fi Adventure": 6926,
    "Films for ages 11 to 12": 6962,
    "Satanic Stories": 6998,
    "Political Documentaries": 7018,
    "Independent Films": 7077,
    "Gay & Lesbian Comedies": 7120,
    "Sports Dramas": 7243,
    "Anime": 7424,
    "Adventures": 7442,
    "TV Comedy Dramas": 7539,
    "Cult Films": 7627,
    "Film Noir": 7687,
    "Westerns": 7700,
    "Mexican Films": 7825,
    "Romantic Italian Films": 7908,
    "TV Animated Comedies": 7992,
    "B-Horror Films": 8195,
    "Italian Films": 8221,
    "Korean Action & Adventure": 8248,
    "Slasher & Serial Killer Movies": 8646,
    "Critically-acclaimed Documentaries": 8673,
    "Horror Films": 8711,
    "Pel\\u00edculas rom\\u00e1nticas": 8883,
    "Suspenses": 8933,
    "Martial Arts Films": 8985,
    "Chinese Action & Adventure": 8999,
    "Spy Thrillers": 9147,
    "Southeast Asian Films": 9196,
    "Chinese Comedies": 9229,
    "Romantic Tearjerkers": 9257,
    "Scandinavian Films": 9292,
    "Teen Dramas": 9299,
    "Anime Comedies": 9302,
    "Sports & Fitness": 9327,
    "Comedias de culto": 9434,
    "Urban & Dance": 9472,
    "Gory Horror Films": 9509,
    "Crime Action & Adventure": 9584,
    "Screwball Comedies": 9702,
    "Critically Acclaimed Comedies": 9736,
    "Fantasy": 9744,
    "Reality Programmes": 9833,
    "Dutch Dramas": 9873,
    "Crime Documentaries": 9875,
    "Movies based on Books": 9889,
    "Romantic Independent Films": 9916,
    "Indian Comedies": 9942,
    "Mist\\u00e9rios": 9994,
    "Religious Documentaries": 10005,
    "Films based on childrens books": 10056,
    "Documentary Programmes": 10105,
    "Comic Book and Superhero Films": 10118,
    "Slapstick Comedies": 10256,
    "Foreign Thrillers": 10306,
    "Comedy Programmes": 10375,
    "Japanese Films": 10398,
    "Indian Films": 10463,
    "Crime Thrillers": 10499,
    "Political Thrillers": 10504,
    "Dutch Films": 10606,
    "TV Soaps": 10634,
    "Educaci\\u00f3n y orientaci\\u00f3n": 10659,
    "Action & Adventure Programmes": 10673,
    "Spy Action & Adventure": 10702,
    "Australian Thrillers": 10719,
    "Japanese Horror Films": 10750,
    "Britische Filme": 10757,
    "African-American Stand-up Comedy": 10778,
    "Filipino Movies": 10869,
    "Cult Horror Films": 10944,
    "Sci-Fi Thrillers": 11014,
    "Irreverent Stand-up Comedy": 11039,
    "Australian Dramas": 11075,
    "Experimental Films": 11079,
    "Supernatural Thrillers": 11140,
    "Anime Fantasies": 11146,
    "Dibujos animados": 11177,
    "Korean Thrillers": 11283,
    "Stand-up Comedy": 11559,
    "Drama Programmes": 11714,
    "Polish Dramas": 11729,
    "Scandinavian Comedies": 11755,
    "Independent Action & Adventure": 11804,
    "Adult Animation": 11881,
    "Ambientadas en otra \\u00e9poca": 12123,
    "Baseball Films": 12339,
    "British Period Pieces": 12433,
    "Boxing Films": 12443,
    "Football Films": 12803,
    "20th Century Period Pieces": 12739,
    "Basketball Films": 12762,
    "Dramas based on contemporary literature": 12994,
    "Dramas based on classic literature": 13158,
    "Musicals": 13335,
    "Showbiz Musicals": 13573,
    "Latin American Documentaries": 15456,
    "Romantic Korean Movies": 16890,
    "Romantic Japanese Films": 17241,
    "Brazilian Comedies": 17648,
    "Australian Documentaries": 17672,
    "Showbiz Documentaries": 25485,
    "Military TV Programmes": 25804,
    "Political TV Shows": 25807,
    "Courtroom TV Dramas": 25955,
    "Crime TV Dramas": 26009,
    "Romantic TV Comedies": 26049,
    "Romantic TV Soaps": 26052,
    "Romantic TV Dramas": 26056,
    "Crime Docuseries": 26126,
    "Crime Programmes": 26146,
    "Romance Programmes": 26156,
    "Faith & Spirituality": 26835,
    "Heist Films": 27018,
    "Barne-TV": 27346,
    "Kids TV for ages 2 to 4": 27480,
    "Heist Action & Adventure": 27756,
    "Kids TV for ages 11 to 12": 27950,
    "Kids TV for ages 5 to 7": 28034,
    "Kids TV for ages 8 to 10": 28083,
    "Kids TV for ages 0 to 2": 28233,
    "Brazilian Documentaries": 28269,
    "Steamy Romance": 29281,
    "Art House Films": 29764,
    "Classic Dramas": 29809,
    "Gangster Action & Adventure": 30140,
    "Japanese Gangster Movies": 31244,
    "Classic Romantic Films": 31273,
    "Classic Films": 31574,
    "Classic Comedies": 31694,
    "Filmes sobre m\\u00e1fia": 31851,
    "Classic Japanese Movies": 31853,
    "Family Dramas": 31901,
    "Classic Musicals": 32392,
    "Medical TV Dramas": 34204,
    "Steamy Romantic Films": 35800,
    "Quirky Romance": 36103,
    "Crime TV Soaps": 37938,
    "Supernatural Horror Films": 42023,
    "Action Comedies": 43040,
    "Action Thrillers": 43048,
    "Deep Sea Horror Films": 45028,
    "Classic TV Programmes": 46553,
    "Classic British Films": 46560,
    "Classic Action & Adventure": 46576,
    "Classic Thrillers": 46588,
    "Classic Sci-Fi & Fantasy": 47147,
    "Classic Westerns": 47465,
    "Classic Horror Films": 48303,
    "Classic Children & Family Films": 48586,
    "Classic War Films": 48744,
    "Travel & Adventure Reality TV": 48762,
    "Nature & Ecology Documentaries": 48768,
    "Investigative Reality TV": 48785,
    "Science & Technology Documentaries": 49110,
    "Competition Reality TV": 49266,
    "Nature & Ecology Docuseries": 49547,
    "Science & Technology Docuseries": 50232,
    "Family Features": 51056,
    "Family Feature Animation": 51058,
    "Academy Award-Winning Films": 51063,
    "British Programmes": 52117,
    "British TV Mysteries": 52120,
    "British TV Comedies": 52140,
    "Teen Screams": 52147,
    "British TV Dramas": 52148,
    "Australian TV Programmes": 52387,
    "British Miniseries": 52508,
    "Science & Nature TV": 52780,
    "Faith & Spirituality Films": 52804,
    "Kids Music": 52843,
    "Familiecomedy": 52847,
    "Family Sci-Fi & Fantasy": 52849,
    "Music & Musicals": 52852,
    "Familieavonturen": 52855,
    "Epics": 52858,
    "TV Teen Dramas": 52904,
    "Silent Films": 53310,
    "Comic Book & Superhero TV": 53717,
    "Teen Romance": 53915,
    "Political TV Documentaries": 55087,
    "Canadian Dramas": 56169,
    "Canadian Comedies": 56174,
    "Canadian Documentaries": 56178,
    "Canadian Films": 56181,
    "Canadian Independent Films": 56184,
    "Hong Kong Movies": 58676,
    "French Dramas": 58677,
    "Danish Films": 58700,
    "Canadian TV Programmes": 58704,
    "French Documentaries": 58710,
    "Spanish Films": 58741,
    "Irish Films": 58750,
    "German Dramas": 58755,
    "Spanish Dramas": 58796,
    "French Thrillers": 58798,
    "Hindi-Language Films": 58806,
    "Franse films": 58807,
    "Family Animation": 58879,
    "German Films": 58886,
    "Romantic French Films": 58900,
    "French Comedies": 58905,
    "Punjabi-Language Movies": 58982,
    "Danish Comedies": 59169,
    "Indian Programmes": 59872,
    "Hungarian Movies": 59954,
    "Thai Comedies": 60724,
    "Teen Programmes": 60951,
    "Norwegian Comedies": 61132,
    "Thai Movies": 61205,
    "Spanish Comedies": 61330,
    "Romantic Danish Movies": 61656,
    "German Crime Movies": 61695,
    "Tamil-Language Films": 61904,
    "Swedish Films": 62016,
    "French TV Programmes": 62041,
    "Thai Dramas": 62116,
    "Swedish Dramas": 62140,
    "Norwegian Dramas": 62235,
    "Finnish Movies": 62285,
    "Norwegian Films": 62510,
    "Romantic Dutch Movies": 62752,
    "Italian TV Shows": 62866,
    "Swedish Comedies": 63092,
    "German Comedies": 63115,
    "German Documentaries": 63286,
    "Telugu-Language Movies": 63676,
    "Japanese Programmes": 64256,
    "German TV Shows": 65198,
    "Thai Horror Movies": 65209,
    "Disney Family Features": 65218,
    "Disney Movies": 65437,
    "Spanish Thrillers": 65558,
    "Japanese Kids TV": 65925,
    "Mexican TV Shows": 67644,
    "Disney": 67673,
    "Spanish-Language TV Shows": 67675,
    "Superheroes": 67698,
    "Latin American TV Shows": 67708,
    "Korean Programmes": 67879,
    "Korean TV Dramas": 68699,
    "Scandinavian Independent Movies": 69192,
    "Argentinian TV Shows": 69616,
    "Brazilian TV Shows": 69624,
    "Colombian Movies": 69636,
    "BAFTA Award-Winning Films": 69946,
    "WWII Films": 70023,
    "Historical Films": 71590,
    "Historical Dramas": 71591,
    "US TV Dramas": 72354,
    "US TV Documentaries": 72384,
    "American Programmes": 72404,
    "US TV Comedies": 72407,
    "Food & Travel TV": 72436,
    "Little Kids": 74253,
    "Cult TV Programmes": 74652,
    "Police Thrillers": 75390,
    "Police TV Shows": 75392,
    "Zombie Horror Films": 75405,
    "Mist\\u00e9rios policiais": 75415,
    "Police Action & Adventure": 75418,
    "Police Movies": 75436,
    "US Police TV Shows": 75445,
    "Time Travel Sci-Fi & Fantasy": 75448,
    "Dramas policiais": 75459,
    "Vampire Horror Films": 75804,
    "Werewolf Horror Films": 75930,
    "Modern Classic Movies": 76186,
    "Military & War Action & Adventure": 76501,
    "Military & War Dramas": 76507,
    "Military & War Movies": 76510,
    "Swedish TV Programmes": 76793,
    "Scandinavian TV": 76802,
    "Politically Incorrect Stand-up Comedy": 77230,
    "Asian Action Films": 77232,
    "Female Stand-up Comedy": 77599,
    "Asian Programmes": 78103,
    "Asian Movies": 78104,
    "Nordic Movies": 78141,
    "Comedy Jams": 78163,
    "Romantic Nordic Movies": 78250,
    "Internationaal": 78367,
    "Norwegian Crime Movies": 78463,
    "Finnish TV Shows": 78503,
    "Norwegian Thrillers": 78507,
    "Nordic Dramas": 78628,
    "Nordic TV Shows": 78634,
    "Nordic Comedies": 78655,
    "Police Detective Movies": 79049,
    "Dutch Comedies": 79871,
    "Hindi-Language TV Shows": 80307,
    "Chinese  Programmes": 80353,
    "True Crime Documentaries": 81050,
    "Golden Globe Award-winning Films": 82489,
    "Horror Programmes": 83059,
    "Music and Concert Films": 84483,
    "Brazilian Music & Musicals": 84488,
    "Brazilian Music and Concert Movies": 84489,
    "Latin American Music & Musicals": 88635,
    "Dutch TV Shows": 89442,
    "Dutch Children & Family Movies": 89513,
    "Horror Comedies": 89585,
    "European TV Shows": 89663,
    "European Movies": 89708,
    "Award-winning Dramas": 89804,
    "Thriller Programmes": 89811,
    "Award-films": 89844,
    "Blockbuster Movies": 90139,
    "Blockbuster Sci-Fi & Fantasy": 90166,
    "Blockbuster Action & Adventure": 90176,
    "Music & Concert Documentaries": 90361,
    "Festive Favourites": 107985,
    "Sci-Fi": 108533,
    "Kids Anime": 413820,
    "Romances de siempre": 502675,
    "Taiwanese TV Shows": 667429,
    "Cannes Film Festival Winners": 702387,
    "Japanese TV Comedies": 711366,
    "Japanese TV Dramas": 711367,
    "Kids Faith & Spirituality": 751423,
    "Actionkrimis": 788212,
    "Action": 801362,
    "Cannes Film Festival Award-winning Movies": 846810,
    "Berlin Film Festival Award-winning Movies": 846815,
    "International Thrillers": 852488,
    "International Action & Adventure": 852490,
    "International Sci-Fi & Fantasy": 852491,
    "International Comedies": 852492,
    "International Dramas": 852493,
    "International Documentaries": 852494,
    "Fantasy TV Shows": 1002031,
    "Turkish Movies": 1133133,
    "Nollywood Movies": 1138254,
    "Japanese TV Thrillers": 1138506,
    "US Movies": 1159493,
    "International TV Sci-Fi & Fantasy": 1192483,
    "Spanish TV Shows": 1193084,
    "International Programmes": 1195213,
    "International Historical TV Dramas": 1208621,
    "International TV Comedies": 1208951,
    "International TV Dramas": 1208954,
    "International Kids TV": 1218090,
    "Japanese Academy Award-winning Movies": 1293326,
    "Romantic International TV Shows": 1295410,
    "Turkish TV Shows": 1295701,
    "Laugh-Out-Loud Comedies": 1333288,
    "Japanese Period Dramas": 1402191,
    "Retro Anime": 1408777,
    "Tear-jerking Romantic Movies": 1412508,
    "Anime Sci-Fi & Fantasy": 1433679,
    "Romantic Japanese TV Shows": 1458609,
    "Taiwanese Movies": 1461905,
    "Japanese TV Sci-Fi & Fantasy": 1461923,
    "International TV Thrillers & Mysteries": 1461986,
    "Romantic International Movies": 1474327,
    "International Horror Movies": 1475312,
    "Middle Eastern TV Shows": 1476847,
    "Youth Drama": 1502288,
    "Food & Travel Docs": 1515639,
    "Stand-up & Chat Shows": 1516534,
    "Japanese Movies based on Comics": 1519160,
    "Slice of Life Anime": 1519826,
    "Romance Anime": 1522234,
    "Cyborg & Robot Anime": 1522235,
    "Japanese TV Reality & Variety": 1592212,
    "Polish TV Shows": 1622170,
    "Sports Anime": 1622375,
    "School Anime": 1623841,
    "Futuristic Sci-Fi": 1626246,
    "Japanese TV Shows Based on Comics": 1627743,
    "Japanese TV Documentaries": 1648599,
    "Japanese Documentary Movies": 1650093,
    "Japanese Youth Dramas": 1652485,
    "Romantic Youth Drama": 1655810,
    "Thriller & Horror Anime": 1663282,
    "TV Shows based on Books": 1819174,
    "Anime based on a Video Game": 1819777,
    "Owarai & Variety Shows": 1827694,
    "Cyberpunk": 1964512,
    "Reality, Variety & Talk Shows": 2070390,
    "Japanese Youth TV Dramas": 2070663,
    "Variety Entertainment": 2070675,
    "Tokusatsu Heroes": 2071073,
    "Family Watch Together TV": 2072262,
    "TV Shows based on Comics": 2192320,
    "Malaysian Programmes": 2199042,
    "Mainland Chinese Movies": 2199520,
    "Documentary Films": 2243108,
    "Family Cozy Time": 2245805,
    "Anime released in 2017": 2246382,
    "Blue Dragon Film Award-winning Movies": 2300054,
    "Baeksang Arts Awards Winners": 2300348,
    "Anime based on Comics": 2316199,
    "K-dramas": 2638104,
    "Social Issue TV Dramas": 2691116,
    "Japanese TV Series": 2691923,
    "Thai TV Shows": 2699150,
    "Lifestyle": 2738568,
    "Anime for Gamers": 2797624,
    "Indonesian Movies": 2867320,
    "Anime Based on Light Novels": 2867325,
    "Shounen Anime": 2867624,
    "TV Shows based on Manga": 2951909,
}

COUNTRY_NAME_ID_MAPPING = {
    "Argentina ": 21,
    "Australia ": 23,
    "Belgium ": 26,
    "Brazil ": 29,
    "Canada ": 33,
    "Colombia ": 36,
    "Czech Republic ": 307,
    "France ": 45,
    "Germany ": 39,
    "Greece ": 327,
    "Hong Kong ": 331,
    "Hungary ": 334,
    "Iceland ": 265,
    "India ": 337,
    "Israel ": 336,
    "Italy ": 269,
    "Japan ": 267,
    "Lithuania ": 357,
    "Malaysia ": 378,
    "Mexico ": 65,
    "Netherlands ": 67,
    "Poland ": 392,
    "Portugal ": 268,
    "Romania ": 400,
    "Russia": 402,
    "Singapore ": 408,
    "Slovakia ": 412,
    "South Africa": 447,
    "South Korea": 348,
    "Spain ": 270,
    "Sweden ": 73,
    "Switzerland ": 34,
    "Thailand ": 425,
    "Turkey ": 432,
    "United Kingdom": 46,
    "United States": 78,
}
COUNTRY_CODE_ID_MAPPING = {
    "AR": 21,
    "AU": 23,
    "BE": 26,
    "BR": 29,
    "CA": 33,
    "CO": 36,
    "CZ": 307,
    "FR": 45,
    "DE": 39,
    "GR": 327,
    "HK": 331,
    "HU": 334,
    "IS": 265,
    "IN": 337,
    "IL": 336,
    "IT": 269,
    "JP": 267,
    "LT": 357,
    "MY": 378,
    "MX": 65,
    "NL": 67,
    "PL": 392,
    "PT": 268,
    "RO": 400,
    "RU": 402,
    "SG": 408,
    "SK": 412,
    "ZA": 447,
    "KR": 348,
    "ES": 270,
    "SE": 73,
    "CH": 34,
    "TH": 425,
    "TR": 432,
    "GB": 46,
    "US": 78,
}
