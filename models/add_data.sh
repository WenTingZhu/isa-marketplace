
# create users
curl -H "Content-Type: application/json" -X PUT -d '{"email":"johndoe@email.com","password":"password", "first_name": "John", "last_name": "Doe", "phone": "7777777777", "school":"UVA"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"ho2es@virginia.com","password":"****", "first_name": "Himanshu", "last_name": "Ojha", "phone": "5712862986", "school":"UT Texas"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"rocko@gmail.com","password":"adf", "first_name": "John", "last_name": "Doe", "phone": "5839862986", "school":"Columbia"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"revanth@kolli.com","password":"asdf", "first_name": "John", "last_name": "Doe", "phone": "397871673", "school":"Duke"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"wendyzhu@yahoo.com","password":"kfosk", "first_name": "John", "last_name": "Doe", "phone": "123456789", "school":"Chantilly"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"turbo@charge.com","password":"fsdf", "first_name": "John", "last_name": "Doe", "phone": "987654321", "school":"Some chinese school in china"}' http://localhost:8000/api/v1/accounts/user/
curl -H "Content-Type: application/json" -X PUT -d '{"email":"max@outlook.com","password":"fefefef", "first_name": "John", "last_name": "Doe", "phone": "192837465", "school":"Ebay"}' http://localhost:8000/api/v1/accounts/user/

# create rides
curl -H "Content-Type: application/json" -X PUT -d '{"driver":"1","open_seats":3, "departure": "2016-01-20 05:30"}' http://localhost:8000/api/v1/ride/ride/
curl -H "Content-Type: application/json" -X PUT -d '{"driver":"1","open_seats":1, "departure": "2016-02-20 06:30"}' http://localhost:8000/api/v1/ride/ride/
curl -H "Content-Type: application/json" -X PUT -d '{"driver":"1","open_seats":4, "departure": "2016-01-21 05:30"}' http://localhost:8000/api/v1/ride/ride/

curl -H "Content-Type: application/json" -X PUT -d '{"driver":"2","open_seats":1, "departure": "2016-02-25 05:00"}' http://localhost:8000/api/v1/ride/ride/
curl -H "Content-Type: application/json" -X PUT -d '{"driver":"3","open_seats":2, "departure": "2016-01-01 06:30"}' http://localhost:8000/api/v1/ride/ride/
curl -H "Content-Type: application/json" -X PUT -d '{"driver":"5","open_seats":3, "departure": "2016-01-20 06:00"}' http://localhost:8000/api/v1/ride/ride/

# dump data into file (to see if it worked)
# python manage.py dumpdata > fixtures/data.json
