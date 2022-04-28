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


This is my bootcamp graduation project.  
A model for a online shop with musical instruments. Comes with a backend built in django & a frontend music-themed. 

<b>Store setup is <a href="#own-store-setup">here</a></b>

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


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

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
6. Open terminal and run python manage.py runserver

"*" means optional

<p align="right">(<a href="#top">back to top</a>)</p>


## Store setup
1. Install the project locally (Explained <a href="#installation">here</a>)
2. Go to the django admin panel (127.0.0.1/admin/ on localhost) and fill the database using the following structure: 
* Up to 5 categories
* Up to 3 subcategories in each category
* Up to 6 products in each subcategory
* <b>Important!</b> Remember to set up relation models in django admin


<!-- CONTACT -->
## Contact

Ioannis Kolokotronis - ioanniskolokotronis1@gmail.com

Project Link: [https://github.com/ikolokotronis/Web-Store-App](https://github.com/ikolokotronis/Web-Store-App)

<p align="right">(<a href="#top">back to top</a>)</p>
