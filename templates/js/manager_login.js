const username = document.getElementById("usernameInput")
const password = document.getElementById("passwordInput")

async function login(){
    let response = await fetch(
        "http://127.0.0.1:5000/manager_login",{
            method:"POST",
            headers:{"Content-Type": "application/json"},
            body: JSON.stringify({"username":username.value, "password":password.value})
        }
       )
    if(response.status === 200){
        let body = await response.json()
        if (body["validated"]){
            sessionStorage.setItem("validated", true)
            window.location.href="manager_dashboard.html"
        }else{
            alert("login failed: please try again")
        }
    }else{
        alert("the request failed")
    } 
}