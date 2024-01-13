# Rankings-API

This project works on two tables with the following schemas:

users (
`id`: Primary key
`username`: Unique
`karma_score`: positive integer, default is 0. `image_id`: foreign key.
)

images (
`id`: primary key `url`: string
)

fetch_records.py:
 is the main file which defines an API and its functionality. The database "mydatabase.db" is hosted on localhost on the basis of which the API gets the information. The database has 100,000 records. Each API hit returns exactly five records. For example :

GET <flask-provided-address>/api/v1/user/19823/karma-position

Will return rank information for the user 19823, and two users rankings above and two users ranking below:

```
[
  {
    "id": 4564,
    "image_url": "https://d2ywys6d0u_4564",
    "karma_score": 1712,
    "position": 75181
  },
  {
    "id": 15438,
    "image_url": "https://okgd42y0jk_15438",
    "karma_score": 1712,
    "position": 75182
  },
  {
    "id": 19823,
    "image_url": "https://y699chx9hy_19823",
    "karma_score": 1712,
    "position": 75183
  },
  {
    "id": 40571,
    "image_url": "https://4mqgcwelnn_40571",
    "karma_score": 1712,
    "position": 75184
  },
  {
    "id": 47840,
    "image_url": "https://ccb2wba8so_47840",
    "karma_score": 1712,
    "position": 75185
  }
]
```


NOTE: for any user_id such as 9000000, a user does not exist, so the API will return 404: user not found.

<img width="1440" alt="Screenshot 2024-01-13 at 2 25 59 PM" src="https://github.com/Vraj1234/API-for-Rankings/assets/53624234/384be217-206c-4c2f-874b-48fccfd30154">


## Installation
We will need one database (SQLite used here). 
We will need a simple web-based Python framework using flask.
To generate a webpage, we will use HTML/CSS/JS


## Execution
### Setting up DB and dummy records:

1) After Installing SQLite, run the following commands in your terminal

```bash
sqlite
```

```bash
CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    url TEXT
);
```

```bash
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    karma_score INTEGER DEFAULT 0,
    image_id INTEGER,
    FOREIGN KEY(image_id) REFERENCES images(id)
);
```

Please note that you must create the `images` table before the `users` table because `users` has a foreign key that references `images`. If `images` don't exist when you try to create `users`, you'll get an error.

The above commands will create the table.

2. Commit changes to the DB and run the "add_random_images.py" file by plugging in the appropriate database in line 7. This will add 100,000 images and image IDs

3. Now, run "add_random_users.py". This will generate 100,000 random users and link image_ids to users.

<img width="1271" alt="Screenshot 2024-01-13 at 2 26 58 PM" src="https://github.com/Vraj1234/API-for-Rankings/assets/53624234/529d0509-f303-490f-a815-fa7a4d257366">


### Setting up API using flask.
1. Make sure Flask is installed and imported with the right version of Python interpreter.

2. Running "fetch_records.py" should start a local host server with an IP address shown in the terminal.

3. <flask-provided-address>/api/v1/user/19823/karma-position
Paste this URL in any browser, and you will get JSON results with exactly five objects every time.

<img width="1440" alt="Screenshot 2024-01-13 at 2 28 05 PM" src="https://github.com/Vraj1234/API-for-Rankings/assets/53624234/049fd499-e479-45c5-bac4-aa47fd26c4ea">


### Testing API using Automated test cases.
1. In the "test_api.py" file, there are two testing functions :
  - to verify if the result of JSON is 200 or not (test_user_id_returns_200)
  - to check the output of any API with a given user id. (test_print_output) 

Parameters for the first function can be changed in line 13 in the API call itself.

AND

Parameters for the second test function can be changed in line 18 in the API call itself.

<img width="1081" alt="Screenshot 2024-01-13 at 2 28 50 PM" src="https://github.com/Vraj1234/API-for-Rankings/assets/53624234/4c0ce84a-8dec-42a8-a898-6d1730b87204">

### Generate a dynamic HTML page on the basis of an API query:
1. Line 39 of the "webpage.html" determines the user id.
2. Using this user_id, the webpage synthesizes an API call, and the resulting JSON is converted to a table and presented.
3. 
<img width="1440" alt="Screenshot 2024-01-13 at 2 29 13 PM" src="https://github.com/Vraj1234/API-for-Rankings/assets/53624234/d1e3a96a-3d2c-4174-ba02-2af6cc2c5005">

### Extras
1. clear_tables.py is to purge data from both the tables.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


