# Pinakothek

This web application provides the ability to download, store and view photos and video content. It was created using Django as a backend and provides a user-friendly interface for users to work with media files.

## Features

- **Authorization and Authentication:** Register new users and log in for existing ones through Django's built-in authentication system.
- **Content Management:** Uploading, deleting, editing, and describing media files.
- **Content Display:** Gallery for viewing photos and videos with pagination and filtering support.
- **Media Processing:** Pillow and FFmpeg libraries are used to work with images and videos, respectively.
- **Data Storage:** SQLite is used to store information about uploaded files.

## Requirements

- Python 3.x
- Django
- Pillow
- FFmpeg
- SQLite

## Installation and Launch

1. Clone the repository:
`` bash
git clone https://github.com/your_username/your_project.git
```
2. Install dependencies:
`` bash
pip install -r requirements.txt
``
3. Perform database migrations:
`` bash
python manage.py migrate
``
4. Start the server:
`` bash
python manage.py runserver
``

## Usage

1. Register a new account or log in to an existing one.
2. Upload photos and videos via the app interface.
3. View, edit and manage content through the gallery.


## Additional Information

- For questions or help, contact [the author](mailto:cima19056@gmail.com ).