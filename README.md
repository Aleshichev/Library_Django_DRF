# Library

## Django, PostgreSQL, Django REST Framework, Bootstrap5, Unit test, Selenium tests, Postman, Docker 

### Front-end

The front-end is implemented using Bootstrap 5. Templates have one common template base.html, from which all other pages are inherited.

### Back-end

The project consists of 4 applications: Authentication, Author, Book, Order. The system of registration and logging (admin, visitor) is realized. Depending on access rights, it is possible to get information, create, edit and delete users, authors, books, orders.
Forms are implemented using **Django forms**. Data is hidden using **django-environ** library.
System edit the site from the **Django admin page**. The project is connected to **PostgreSQL** database

### API

Api is implemented using **DRF**. Registration and logging system (admin, visitor). Authentication system via **token**. Depending on access rights, it is possible to receive information, create, edit, delete users, authors, books, orders. Tested via **Postman**.

### Tests

**Unittest:** All models Authentication, Author, Book, Order are tested - **64 tests** 

**Selenium tests:** Registration and logging system tested - **3 tests**

### Deploy

The project is deployed using Docker and has a file **Docker_compose.yml** which raises 2 containers - web server on gunicorn and connects PostgreSQL db.
