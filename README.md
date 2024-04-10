# Django Book Shop

This is a Django-based web application for a book shop. The application allows users to view all books.

## Project Structure

The project is structured using Django's standard project layout with a separate application named `market` for handling the book-related functionality.

- `settings.py`: Contains the configuration for the Django project. It includes settings for the database, installed apps, middleware, templates, and static and media files.
- `views.py`: Defines two views. The `all_books` view retrieves all books from the database and renders them in a template named `book.html`.
- `urls.py`: Defines the URL patterns for the project. It includes the URLs from the `market` application and also serves media files in development mode.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
