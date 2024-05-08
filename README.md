# RNS Trial Task
RNS Trial Task: A Django Rest API that accepts a file to upload, creates a new key, 
encrypts the file and stores it in AWS S3. It also provides endpoints to list all encrypted files, 
delete an encrypted file and decrypt encrypted file. It encrypts files using the Fernet (symmetric encryption)
available in the cryptography module. The key used for encryption is returned by the upload API but not persisted.
One can save this key and later use the decrypt API to decrypt the file. The decrypt API returns a base64 encoded
decrypted version of the file. You can use a tool like [Base64 to File](https://base64.guru/converter/decode/file) 
to decode it. Below is a screenshot of a test decoding a PDF file

![Screenshot of decoding a base64 encoded PDF file after decryption](/test_decoded_pdf.png)

### API Documentation
A Postman documentation of the API can be found [here](https://documenter.getpostman.com/view/1245038/2sA3JKcgxF)

### Test environment
The API is hosted on Heroku for testing purposes. Click [here](https://rns-trial-task-7a333c830762.herokuapp.com/) to access it 

 Below is instructions on how to run this API locally on your device using Docker.

### Getting started
Install docker desktop locally on your machine

To run the application, open a terminal in the project root directory and run the command below. 
Before doing that, make sure to have created a `.env` file with all the env variables required by 
the application. This is needed by docker to properly configure and run the application. 
There an .env.example file that will let you know what values are needed.

```
docker-compose up rns_trial_task
```

This command will also build the container and install all necessary dependencies, so you do not have to do it manually.

### Migrations
After the container starts up, the terminal will warn you to apply any un applied migrations. To do that,
open a new terminal and execute the commands below one after the other.

```
docker exec -i rns_trial_task python manage.py makemigrations
docker exec -i rns_trial_task python manage.py migrate
```

The first command will create migration files for any model updates. This command must be run anytime a model update is made. 
The second command will apply any un applied migrations.

### Creating a superuser
Normally, you will need a superuser account to access the Django admin. To do that, execute the following command 
in a new terminal while the container is running to create a new superuser. The django admin is an easy way to access
encrypted files that have been uploaded.

```
docker exec -t -i rns_trial_task python manage.py createsuperuser
```

### Shell
If you plan to continuously execute a lot of django commands for the container, it helps to jump into the bash directly, 
that way, you can easily execute all the various commands without needing to do `docker exec` each time. 
To access the bash, execute the command below, you must make sure the container is running

```
docker exec -it rns_trial_task /bin/bash
```