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

**Run main**

`python3 main.py`


**Run Flask Web**

`python3 web.py`

## Test the endpoint locally:

`curl -X POST http://127.0.0.1:8080/webhook/djsnckvj --header 'Content-Type: application/json' --header 'Hmac-SHA256: SgS9OYxlwwM75ttkEJSrMJvVpoXTLrHkWQAJrgFx7LY='  --data '{"event": "SERVER_UPDATE"}'
`

With **Postman**:

![postman-body.jpg](static%2Fpostman-body.jpg)

![postman-header.jpg](static%2Fpostman-header.jpg)