// I want to get all reimbursement info a page startup


const managerTable = document.getElementById("reimbursementTable");
const managerTableBody = document.getElementById("reimbursementHead");

async function getAllEmployeeReimbursementData(){
    let url = "http://127.0.0.1:5000/manager";

    let response = await fetch(url);

    if (response.status == 200){
        let body = await response.json();
        populateData(body);
    }else{
        alert("There was a probleming loading reimbursement data");
    }
}

function populateData(responseBody){

    for(let request of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${request.firstName}</td><td>${request.lastName}</td><td>${request.employeeId}</td><td>${request.requestAmount}</td><td>${request.employeeComment}</td><td>${request.requestTicket}</td><td>${request.requestStatus}</td><td>${request.managerComment}</td>`;
        managerTableBody.appendChild(tableRow);
        
    }
}

getAllEmployeeReimbursementData()