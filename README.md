<div id="top"></div>


<br />
<div align="center">

<h3 align="center">Web Store App</h3>

  <p align="center">
    <a href="#demo">View Demo</a>
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


This is my bootcamp graduation project. Register and buy music instruments with fake money or personalize the app to create your own store using your ideas. 

<b>Want to set up your own store?</b> Go to <a href="#own-store-setup">this</a> section

<p align="right">(<a href="#top">back to top</a>)</p>


## Key functionalities
* Shopping cart
* Viewed recently (session based)
* Bestsellers, new products and recently viewed products are displayed in landing page
* Newsletter
* Forgot password functionality 
* Discount functionality 
* Wallet
* Auth system
* Personal account 


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
3. Enter your database settings in settings.py. Here is an example if you want to use PostgreSQL:
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
6. In your terminal run python manage.py runserver

"*" means optional

<p align="right">(<a href="#top">back to top</a>)</p>


## Own store setup
Want to setup your own store? Follow these instructions:
1. Install the project locally (Explained <a href="#installation">here</a>)
2. Go to the django admin panel (127.0.0.1/admin/ on localhost) and fill the database with your data, the following structure is recomended: 
* Up to 5 categories
* Up to 3 subcategories in each category
* Up to 6 products in each subcategory
* <b>Important!</b> Remember to set up relation models in django admin
3. In base.html files replace the logo, ads, title and hard coded information with whatever you want, and you're good to go!


<!-- CONTACT -->
## Contact

Ioannis Kolokotronis - ioanniskolokotronis1@gmail.com

Project Link: [https://github.com/ikolokotronis/Web-Store-App](https://github.com/ikolokotronis/Web-Store-App)

<p align="right">(<a href="#top">back to top</a>)</p>
