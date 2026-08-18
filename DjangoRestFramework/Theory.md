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

