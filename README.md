# isa-marketplace

### UVA Ridesharing & Delivery Services

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


### Setup
1. git clone https://github.com/WenTingZhu/isa-marketplace.git
2. docker-compose run models python manage.py makemigrations
3. docker-compose run models python manage.py migrate
4. docker-compose up
