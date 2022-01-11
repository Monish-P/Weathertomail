# Weathertomail

## About:
* This is a small web application , where for backend , I used Django framework, which ultimately uses Python.
* It sends the weather details , like temperature , of a particular , city to our specified email.
* Here , first , the home page asks for , the name, email and city of the user , for which he wanted to know the weather
* The same details will be stored in the database, for further references.
* Next , as soon as we submit , the temperature of the particular city will be sent to the specified mail , along with the an emoji depicting the temperature

## Inside the box:

* So first I created an app 'core', in the project weatherapi
* It contains the User table, where it stores the user details
* All the main logic is inside the views.py file, where first thing I did is to make an API request call to https://openweathermap.org/api , where it provides weather information
* The same , information I embedded in the mail , and sending the mails.


## Gallery:
![image](https://user-images.githubusercontent.com/69596691/148989103-3df390f0-c35d-4ebb-aba2-226886819034.png)
![Screenshot 2022-01-11 at 10 38 56 PM](https://user-images.githubusercontent.com/69596691/148989149-7a5aebce-d6fa-4994-bb6b-adba633dff6e.png)
