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
    <a href="">View Demo</a>
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
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
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

<p align="right">(<a href="#top">back to top</a>)</p>


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

To get a local copy up and running follow these simple example steps.

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
5. In your terminal, switch to the main directory (cd web_store_app/) and run python manage.py runserver
6. In settings.py change the email data to yours if you want to work with the django send_email function. *

"*" means optional

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add some JavaScript to make the app more dynamic
- [ ] Improve the front-end


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are appreciated.

If you have a suggestion that would make this better, please follow these instructions:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b branch_name/some_text`)
3. Commit your Changes (`git commit -m 'Commit name'`)
4. Push to the Branch (`git push origin branch_name/some_text`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Ioannis Kolokotronis - ioanniskolokotronis1@gmail.com

Project Link: [https://github.com/ikolokotronis/Web-Store-App](https://github.com/ikolokotronis/Web-Store-App)

<p align="right">(<a href="#top">back to top</a>)</p>
