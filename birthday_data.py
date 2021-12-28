def get_birth_stones(birthday):
    # https://www.forbes.com/sites/trevornace/2017/07/02/birthstones-discover-birthstone-color-month/?sh=5c4a0dbd1f06
    # birth months 1-12
    # TODO get image of each gem

    birth_stones = ["0th Month", "Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl and Alexandrite",
                    "Ruby", "Peridot", "Sapphire", "Tourmaline and Opal", "Topaz or Citrine",
                    "Tanzanite, Zircon, and Turquoise"]
    return birth_stones[birthday.month]


def get_birth_flowers(birthday):
    # https://www.almanac.com/content/birth-month-flowers-and-their-meanings
    # TODO image of each flower
    # birth months 1-12
    birth_flowers = ["0th Month", "Carnation and Snowdrop", "Violet and Primrose", "Daffodil and Jonquil",
                     "Daisy and Sweet Pea", "Lily of the Valley or Hawthorn", "Rose and Honeysuckle",
                     "Larkspur and Water Lily", "Gladiolus and Poppy", "Aster and Morning Glory", "Marigold and Cosmos",
                     "Chrysanthemum", "Narcissus and Holly"]
    return birth_flowers[birthday.month]


def get_chinese_zodiac(birthday):
    # modulo year of birth by 12
    # TODO get image of each 'sign'/animal
    chinese_zodiac = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
                      'Goat']
    return chinese_zodiac[birthday.year % 12]


def get_western_horoscope(birthday):
    # TODO get daily horoscope?
    # IDE doesnt recognize 'match' keyword yet.
    if birthday.month == 1:
        if birthday.day >= 20:
            return "Aquarius"
        elif birthday.day <= 19:
            return "Capricorn"
    elif birthday.month == 2:
        if birthday.day >= 19:
            return "Pisces"
        elif birthday.day <= 18:
            return "Aquarius"
    elif birthday.month == 3:
        if birthday.day >= 21:
            return "Aries"
        elif birthday.day <= 20:
            return "Pisces"
    elif birthday.month == 4:
        if birthday.day >= 20:
            return "Taurus"
        elif birthday.day <= 20:
            return "Aries"
    elif birthday.month == 5:
        if birthday.day >= 21:
            return "Gemini"
        elif birthday.day <= 20:
            return "Taurus"
    elif birthday.month == 6:
        if birthday.day >= 21:
            return "Cancer"
        elif birthday.day <= 19:
            return "Gemini"
    elif birthday.month == 7:
        if birthday.day >= 20:
            return "Leo"
        elif birthday.day <= 19:
            return "Cancer"
    elif birthday.month == 8:
        if birthday.day >= 20:
            return "Virgo"
        elif birthday.day <= 19:
            return "Leo"
    elif birthday.month == 9:
        if birthday.day >= 20:
            return "Libra"
        elif birthday.day <= 19:
            return "Virgo"
    elif birthday.month == 10:
        if birthday.day >= 20:
            return "Scorpio"
        elif birthday.day <= 19:
            return "Libra"
    elif birthday.month == 11:
        if birthday.day >= 20:
            return "Sagittarius"
        elif birthday.day <= 19:
            return "Scorpio"
    elif birthday.month == 12:
        if birthday.day >= 20:
            return "Capricorn"
        elif birthday.day <= 19:
            return "Sagittarius"
    else:
        return "Invalid birth month for horoscope"

# TODO get 'this day in history' type thing. Grab headlines. Top 15 or whatever. Links, preferably.
