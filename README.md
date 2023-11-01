# Personal Blog on IBM Cloud Static Web Apps

This is a personal travel blog that runs on IBM Cloud.

## How to Run the Project

1. First, download the personal travel blog folder.

2. Inside the folder, open the app.py file.

3. To run the file, install ibm_db and flask using pip in Python.

4. Create a database in the cloud using the following steps:
   - Select the DB2 service from the list of available services.
   - Create a database instance.
   - In that database, navigate to load data and upload the table structure as a CSV format provided in the code and go to the next step.
   - Create a table and edit the columns as required.
   - Finally, the data will be loaded onto the cloud.

5. Run the project using the command python app.py.

## Deployment Options

You can deploy the project using various methods:

1. Use the provided Docker file in the folder.
2. Build a Docker image.
3. Run the Docker image.
4. Consider using Kubernetes for deployment.
5. Deploy the project in the cloud.

## Navigation Through the Pages

When you run the code, the home page will be displayed. The navigation bar is used to move between pages, and it is present on all web pages.

In the Navigation bar:

- "HOME" links to the root of the webpage ("/home.html").
- "STORIES" links to "/travel.html". Clicking on a specific destination image leads to a related blog page (e.g., "/taj.html" for Taj Mahal).
- "TRIPS & GUIDES" links to "/guide.html". Clicking on images of various places with guides leads to specific guide pages (e.g., "/india.html" for India).
  Inside "india.html," under "Top destinations," clicking on a destination links to a blog post related to that destination.
- "GALLERY" links to "/gallery.html".
