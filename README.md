# Transportation Data Project

- In this project I'm exploring different data sources providing information about roads in the UK.
- The idea is to first explore the data sources available as I find more and more, and then build an ingestion pipeline using Apache Airflow.
- When I have enough data to be able to build some kind of data warehouse, I will then start implementing a dashboarding system where I can showcase the transportation data.
- We can then start having a deep dive into analysing these datasets and build a model to provide suggestions.

P.S:
- I am finding ideas as I go, I do not have a concrete idea about what I'm building, what I find guides my next step.
- This is iteration 1. Each iteration will be in a branch, and once I finish with an iteration, I merge it with master branch.

## Iteration 1

So far in this stage we built the following parts:
- Set up Airflow and got it running successfully in the local environment.
- Set up the first DAG (NHRN Extraction DAG).
- In the NHRN Extraction DAG we set up the first task as a Docker Operator that uses Selenium to scrape the NHRN datasets page in data.gov.uk. It then returns all the links for the files currently available for ingestion.
- The Docker image used to perform this task is in the 'web_scraping' directory.
- I faced a few problems when trying to set up this task. The biggest one was being able to spin up Docker containers from Airflow using the operator, because when I expose the docker socket to the Airflow container to use, I need to give the user in the Airflow container permission to access the socket on my local machine (manually), which is not ideal, and is also a security concern. After I searched the internet for solutions to this problem, I came accross an article that suggests a very elegant approach, which was exposing the Docker API through TCP by running a UNIX to TCP port forwarder as a Docker Compose service. [1](#references)




### References

[1] [How to fix a permission denied when using DockerOperator in Airflow](https://onedevblog.com/how-to-fix-a-permission-denied-when-using-dockeroperator-in-airflow/)