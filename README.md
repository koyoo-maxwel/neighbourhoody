# Neighbourhood Watch

<img src="/staticfiles/Screenshot from 2018-10-23 18-09-27.png" alt="">

## Description

A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User Stories

- A user can sign in to the application

- A user can create a profile and set profile with general information and location
- A user can view a list of different businesses in my neighborhood.
- A user can find contact Information public services such as health department and the police department.
- A user can post to as well as view posts on their neighborhood.
- A user can move out of a neighborhood.
- A user can only view information concerning their neighborhood.

## More Specifications

| Behavior                       |                        Input                         |                                                      Outcome |
| ------------------------------ | :--------------------------------------------------: | -----------------------------------------------------------: |
| Display of in form             |                         N/A                          |            Displays sign in form when a user visits the site |
| Logout current user            | click the logout link in the drop down in the navbar |                                      Displays the login form |
| Display of current user        |                         N/A                          | Displays name of current user in a Navbar when user signs in |
| Displays all the neighborhoods |              Click Hood link in navbar               |                  Displays all neighbourhoods in new template |
| Create New Business            |      Click the plus sign in the businesses page      |         Redirects to pages where users can create a business |

## Set Up and Installation

### Prerequisites

- Python 3.6.3
- Virtual environment
- Postgres Database
- Reliable Internet Connection

## Installation Process

- Copy the github repository link

In your terminal run the following commands

- $ git clone REPO-URL in your terminal
- $ cd watch
- $ python3.6 -m venv virtual
- $ touch .env ( to the file add :
  SECRET_KEY=<your secret key>
  DEBUG=True)
- $ source virtual/bin/activate
- $ python3.6 -m pip install -r requirements.txt
- $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'neighbourhood',
'USER': _POSTGRES_USERNAME_,
'PASSWORD': _POSTGRES_USERNAME_,
}
}

- $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )

## Known Bugs

nonnburgs for now so far

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

- HTML5/CSS
- Bootstrap4
- Python3.6
- Django
- Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through mburubeatricewanjiru@gmail.com or leave a comment here on github.

## License

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Beatrice Wanjiru](https://github.com/mburuBeatrice)
