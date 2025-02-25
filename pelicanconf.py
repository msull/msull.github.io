AUTHOR = "Sully"
SITENAME = "Sully's Page"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

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
    "neighbors",  # find next, previous article
    "search",
]

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/msullenberger/"),
    ("github", "https://github.com/msull/"),
)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = "blog-output"
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ["images"]

TEMPLATE_PAGES = {
    "extra/api_explorer.html": "extra/api_explorer.html",
    "extra/pyodide.html": "extra/pyodide.html",
    "extra/imageEdit.html": "extra/imageEdit.html",
    "extra/aiconvo.html": "extra/aiconvo.html",
    # "src/resume.html": "dest/resume.html",
    # "src/contact.html": "dest/contact.html",
}
# EXTRA_PATH_METADATA = {
#     "": {"path": "api_explorer.html"},
#     "extra/pyodide.html": {"path": "pyodide.html"},
# }
THEME = "themes/elegant"

TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"

IGNORE_FILES = ["*.html"]

DIRECT_TEMPLATES = [
    "index",
    "tags",
    "categories",
    "authors",
    "archives",
    "404",
]
# DIRECT_TEMPLATES = [
#     "index",
#     "authors",
#     "categories",
#     "tags",
#     "archives",
#     "404",
# ]
