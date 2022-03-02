# assignment_django
Sunaritha Rajendra Karanth
A00447454

**API for hotel reservation system using Python Django rest framework**

## Get: Get List of hotels available in database
http://localhost:8000/hotel_list/

Response: 
'''
[
    {
        "id": 7,
        "name": "Taj",
        "price": 3405
    }
]
'''
## Post: Add new hotel into the database.

parameters: id (int) - ID number- Primary key
            name(String)- Hotel name
            price(Float)- Price of the room per night   
            
http://localhost:8000/hotel_list/

Example:
'''
{
    "id": 7,
    "name":"Taj",
    "price":3405
}
'''

Response: 
'''
{
    "Message": "Added Successfully"
}
'''
