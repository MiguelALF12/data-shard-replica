# Backend API for CRUD Dashboard

## Project Status
> IMPORTANT UPDATE: This project is no longer in active development. While the initial groundwork has been laid, and some functionalities may be partially implemented, there will be no further updates, features, or fixes.

## Overview
This project consists of the backend API and logic for a web application that provides a CRUD dashboard, designed exclusively for managing user data. The API ensures efficient interaction and data manipulation without encompassing the frontend elements, as the frontend development was outside the scope of this project.

## Architecture
The backend is structured on a microservices architecture pattern, utilizing Python and the Flask framework. It has been optimized for performance and ease of integration with frontend services.

<img src="https://github.com/MiguelALF12/data-shard-replica/blob/main/imgs/Arquitectura-0.jpeg" alt="Deployment architecture" width="700"/>

### Database Configuration

The heart of the application's data persistence is a MongoDB setup, which runs on Docker containers. This setup employs replica sets and sharding to ensure data is highly available and the service can scale horizontally with demand.

<img src="https://github.com/MiguelALF12/data-shard-replica/blob/main/imgs/sharding-and-replica-sets.png" alt="Mongo DB cluser"/>

### Deployment

Deployment is managed on DigitalOcean, although the API is not currently deployed for public access. Initial attempts to establish a domain name and set up the DNS service were not successful, but these issues are being actively addressed.

## Key Features

- **API-Driven User Management**: Perform CRUD operations through API endpoints, facilitating the manipulation of user data.
- **Authorization**: It uses JWT authorization to ensure security when accesing to the dahsboard.
- **Dockerized MongoDB Infrastructure**: Leverages Docker to containerize MongoDB instances, configured with replica sets and sharding for optimal data management.
- **Scalability**: The architecture is designed for horizontal scaling to accommodate growth.
- **Deployment**: Prepared for deployment on DigitalOcean, with domain name and DNS setup to be completed.

## Technical Stack

- **Backend API**: Python with the Flask framework.
- **Database**: MongoDB, utilizing Docker for container deployment.
- **Deployment**: Intended for DigitalOcean (API not yet publicly available).

## Acknowledgement
Thanks to @minhhungit for its description and implementation of the mongoDB cluster architeture. It can be found [here](https://github.com/minhhungit/mongodb-cluster-docker-compose)


