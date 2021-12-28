from flask import Flask
from flask_restful import Api, Resource, abort
import json
import datetime
# my files
from birthday_data import *

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        home_message = "This is the homepage of the birthday stats API, developed by Chase Traver.\n" \
                    "To use me, put your birthday in YYYYMMDD format in the url after a slash, e.g. " \
                    "https://birthday-facts-api.herokuapp.com/19970715\n" \
                    "You can also narrow your results from getting everything related to your birthday to one resource" \
                    "by putting the resource you want in a slash after your birthday, e.g. " \
                    "https://birthday-facts-api.herokuapp.com/19970715/chinesezodiac \n " \
                    "You can also request multiple resources simultaneously by using & to chain them, e.g. " \
                    "https://birthday-facts-api.herokuapp.com/19970715/chinesezodiac&birthflowers\n"\
                    "Source code can be found at this location: https://github.com/chasetraver/birthday-api"
        return home_message, 200


class BirthdayStats(Resource):
    # default to returning all birthday stats if one isnt specified.
    def get(self, birthday: str) -> (str, int):

        birthday = format_birthday(birthday)

        stones = get_birth_stones(birthday)
        zodiac = get_chinese_zodiac(birthday)
        flowers = get_birth_flowers(birthday)
        horoscope = get_western_horoscope(birthday)
        birthdayjson = {
            "birthday": str(birthday.strftime("%b %d %Y")),
            "birth stones": stones,
            "chinese zodiac": zodiac,
            "birth flowers": flowers,
            "western horoscope": horoscope
        }
        birthdayjson = json.dumps(birthdayjson)
        return birthdayjson, 200


class TargetBirthdayStat(Resource):

    def get(self, birthday: str, target: str):
        target = target.lower()
        # allow for multiple stats to be targeted via the use of & to chain them
        targets = target.split('&')
        birthday = format_birthday(birthday)
        birthdaydict = {"birthday": str(birthday.strftime("%b %d %Y"))}
        for target in targets:
            # remove separator character for each separate statement.
            target.lstrip('&')
            if target in {"stones", "birthstones", "birth-stones"}:
                birthdaydict['birth stones'] = get_birth_stones(birthday)
            elif target in {"zodiac", "chinesezodiac", "chinese-zodiac"}:
                birthdaydict['chinese zodiac'] = get_chinese_zodiac(birthday)
            elif target in {"flowers", "birthdayflowers", "birthday-flowers"}:
                birthdaydict["birth flowers"] = get_birth_flowers(birthday)
            elif target in {"horoscope", "sign", "westernhoroscope", "western-horoscope"}:
                birthdaydict['horoscope'] = get_western_horoscope(birthday)
            else:
                abort(400, message="Invalid target(s) for birthday stats. Valid targets are: stones, zodiac, flowers, "
                                   "or horoscope.\nYou can access multiple simultaneously via linking them via '&', e.g."
                                   "'stones&flowers'.")
        birthdayjson = json.dumps(birthdaydict)
        return birthdayjson, 200


def invalid_format_abort():
    abort(400, message="Invalid date format. YYYYMMDD, YYYY/MM/DD, or YYYY-MM-DD are accepted.")


def format_birthday(birthday)->datetime.date:
    # handle cases where format is YYYY%MM%DD where % is a divider
    if len(birthday) == 10:
        if not birthday[4].isnumeric():
            # get any nonnumeric character that is functioning as a divider after YYYY
            divider = birthday[4]
            year, month, day, *_ = birthday.split(divider)
            # data converted from string to int, and remove leading zeroes
            day = int(day.lstrip("0"))
            month = int(month.lstrip("0"))
            # strip zeroes from year to support millennia old vampires
            year = int(year.lstrip("0"))
        else:
            invalid_format_abort()
    # handle just YYYYMMDD
    elif len(birthday) == 8:
        # data converted from string to int, and remove leading zeroes
        day = int(birthday[6:8].lstrip("0"))
        month = int(birthday[4:6].lstrip("0"))
        # strip zeroes from year to support millennia old vampires
        year = int(birthday[0:4].lstrip("0"))
    else:
        invalid_format_abort()
    try:
        birthday = datetime.date(year, month, day)
    except ValueError:
        invalid_format_abort()
    return birthday


# birthday format is YYYY-MM-DD
api.add_resource(Home, "/")
api.add_resource(BirthdayStats, "/<string:birthday>")
api.add_resource(TargetBirthdayStat, "/<string:birthday>/<string:target>")

if __name__ == '__main__':
    app.run()
