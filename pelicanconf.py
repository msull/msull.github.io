AUTHOR = 'Sully'
SITENAME = "Sully's Blog"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

PLUGINS = [
    'neighbors', # find next, previous article
]

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/msullenberger/"),
)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = "blog-output"
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ["images"]
THEME = "themes/notmyidea"
# PAGE_PATHS = [
#     'pages'
# ]
# DIRECT_TEMPLATES = [
#     'index',
#     'authors',
#     'categories',
#     'tags',
#     'archives',
#     '404',
# ]
