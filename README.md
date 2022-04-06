<div id="top"></div>


<br />
<div align="center">

<h3 align="center">Web Store App</h3>

  <p align="center">
    A web store application made with django
    <br />
    <a href="https://github.com/ikolokotronis/Web-Store-App"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/ikolokotronis/Web-Store-App/issues">Report Bug</a>
    ·
    <a href="https://github.com/ikolokotronis/Web-Store-App/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#key-functionalities">Key functionalities</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#own-store-setup">Own store setup</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


This is my Coders Lab bootcamp graduation project. It's main goal is to make a web application for any kind of store.  
Originally it was written to be a music store, but it could be anything you want, based on what you add to the database.  
Please mark that I used a logo and some ad's for visual purposes, which refer to the music store theme.  
Also, please note that I had to make some logical decisions due to the application's overall theme, which may not be applicable to other themes.  
<b>Want to set up your own store?</b> Go to <a href="#own-store-setup">this</a> section

<p align="right">(<a href="#top">back to top</a>)</p>


## Key functionalities
* Shopping cart
* Viewed recently (based on session)
* Bestsellers, new products and recently viewed products are displayed in landing page
* Newsletter
* Forgot password
* Discount codes
* Wallet
* Authentication system


## Demo
<i>Not available yet</i>


### Built With

* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Pytest](https://docs.pytest.org/)
* [Six](https://six.readthedocs.io/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Django mathfilters](https://pypi.org/project/django-mathfilters/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is a list of things you need in order to use the software and how to install them.

* pip
  ```sh
  pip install django
  ```
  ```sh
  pip install psycopg2-binary
  ```
  ```sh
  pip install six
  ```
  ```sh
  pip install django-mathfilters
  ```
  ```sh
  pip install pillow
  ```

### Installation

1. Make sure you have python installed in your sytem
2. Clone the repo
   ```sh
   git clone https://github.com/ikolokotronis/Web-Store-App
   ```
3. Install PIP packages(shown above)
4. Enter your database settings in settings.py. Here is an example if you want to use PostgreSQL:
   ```python
   DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'db_name_here',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'user_name_here',
        'PASSWORD': 'password_here',
    }
    }
   ```
5. In settings.py change the email data to yours if you want to work with the django send_email function. *
6. In your terminal, switch to the main directory (cd web_store_app/) and run python manage.py runserver

"*" means optional

<p align="right">(<a href="#top">back to top</a>)</p>


## Own store setup
Want to setup your own store? Follow these instructions:
1. Install the project locally (Explained <a href="#installation">here</a>)
2. Update the database with your data, the following structure is recomended: 
* Up to 5 categories
* Up to 3 subcategories in each category
* Up to 6 products in each subcategory
* <b>Important!</b> Remember to set up relations. Each relation has it's own model in the DB. I recommend using django admin for that. (For a server on localhost the address is 127.0.0.1/admin/).
3. Replace the logo, ads, title and information with whatever you choose. Look at them as an inspiration for your ideas.
4. You're good to go! 


<!-- CONTACT -->
## Contact

Ioannis Kolokotronis - ioanniskolokotronis1@gmail.com

Project Link: [https://github.com/ikolokotronis/Web-Store-App](https://github.com/ikolokotronis/Web-Store-App)

<p align="right">(<a href="#top">back to top</a>)</p>
