class ArchiveItem:
    uid=""
    title=""
    year=0

    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return "(" + str(self.uid) + ", " + str(self.title) + ", " + str(self.year) + ")"

    def __eq__(self, other):
        return self.uid == other.uid

    def recent(n, year):
        if year >= (2025-n):
            return True
        else:
            return False

class Book(ArchiveItem):
    author = ""
    pages = 0

    def __init__(self, uid, title, year, author, pages):
        ArchiveItem.__init__(self, uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return super(Book, self), str(self.author), str(self.pages)

class Article(ArchiveItem):
    journal = ""
    doi = ""

    def __init__(self, uid, title, year, journal, doi):
        ArchiveItem.__init__(self, uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return super(Article, self), str(self.journal), str(self.doi)

class Podcast(ArchiveItem):
    host = ""
    duration = 0

    def __init__(self, uid, title, year, host, duration):
        ArchiveItem.__init__(self, uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return super(Podcast, self), str(self.host), str(self.duration)

def save_to_files(items, filename):
    with open(filename, "w") as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book",item.uid, item.title, item.year, item.author, item.pages)
            elif isinstance(item, Article):
                f.write(f"Article",item.uid, item.title, item.year, item.journal, item.doi)
            elif isinstance(item, Podcast):
                f.write(f"Podcast",item.uid, item.title, item.year, item.host, item.duration)

def load_from_file(filename):
    itemsList = []
    with open(filename, "r") as f:
        for line in f:
            line.strip().split(",")
            print(line)


save_to_files([],"newfle")
load_from_file("ckod.txt")
