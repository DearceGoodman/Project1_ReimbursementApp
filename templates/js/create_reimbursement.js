

let newReimbursement=document.getElementById("reimbursementForm");


async function sumbitReimbursement(){
    
  

    let url = "http://127.0.0.1:5000/employee";

    let firstName=document.getElementById("firstName")
    let lastName=document.getElementById("lastName")
    let employeeId=document.getElementById("employeeId")
    let requestAmount=document.getElementById("requestAmount")
    let employeeComment=document.getElementById("employeeComment")
    let requestTicket=document.getElementById("requestTicket")
    let requestStatus=document.getElementById("requestStatus")
    let managerComment=document.getElementById("managerComment")
    
    
    let response = await fetch(url,{

        method: "POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({
            "firstName": firstName.value,
            "lastName": lastName.value,
            "employeeId": employeeId.value,
            "requestAmount": requestAmount.value,
            "employeeComment": employeeComment.value,
            "requestTicket": requestTicket.value,
            "requestStatus": requestStatus.value,
            "managerComment": managerComment.value,
            
        })

    })
    let responsedata = await response.json();
    console.log(responsedata)
}