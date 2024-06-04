data_get_pet = "https://petstore.swagger.io/v2/pet/1"
data_pet_name = "doggie"
data_post_url = "https://restful-booker.herokuapp.com/booking"
data_post_json = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }


data_add_pet = "https://petstore.swagger.io/v2/pet"
data_response_body = {
  "id": 68,
  "category": {
    "id": 7,
    "name": "string"
  },
  "name": "cheburek",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 4,
      "name": "vasya"
    }
  ],
  "status": "available"
}

data_find_pet_id = "https://petstore.swagger.io/v2/pet/68"
data_delete_pet = "https://petstore.swagger.io/v2/pet/68"
data_delete = "68"

data_put_url = "https://restful-booker.herokuapp.com/booking"
data_put_json = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 112,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}


data_patch_url = "https://restful-booker.herokuapp.com/booking"
data_patch_json = {
    "firstname": "James",
    "additionalneeds": "dinner"
}
