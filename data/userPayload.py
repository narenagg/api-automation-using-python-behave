def add_user_payload():
    body = {
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
    return body

def add_user_list_payload():
  body = [
  {"id": 11,
  "username": "theUser1",
  "firstName": "John1",
  "lastName": "James",
  "email": "john1@email.com",
  "password": "123456",
  "phone": "123456",
  "userStatus": 2},
   {"id": 12,
  "username": "theUser2",
  "firstName": "John2",
  "lastName": "James2",
  "email": "john21@email.com",
  "password": "1234256",
  "phone": "1223456",
  "userStatus": 3}]
  return body

    

def updated_user_payload():
  body = {
  "id": 10,
  "username": "theUser",
  "firstName": "John12",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
  return body