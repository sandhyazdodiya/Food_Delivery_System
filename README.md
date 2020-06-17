# Food Delivery System.
I am developing this web-app for learning purpose.
A. User Sign-UP:
-------------------
1.  Url: /user-signup/
    Action: Render user-signup Page
    Method: GET
    
2.  Url: /users/
    Action: User Registration
    Method: POST
    Request Data:{
        "id": 23,
        "password": "pbkdf2_sha256$180000$m9A56tw3rbiP$KP4CTGYICWz1mdrvQQpWlgTkKXFBdv/5yHI0hFu9QxM=",
        "last_login": "2020-06-16T18:07:26.473275Z",
        "is_superuser": false,
        "first_name": "",
        "last_name": "",
        "email": "sandhya.lintel@gmail.com",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2020-06-16T17:57:01.727400Z",
        "user_type": 1,
        "phone": "",
        "groups": [],
        "user_permissions": []
    }
	
B. User Login
1. Url:/login/
   Action:Render user-login page
   Method:GET
2. Url:/login/api/
   Action:User login
   Method:POST
   Request Data:{
   "email": "sandhya.lintel@gmail.com",
   "password": "pbkdf2_sha256$180000$m9A56tw3rbiP$KP4CTGYICWz1mdrvQQpWlgTkKXFBdv/5yHI0hFu9QxM=",
   "user_type": 1,----[(1, 'admin'),(2, 'restaurant'),(3, 'dpartner'),(4, 'user')]
   }
   