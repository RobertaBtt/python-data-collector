# Template - Small Python Service connection to a DB and Dependency Inversion



Use this template everytime you want to quick set up a Python service.

This template is able to 
- connect to different Database (inheriting from ConnectionAbstract) 
for now is implemented the connection to a **SQLite** Database

- This service is also prepared to read as an input different file format, 
for now it is implemented only the **JSON** format.

- This service is able to read from file of type **.conf** and from files of type **.env**

- This service has two endpoints:
    - **main.py**
    - **web.py**

From both of these endpoints is possible to call the different services that
has been injected in the Container.

------------------

This projects follows the **Repository Pattern**.

It is an abstraction over persistent storage. It hides the details of data access.


In the dependency inversion the domain model is free from the Infrastructure concerns.

Repository pattern is a simple abstraction
around permanent storage. Repository gives you the illusion of a collection of in-memory objects.

![RepositoryPattern.jpg](static%2FRepositoryPattern.jpg)

The Service Layer orchestrate our workflow and defines the Use Cases of our systems.
The service layer will become the main way to our app.

This is the architecture **Layered Architecture**, of type monolith.

Components are organized into logical horizontal layers and every layer consists of 4 standards layers:

* Presentation
* Business
* Persistence
* Database

![Layers.jpg](static%2FLayers.jpg)

_Layers of isolation: changes made in one layer in the architecture, generally don't impact
or affect components in other layers.
Each layer is independent of the others._



### Environment - POSIX
**Install python3. Last Version is now 3.10.6**

**Create a hidden folder with the local python environment with this command**

`python3 -m venv .local_venv`


**Activate the environment**

`source .local_venv/bin/activate`

**Install the requirements**

`pip3 install -r requirements.txt`

**Run tests**

`python3 -m pytest tests/ -v`

**Run Flask Web**

`python3 web.py`

## Test the endpoint locally:

`curl -X POST http://127.0.0.1:8080/webhook/djsnckvj --header 'Content-Type: application/json' --header 'Hmac-SHA256: SgS9OYxlwwM75ttkEJSrMJvVpoXTLrHkWQAJrgFx7LY='  --data '{"event": "SERVER_UPDATE"}'
`

With **Postman**:

![postman-body.jpg](static%2Fpostman-body.jpg)

![postman-header.jpg](static%2Fpostman-header.jpg)


**Business** endpoint with Curl


`curl -X POST http://127.0.0.1:8080/webhook/djsnckvj --header 'Content-Type: application/json' --header 'Hmac-SHA256: nbulYuM2wST8rtdF39opCYnLoNQozjYgOHiaastNhLs='  --data '{"job_latitude":"37.3333333333","fleet_email":"JoehRichmondAndAssociate@example.com","job_id":"236365","job_state":"Successful","has_delivery":"1","job_pickup_latitude":"30.2222222222","job_pickup_name":"JonRichmondPeppy","job_status":"2","sign_image":"https://flolaLux.net","customer_username":"username","job_longitude":"-122.0000000000","job_pickup_longitude":"-122.0000000","total_distance_travelled":"0","total_time_spent_at_task_till_completion":"15","has_pickup":"1","job_token":"304958304958304958","job_pickup_address":"5849GjfoJFOMSMAvenue","job_pickup_phone":"+43574830485","fleet_id":"3635","fleet_name":"Postino","job_pickup_email":"test@email.com","task_history":[{"id":235973,"job_id":85185,"fleet_id":3829,"fleet_name":"bobbysingh","latitude":"30.7192552","longitude":"76.8102558","type":"state_changed","description":"StatusupdatedfromAssignedtoUnassigned","creation_datetime":"2016-01-11T09:34:17.000Z"},{"id":236365,"job_id":85185,"fleet_id":3635,"fleet_name":"PeppyB","latitude":"30.7193512","longitude":"76.8102679","type":"state_changed","description":"Acceptedat","creation_datetime":"2016-01-11T12:11:02.000Z"}],"transaction_fields":{"fare_amount":456.78,"driver_amount":123.45,"added_fees":0}}'
`


### This service needs a RabbitMQ container.


`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management`



### When a delivery is successful? ###

Those are the fields to take in consideration for computing a successful ride,
that has transactions of money and make the business sustainable.

id	-> auto generated
UUID -> created ex-novo during the creation
driver_name	String -> fleet_name from task history
amount_total	decimal = driver_amount + fare_amount + added_fees
amount_driver	decimal -> from driver_amount
timestamp	Timestamp -> from the first task history item.
distance	decimal -> total_distance_travelled ***
time_spent	decimal -> total_time_spent_at_task_till_completion


** do we need these fields ?
- latitude_start	String -> from the first task history
- longitude_start	String
- latitude_end	String -> from the last task history item
- longitude_end	String
- 
*** since the distance is not just the distance from point A (pickup) and point B, 
we can't calculate it with the latitude and longitude provided because 
we don't know the effective street that was taken.

So we take the total_distance_travelled 

"transaction_fields": {
    "fare_amount": 311.61,
    "driver_amount": 255.67,
    "added_fees": 0 


"job_id":"236365"


  "job_state":"Successful",
  "has_delivery":"1",

  "job_pickup_latitude":"30.7397101",
  "job_pickup_longitude":"-122.4008504",
  "total_distance_travelled":"0",
  "total_time_spent_at_task_till_completion":"15",
  "has_pickup":"1",
  "fleet_id":"3635",

We can only take the task history where the fleet id coincide with the one in the main array

 
  "task_history":[
    {
      "id":235973,
      "job_id":85185,
      "fleet_id":3829,
      "fleet_name":"bobby singh",
      "latitude":"30.7192552",
      "longitude":"76.8102558",
      "type":"state_changed",
      "description":"Status updated from Assigned to Unassigned",
      "creation_datetime":"2016-01-11T09:34:17.000Z"
    },

  "transaction_fields": {
    "fare_amount": 311.61,
    "driver_amount": 255.67,
    "added_fees": 0 
  