# The Polygot

A CMPT 383 project

<b>Topic idea: Python dashboard hosted on a Flask and Express Server.</b>

## Project Summary

Overall goal of the project: The city of Jakarta recorded a high increase of covid cases in the month of June in 2021. The bed occupation rate was high and the active cases number was the highest since January 2021. This project is showing a dashboard of the growth of covid cases in the city of Jakarta in June 2021. The dashboard can then be analyzed by the government to make decisions based on the data that can reduce the spread of the virus and allocate beds in the hospital.

## Languages Used

Programming Languages:

* Scripting Language - Javascript: Implement the starting server and the landing page
* Scripting Language - Python: Generate dashboard for the data and run the secondary server
* System Language - C++: Calculation

Communication Methods:

* Inter-language communication methods

* RPC (REST) server: To make request from one another. The JS Express initial server calls a Flask (python) that hosts the dashboard.
foreign function interface: CDLL for calling C/C++ function from python Deployment technology: Docker containers
To get the project working you should:

## How to Run

Open the docker application on your computer Open terminal then type and run

docker-compose build
docker-compose up
When the application is running open http://localhost:3000 to view landing webpage. Click the link on the webpage to view the dashboard. THe date range can be changed. The result of the C calculation can be seen in the console.

## Things you should be looking at

You should be looking at how there are 2 webpages that are hosted in two different servers. It makes sense to have one server hosting the dashboard and the other one hosting other pages, because the dashboard could be expanded to be a big data analytics webpage that requires a lot of resources since the traffic will definitely be high. You can also change the date range in this dashboard. However, in this project I am making a prototype of how the servers interact with each other. In addition to that, the C++ calculation is also helpful when dealing with data that are big in terms of size as it is able to do fast calculation compared to python.

References: Python Dashboard and CSS https://realpython.com/python-dash/#how-to-set-up-your-local-environment
