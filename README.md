# Python RESTful API with Flask and SQLAlchemy

This is a simple RESTful API built with Python using Flask and SQLAlchemy. The API provides endpoints for creating, reading data from ODK database.

## Running the API

To run the API, make sure you have Python and pip installed. Then, install the required packages with the following command: `pip install -r requirements.txt`

Once the dependencies are installed, you can run the API using the following command: `python api.py`

The API will start running on http://localhost:5000

## Endpoints

The API provides the following endpoints:

- `GET https://inqueritos.openldr.org.mz/v1/users`: List all users
- `GET https://inqueritos.openldr.org.mz/v1/projects`: List all projects
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}`: Fetch a project given its identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms`: Fetch the forms by given project identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms/{form_id}`: Fetch a form given its identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms/{form_id}/submissions`: Fetch the form submissions by given form identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms/{form_id}/submissions/{submission_id}`: Fetch a form submission given its identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms/{form_id}/submissions/{submission_id}/metadata`: Fetch the form submissions metadata by given form identifier
- `GET https://inqueritos.openldr.org.mz/v1/projects/{project_id}/forms/{form_id}/submissions/{submission_id}/metadata/{metadata_id}`: Fetch a form submission metadata given its identifier

## Testing the API

To test the API, you can use the following command: `pytest`

The API will start running on http://localhost:5000

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenLDR
- Open Data Kit
- ODK
- ODK Collect
- ODK Aggregate
- ODK Form Builder
- ODK Form Editor
- ODK Collect
- ODK Form Editor
- ODK Form Builder