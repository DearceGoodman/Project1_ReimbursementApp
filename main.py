from flask import Flask, request, jsonify
from custom_exception.duplicate_employee_id_exception import DuplicateEmployeeIdException
from data_access_layer.implementation.login_dao_postgres import LoginPostgresDAO
from data_access_layer.implementation.manager_login_dao_postgres import ManagerLoginPostgresDAO
from data_access_layer.implementation.reimbursement_postgres_dao import ReimbursementPostgresDAO
from entities.login import Login
from entities.manager_login import ManagerLogin
from entities.reimbursement import Reimbursement
from service.implementation.login_service_postgres import LoginPostgresService
from service.implementation.manager_login_service_postgres import ManagerLoginPostgresService
from service.implementation.reimbursement_service_postgres import ReimbursementPostgresService
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

employee_dao = ReimbursementPostgresDAO()
employee_service = ReimbursementPostgresService(employee_dao)
login_dao = LoginPostgresDAO()
login_service = LoginPostgresService(login_dao)
manager_login_dao = ManagerLoginPostgresDAO()
manager_login_service = ManagerLoginPostgresService(manager_login_dao)


# employee_dao = EmployeeDAOImp()
# employee_service = EmployeeServiceImp(employee_dao)


@app.post("/employee")
def create_employee_entry():
    try:
        employee_data = request.get_json()
        new_employee = Reimbursement(
            employee_data["firstName"],
            employee_data["lastName"],
            employee_data["employeeId"],
            employee_data["requestAmount"],
            employee_data["employeeComment"],
            employee_data["requestTicket"],
            employee_data["requestStatus"],
            employee_data["managerComment"]
        )
        employee_to_return = employee_service.service_create_reimbursement(new_employee)
        employee_as_dictionary = employee_to_return.make_reimbursement_dictionary()
        employee_as_json = jsonify(employee_as_dictionary)
        return employee_as_json
    except DuplicateEmployeeIdException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get customer information
@app.get("/employee/<employee_id>")
def get_view_employee_requests(employee_id: str):
    result = employee_service.service_view_employee_requests(int(employee_id))
    result_as_dictionary = []
    for requests in result:
        dictionary_request = requests.make_reimbursement_dictionary()
        result_as_dictionary.append(dictionary_request)
    return jsonify(result_as_dictionary)


# get all customer information
@app.get("/employee")
def get_all_reimbursements_request():
    requests_as_requests = employee_service.service_get_all_request_tickets()
    requests_as_dictionary = []
    for requests in requests_as_requests:
        dictionary_request = requests.make_reimbursement_dictionary()
        requests_as_dictionary.append(dictionary_request)
    return jsonify(requests_as_dictionary)


# get all customer information
@app.get("/manager")
def manager_view_reimbursements_request():
    requests_as_requests = employee_service.service_get_all_request_tickets()
    requests_as_dictionary = []
    for requests in requests_as_requests:
        dictionary_request = requests.make_reimbursement_dictionary()
        requests_as_dictionary.append(dictionary_request)
    return jsonify(requests_as_dictionary)


@app.patch("/manager/<request_ticket>")
def update_request_information(request_ticket: str):
    try:
        request_data = request.get_json()
        new_request = Reimbursement(
            request_data["firstName"],
            request_data["lastName"],
            request_data["employeeId"],
            request_data["requestAmount"],
            request_data["employeeComment"],
            int(request_ticket),
            request_data["requestStatus"],
            request_data["managerComment"]
        )
        updated_request = employee_service.service_update_status_judgement(new_request)
        return "Customer updated successfully, the customer info is now " + str(updated_request)
    except DuplicateEmployeeIdException as e:
        return str(e)


# fix on statistics
@app.get("/manager/average/<employee_id>")
def average_request(employee_id):
    request_average = employee_service.service_statistics_average_reimbursement(employee_id)
    average = {"averagePayout": request_average}
    return jsonify(average)


@app.post("/login")
def login():
    body = request.get_json()
    login_credentials = Login(body["username"], body["password"])
    validated = login_service.validate_login(login_credentials.username, login_credentials.password)
    if validated:
        message = {"validated": True}
        return jsonify(message)
    else:
        message = {"validated": False}
        return jsonify(message)


@app.post("/manager_login")
def manager_login():
    body = request.get_json()
    manager_login_credentials = ManagerLogin(body["username"], body["password"])
    validated = manager_login_service.validate_manager_login(manager_login_credentials.username,
                                                             manager_login_credentials.password)
    if validated:
        message = {"validated": True}
        return jsonify(message)
    else:
        message = {"validated": False}
        return jsonify(message)


app.run()
