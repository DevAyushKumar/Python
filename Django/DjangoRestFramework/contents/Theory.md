Theory:
-> API
-> REST
-> Error codes/HTTP status codes
-> Statelessness
-> Endpoints

Traditional Web Paradigm
-> HTTP
Browser     <->     Webserver  <-> Database(s)
(front-end)     (backend/frontend) (weather database)

HTTP response codes:
-> (2xx) Success
200 success, 201 created, 202 accepted
-> (3xx) Redirections
-> (4xx) Client error
-> (5xx) Server error
500 Internal server errror

Applied to webservices:
--> Restful API:
-> A base URL https://ex.com/api/
-> HTTP meathods (GET, POST, PUT, PATCH and DELETE)
-> is stateless, like HTTP
-> Includes media type to define state transition data elemets(JSON)

Endpoints:
-> webpages normally contains links to resources (http://site.com/blog)
-> RESTful API have Endpoints
~ http://site.com/api/user/1 -> get user with id=1
~ http://site.com/api/books -> get all books
~ Remember -> Data is returned as (JSON etc)

Endpoints and request meathod:
-> restful api have endpoints
http://site.com/user/1

-> Service respond based upon request type:
~ Get: retrive user 1 data
~ delete: delete user 1

Theory:
-> API
-> REST
-> Error code/HTTP Status Codes
-> Statelessness
-> Endpoints

