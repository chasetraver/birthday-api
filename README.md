Live at https://birthday-facts-api.herokuapp.com as of 12/28/2021

This is an api that you can run from main.py.
It uses the flask and flask_restful libraries to return birthday facts as JSON, such as:
your horoscope sign, 
birthstone, 
flowers associated with your birth month, 
and/or the associated Chinese zodiac sign.


To use me, put your birthday in YYYYMMDD format in the url after a slash, e.g.
  hostsite/19970715

You can also narrow your results from getting everything related to your birthday to one resource
by putting the resource you want in a slash after your birthday, e.g.
  hostsite/19970715/chinesezodiac

You can also request multiple resources simultaneously by using & to chain them, e.g.
  hostsite/19970715/chinesezodiac&birthflowers
