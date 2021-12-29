## Prune links with bit.ly like a pro

Get handy shortened links from your long bulky url. Alternatively,
find out the number of times the bitlink was clicked

To get a short link or number of clicks, run the script with your link
as a parameter:

```
python3 main.py yourLinkHere
```

### Installing

You should have python3 working in your system. Use `pip` (or `pip3` in
case of dependency conflicts with python2):

```
pip install -r requirements.txt
```

[virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for the means of project isolation

### Environmental varibles

To run the script, you need to obtain a bitly access token (refer to
[Bitly documentation](https://dev.bitly.com/get_started.html) for details)
It should look something like `17c09e20ad155405123ac1977542fecf00231da7`.
Store it in the .env file placed in the proect root folder; in the file,
name i as BITLY_TOKEN like this:
```
BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```

### Project objective

The project is purely educational made during web developers course
in [dvmn.org](https://dvmn.org)