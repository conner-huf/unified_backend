# Centralized ConnerAPI

#### Reasoning
Here's a little tidbit for every developer on the job market: hosting stuff gets expensive. And because all of us have been in the market for a long period of time (most of us anyway), optimizing the cost of hosting should be pretty front-of-mind.

I've got lots of projects out there, and most of them require some kind of hosted backend with exposed endpoints. And hosting all these backends has a kind-of 'floor' cost - like it costs *something* to have it hosted, even if there's little-to-no traffic. 

So I've decided to consolidate all of my backends into a single hosted api that routes to the appropriate endpoints / backends / data and host it in a single centralized location. This way, if I don't meet the traffic needed to actually start costing something additional to the base cost of hosting a backend, I don't have 5 backends being hosted with little-to-no traffic, I have 1 (cutting the cost by a lot).

This API is written using Python - FastAPI and will be hosted on Azure when completed.

#### Available Routes

- /resume 
  - endpoints for accessing my resume information
- /noodle 
  - endpoints for my concert venue web application
- /ribbon
  - API for accessing gift data for users

#### Architecture
  - data
    - This is where referenced data is stored. ~~Holds things like my resume information in a json file.~~ Holds the mongoDB connection and is referenced by services that need db access.
  - models
    - Place for defining data models for more complicated data structures.
  - routes
    - Where endpoints are defined. Separated by project (ex- NoodleAPI, ResumeAPI)
  - services
    - Where the functions that endpoints call are defined. Separated by project (ex- NoodleService, ResumeService)
  - auth
    - Where authentication logic goes
  - config
    - This is where the environment configuration is stored.
  - main
    - The main entry point for the server. Where all the endpoints are initialized.

#### Update (1/2/25)

I've added a new portion to this backend, I'm currently calling it Red Ribbon. I want this to serve as a backend data manipulation endpoint for storing wishlists, users, and other data that will support a frontend app for organizing things like secret santa and deciding what gifts to get your loved ones on holidays.

#### Update (2/13/25)

Over the past few weeks, I moved this to a new repo because I wanted to get this connected with an Azure App service. Da-da-daaaaa, now I've officially consolidated my backend APIs into this one (the ones I still want, anyway). I've also got this set up with CI/CD so that it'll auto-deploy changes to main when a branch gets merged. I've found a new thing I want to work on for a bit, so Red Ribbon is on the back burner for a second here, but I'll be back on it soon.
