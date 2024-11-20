from flask import Flask, Blueprint
from flask_restx import Api, Resource, fields
from controller import *

# Flask setup
app = Flask(__name__)
blueprint = Blueprint("api", __name__, url_prefix="/")
api = Api(
    blueprint,
    version="1.0",
    title="ODK API",
    description="APHL - ODK API",
    contact="irzelindo salvador",
    contact_email="irzelindo.salvador@moz.aphl.org",
)

app.register_blueprint(blueprint)

# Define API namespace for users
user_ns = api.namespace("users", description="User operations")

# Define API namespace for projects
project_ns = api.namespace("projects", description="Project operations")

# Define user model for Swagger
user_model = user_ns.model(
    "User",
    {
        "id": fields.Integer(readOnly=True, description="The unique identifier"),
        "email": fields.String(required=True, description="The user email"),
        "type": fields.String(required=True, description="The user type"),
        "displayName": fields.String(
            required=True, description="The display name of the user"
        ),
        "createdAt": fields.String(description="The creation date of the user"),
        "updatedAt": fields.String(description="The last update date of the user"),
        "deletedAt": fields.String(description="The deletion date of the user"),
    },
)

# Define project model for Swagger
project_model = project_ns.model(
    "Project",
    {
        "id": fields.Integer(
            readOnly=True, description="The unique identifier of the project"
        ),
        "name": fields.String(required=True, description="The name of the project"),
        "description": fields.String(description="The description of the project"),
        "archived": fields.Boolean(description="Whether the project is archived"),
        "keyId": fields.String(description="The key ID of the project"),
        "createdAt": fields.String(description="The creation date of the project"),
        "updatedAt": fields.String(description="The last update date of the project"),
        "deletedAt": fields.String(description="The deletion date of the project"),
        "verbs": fields.List(
            fields.String, description="The actions available for the project"
        ),
    },
)


# Define the User Resource
@user_ns.route("/")
class UserList(Resource):
    @user_ns.doc("list_users")
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return get_users()


# Define the Project Resource
@project_ns.route("/")
class ProjectList(Resource):
    @project_ns.doc("list_projects")
    @project_ns.marshal_list_with(project_model)
    def get(self):
        """List all projects"""
        return get_projects()


# Define the Project Details Resource
@project_ns.route("/<int:project_id>")
@project_ns.response(404, "Project not found")
@project_ns.param("project_id", "The project identifier")
class Project(Resource):
    @project_ns.doc("get_project")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id):
        """Fetch a project given its identifier"""
        return get_project_details(project_id)


# Define the Forms Details Resource By Project
@project_ns.route("/<int:project_id>/forms")
@project_ns.response(404, "Project forms not found")
@project_ns.param("project_id", "The project identifier")
class Project(Resource):
    @project_ns.doc("get_forms_by_project")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id):
        """Fetch the forms by given project identifier"""
        return get_forms_by_project(project_id)


# Define the Form Details Resource By Form
@project_ns.route("/<int:project_id>/forms/<form_id>")
@project_ns.response(404, "Form details not found")
@project_ns.param("project_id", "The project identifier")
@project_ns.param("form_id", "The form identifier")
class Project(Resource):
    @project_ns.doc("get_forms_details_by_project")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id, form_id):
        """Fetch the form details by given project identifier"""
        return get_form_details(project_id, form_id)


# Define the Form Submissions
@project_ns.route("/<int:project_id>/forms/<form_id>/submissions")
@project_ns.response(404, "Form Submissions not found")
@project_ns.param("project_id", "The project identifier")
@project_ns.param("form_id", "The form identifier")
class Project(Resource):
    @project_ns.doc("get_submissions_by_form")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id, form_id):
        """Fetch the form submissions by given form identifier"""
        return get_submissions(project_id, form_id)


# Define the Form Submissions answers data for specific instance
@project_ns.route("/<int:project_id>/forms/<form_id>/submissions/<instance_id>")
@project_ns.response(404, "Form Submissions not found")
@project_ns.param("project_id", "The project identifier")
@project_ns.param("form_id", "The form identifier")
@project_ns.param("instance_id", "The form instance identifier")
class Project(Resource):
    @project_ns.doc("get_submissions_data_by_form")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id, form_id, instance_id):
        """Fetch the form submissions answers data by given form identifier"""
        return get_submission_by_instance(project_id, form_id, instance_id)


# Define the Form Submissions Metadata
@project_ns.route(
    "/<int:project_id>/forms/<form_id>/submissions/<instance_id>/metadata"
)
@project_ns.response(404, "Form Submissions Metadata not found")
@project_ns.param("project_id", "The project identifier")
@project_ns.param("form_id", "The form identifier")
@project_ns.param("instance_id", "The form instance identifier")
class Project(Resource):
    @project_ns.doc("get_submissions_metadata_by_form")
    # @project_ns.marshal_with(project_model)
    def get(self, project_id, form_id, instance_id):
        """Fetch the form submissions metadata by given form identifier"""
        return get_submission_by_instance_metadata(project_id, form_id, instance_id)


if __name__ == "__main__":
    app.run(debug=True)
