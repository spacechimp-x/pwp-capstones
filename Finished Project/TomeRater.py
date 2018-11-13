class User(object):
    def __init__(self, name, email):
        self.name = name    #string
        self.email = email  #string
        self.books = {}     #An empty dictionary that will map a Book object.

    # Returns the email address associated with the user.
    def get_email(self):
        return self.email

    # Changes the email associated with the user and prints update message.
    def change_email(self, address):
        self.email = address
        print("The user's email address has been updated.")

    # Returns a string to print out the user object.
    def __repr__(self):
        return "User: {name}; email: {email}; books read: {number}".format(name=self.name, email=self.email, number=len(self.books))

    # Defines comparison between users.
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    # Takes in 'book' and an optional parameter 'rating' and adds a key:value pair to self.books where
    # the key is 'book' and the value is 'rating'.
    def read_book(self, book, rating="None"):
        self.books[book] = rating
        return self.books

    # Iterates through all of the values in self.books and calculates the average rating.
    # Returns average.
    def get_average_rating(self):
        combined_ratings = 0
        number_of_books = len(self.books)
        for rating in self.books.values():
            if rating == "None":
                combined_ratings += 0
            else:
                combined_ratings += rating
        return combined_ratings / number_of_books

class Book:
    def __init__(self, title, isbn):
        self.title = title  #string
        self.isbn = isbn    #number
        self.ratings = []

    # Returns a string with the title.
    def __repr__(self):
        return "{title}".format(title=self.title)

    # Returns the title of the book.
    def get_title(self):
        return self.title

    # Returns the ISBN of the book.
    def get_isbn(self):
        return self.isbn

    # Changes the ISBN of the book and prints and update message.
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book's ISBN has been updated to the new number.")

    # Adds a rating to the self.ratings list for the book.
    def add_rating(self, rating):
        if rating == "None":
            pass
        else:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    # Defines comparison between books.
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    # Iterates through all of the values in the list self.ratings; calculates and returns average.
    def get_average_rating(self):
        combined_ratings = 0
        number_of_ratings = len(self.ratings)
        for rating in self.ratings:
            combined_ratings += rating
        return combined_ratings / number_of_ratings

    # Makes sure that the book object is hashable.
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author    #string

    # Returns the author of the book.
    def get_author(self):
         return self.author

    # Returns a string with the title and author.
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject  #string
        self.level = level      #string

    # Returns the subject of the book.
    def get_subject(self):
        return self.subject

    # Returns the level of the book.
    def get_level(self):
        return self.level

    # Returns a string with the title, level, and subject of the book.
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}         # Maps a user's email to the corresponding User object.
        self.books = {}         # Maps a Book object to the number of Users that have read it.

    # Takes a 'title' and 'isbn' and creates a new book with that title and ISBN. Returns this book object.
    def create_book(self, title, isbn):
        return Book(title, isbn)

    # Takes 'title', 'author', and 'isbn' and creates a new Fiction with that information. Returns Fiction object.
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    # Takes 'title', 'author', 'level', and 'isbn' and creates a new Fiction with that info. Returns Non_Fiction object.
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating="None"):
        # If the User object doesn't exist, an error message will appear.
        if not self.users.get(email):
            print("No user with email {email}!".format(email=email))
        # If User object exists, maps a Book object to a corresponding User object's 'self.books' dictionary.
        # Adds the book to the 'self.books' dictionary; mapped to the number of Users that have read it.
        else:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if not self.books.get(book):
                self.books[book] = 1
            else:
                self.books[book] += 1

    # Creates a new user object from 'name' and 'email'.
    # Then, if 'user_books' is provided , it loops through the list and adds each Book to the user.
    def add_user(self, name, email, user_books="None"):
        user = User(name, email)
        self.users[email] = user
        if not user_books == "None":
            for book in user_books:
                self.add_book_to_user(book, email, rating="None")

    # Prints all of the books in the self.books dictionary.
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    # Prints all of the users in the self.users dictionary.
    def print_users(self):
        for user in self.users.values():
            print(user)

    # Iterates through all of the books in self.books and returns teh book that has been read the most.
    def most_read_book(self):
        times_read = 0
        most_read = ""
        for book, tally in self.books.items():
            if tally > times_read:
                times_read = tally
                most_read = book
        return most_read

    # Iterates through all of the books in self.books and returns the book with the highest avg rating.
    def highest_rated_book(self):
        highest_rated = ""
        highest_rating = 0
        for book in self.books.keys():
            book_rating = book.get_average_rating()
            if book_rating > highest_rating:
                highest_rating = book_rating
                highest_rated = book
        return highest_rated

    # Iterates through all of the users in self.users and returns the user that has the highest average rating.
    def most_positive_user(self):
        highest_rater = ""
        highest_rating = 0
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if average_rating > highest_rating:
                highest_rating = average_rating
                highest_rater = user
        return highest_rater
