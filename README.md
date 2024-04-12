
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




