# Django Personal Blog Api With Nuxt Frontend with Docker Compose, Makefile, and PostgreSQL

This is a basic api for a personal blog. You can create posts, comments, tags for your posts. The application uses jwt
authorisation.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

2. Install all required packages in `Requirements` section.

3. Endpoint docs on api/docs

### Implemented Commands

* `make app` - up application and database/infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make storages` - up only storages. you should run your application locally for debugging/developing purposes
* `make storages-logs` - foolow the logs in storages containers
* `make storages-down` - down all infrastructure

### Most Used Django Specific Commands

* `make migrations` - make migrations to models
* `make migrate` - apply all made migrations
* `make collectstatic` - collect static
* `make superuser` - create admin user

### Frontend build
`cd frontend`
 
* `npm install` - install dependencies
* `npm run dev` - serve with hot reload at localhost:3000
* `npm run build` - build for production
* `npm run start` - launch server
* `npm run generate` - generate static project