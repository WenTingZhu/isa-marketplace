# isa-marketplace

### UVA Ridesharing & Delivery Services

This repo contains three independent django applications and a database.
Folders
* experience
* models
* front-end
* mysql

Each has its own folder.


### Setup
1. make sure you have docker and docker-compose installed
2. git clone https://github.com/WenTingZhu/isa-marketplace.git
3. cd isa-marketplace
4. docker-compose up
5. Quit by pressing *ctr-c* This sets up the initial connection between the different docker containers
4. docker-compose run models python manage.py makemigrations
5. docker-compose run models python manage.py migrate
6. docker-compose up
7. You're all done! You can edit the isa-marketplace/rideshare directory. Your changes will be applied in the docker container, and you will see them live on the browser at http://localhost:8000

If you are going to be creating applications and projects or performing any Django operations on your local computer, you may want to create a virtual environment.
1. cd isa-marketplace
2. pip install virtualenv
3. virtualenv ENV -p `which python3.5`
  * I am using ` ` not ' '. It can be found on the top left of most keyboards. It is usually left of the 1. It is paired with ~.
  * requires python3.5
  * ENV folder (and therefore your virtualenv) will **NOT** be pushed to github since it is ignored in .gitignore
4. source ENV/bin/activate
5. pip install django==1.8
6. pip install mod_wsgi
  * it may be difficult to install mod_wsgi. If so, then go ahead and go into the setting.py file for the project that you want to work on and simply comment out 'mod_wsgi.server' from INSTALLED_APPS.
  * once you are done modifying the structure of the app, you want to uncomment 'mod_wsgi.server'

* Debug: bash start.sh --reset-hard

* Testing: sudo docker-compose run models python manage.py test


### User stories:
- As a driver, I want to enter a preset location to which I will be driving so that riders can see and request a ride.
- As a driver, I want to set a limit of the number of riders I can take with me.
- As a driver, I want to have the option for choosing to drop people off at a predefined central location or a specific location.
- As a driver, I want to be payed more for dropping off people at home.
- As a driver, I want to make sure that the riders can be relied on to pay for the ride.
- As a driver, I want to let people know that I am going at a scheduled future time.
- As a driver, I want to know where I need to know where I am dropping people off if they chose specific locations.
- As a driver, I want to be able to specify my own pricing.
- As a rider, I want to make sure that the driver is a UVA student.
- As a rider, I want to be able to choose whether I want to be dropped off at a central location or a specific location if I have that option.
- As a rider, I want to pay online.
- As a rider, I want to be able to get a ride at a scheduled future time.
- As someone who receives/sends goods, I want to make sure the driver does not open my packages.
- As someone who receives/sends goods, I want to receive/send goods faster and safer than traditional mail service.

### Models: https://docs.google.com/document/d/11De7BG0eWag_XKodsec3UjT_76n3ddE1yZ8IutVF4eg/edit


### Rides page
* list of rides
  * driver
  * number of available seats
  * from, to
  * map -> will be on details page for a given ride
  * departure time
  * button to ask for ride
  * clicking on ride row in table should take you to details page for ride
* current user information -> display name at top right corner
* go to home page button
* menu -> profile page, home page, list of rides page,
* ride details page
