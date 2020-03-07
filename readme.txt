RESTful API 

Methods: GET, POST, PUT, DELETE 

--> GET: requests the information 
--> POST: Create new information
--> PUT: update information 

What are you offering: +, -, /, * 
--------------------------------

Resource: Method Path,      used for,       Param,               error code 
+ : POST    /add            adding 2 nums   x: int, y: int       200 OK, 301- missing parameter if any 
- : POST    /subtract       adding 2 nums   x: int, y: int       200 OK, 301- missing parameter if any 
- : POST    /divide         adding 2 nums   x: int, y: int       200 OK, 301- missing parameter if any, 302- invalid 
* : POST    /multiply       adding 2 nums   x: int, y: int       200 OK, 301- missing parameter if any 
