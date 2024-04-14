
# Library

This Django project, named "MyBookShop", serves as a virtual library for managing books.

## Overview

The project consists of the following components:


### Author Management

- Add, update, and delete authors.
- View detailed information about each author, including:
  - Name
  - Birth date
  - Birth place
  - Death date (if applicable)
  - Death place (if applicable)
- List all authors with their details.

### Models

In our `Book` model, we have a `category` field which is a `ManyToManyField`. This means a book can belong to multiple categories and a category can have multiple books. Here's how it's defined:

## Features

### Home Page

The home page is the landing page of the application. It displays a list of featured books and authors.

### Book Page

The book page displays a list of all the books available in the shop. Each book is displayed as a list item with the book information on the left and the cover on the right. The book page also includes a pagination feature for easy navigation through the list of books.
Each book has a cover type attribute. This attribute can be used to filter the books on the book page.

### Book Filters

The book page includes a filter form. Users can filter books by cover type, author's name, maximum price. The filter is applied across all pages of the book list.



### Author Page

The author page displays a list of all the authors whose books are available in the shop. Each author is displayed in a grid layout with a portrait and some details about the author.


1. **Models:** Defined in `market/models.py`, the `Book` model includes fields such as title, author, category, year, price, cover, created_at, and updated_at.

2. **Views:**
    - `all_books`: Renders all books paginated with 3 books per page.
    - `home_page`: Renders the main page of the application.
    - `BookDetailView`: Detail view for a specific book.

3. **Templates:**
    - `main.html`: Base template for the application layout.
    - `header.html`: Header section including navigation links.
    - `book_list.html`: Template for displaying a list of books with pagination.
    - `book_detail.html`: Template for displaying details of a single book.

4. **URLs:** Defined in `market/urls.py`, URL patterns route requests to appropriate views.

5. **Pagination:** Implemented using Django's `Paginator` class to display books in paginated format.

6. **Styling:** Basic CSS styles are included inline within HTML templates for simplicity.

## Usage

1. Ensure Django is installed.
2. Navigate to the project directory and run:
    ```bash
    python manage.py runserver
    ```
3. Visit `http://127.0.0.1:8000/` in your web browser to access the library application.

## Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.




