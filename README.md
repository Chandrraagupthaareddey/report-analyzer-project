
# Medical Report Analysis Application

This project is a web application for analyzing medical reports. It includes frontend and backend components, as well as MongoDB and PostgreSQL databases.

## Directory Structure

project/
│
├── backend/
│ ├── app.py
│ └── Dockerfile
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── Dockerfile
│ └── package.json
│
├── database/
│ └── schema.sql
│
├── models/
│ ├── nlp_model.py
│ └── preprocessing.py
│
├── README.md
└── docker-compose.yml


## Backend
- The `backend/` directory contains Flask backend code.
- Modify the `app.py` file to adjust database connection URIs and application logic.

## Frontend
- The `frontend/` directory contains React.js frontend code.
- Add React components and stylesheets in the `src/` directory.

## Database
- The `database/` directory contains the `schema.sql` file with the database schema definition.

## Models
- The `models/` directory may contain additional Python files for data processing or machine learning models.

## Usage

### Running the Application
1. Install Docker and Docker Compose.
2. Clone this repository.
3. Navigate to the project directory.
4. Run `docker-compose up` to start the application.

### Accessing the Application
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

### Database Setup
- MongoDB: No setup required. Data is persisted in the `mongo_data` volume.
- PostgreSQL: No setup required. The schema is automatically created based on the `schema.sql` file.

## Contributing
1. Fork this repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).
