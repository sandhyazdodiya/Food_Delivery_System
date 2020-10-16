# Food Delivery System.
I am developing this web-app for learning purpose.



A. User Sign-UP:
-------------------
1.  Url: /user-signup/
    Action: Render user-signup Page
    Method: GET
    
2.  Url: /api/customer/
    Action: User Signup
    Method: POST
    Request Data:{
    "user": {
        "email": "sandhya@gmail.com",
        "password": "",
        "is_superuser": false,
        "user_type": 2,
        "phone": ""
    },
    "city": "",
    "state": "",
    "country": ""
}
	
B. User Login
-------------------
1. Url:/login/
   Action:Render user-login page
   Method:GET
2. Url:/login/api/
   Action:User login
   Method:POST
   Request Data:{
   "email": "sandhya@gmail.com",
   "password": "pbkdf2_sha256$180000$m9A56tw3rbiP$KP4CTGYICWz1mdrvQQpWlgTkKXFBdv/5yHI0hFu9QxM=",
   "user_type": 1,----[(1, 'admin'),(2, 'restaurant'),(3, 'dpartner'),(4, 'user')]
   }
   
   
C. Restaurant Sign-UP
-------------------
1. Url:/restaurant/api/
   Action:Restaurant Registration
   Method:POST
   Request Data:{
        "user": {
            "id": 5,
            "email": "sandhyazaverdodiya@gmail.com",
            "password": "pbkdf2_sha256$180000$Thj3Min73GIn$gzC5YUV1RgCVKAn1tk+b50ZLh5ivRd6JK8w/1+NuA0s=",
            "is_superuser": true,
            "user_type": 1,
            "phone": "sdsdf"
        },
        "name": "dsff",
        "description": "sdfsf",
        "city": "sdsd",
        "state": "sds",
        "country": "sdsd"
    },
	
D. Delivery Person Sign-UP
-------------------
1. Url:/delivery/api/
   Action:Restaurant Registration
   Method:POST
   Request Data:{
        "user": {
            "id": 5,
            "email": "sandhyazaverdodiya@gmail.com",
            "password": "pbkdf2_sha256$180000$Thj3Min73GIn$gzC5YUV1RgCVKAn1tk+b50ZLh5ivRd6JK8w/1+NuA0s=",
            "is_superuser": true,
            "user_type": 1,
            "phone": "sdsdf"
        },
        "name": "dsff",
        "description": "sdfsf",
        "city": "sdsd",
        "state": "sds",
        "country": "sdsd"
    },