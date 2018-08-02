document.getElementById('student-submit').addEventListener('click',(e)=>{
  s = JSON.stringify(document.getElementById('name').value)
  fetch('http://localhost:5000/email', {
    method: 'POST',
    body:s,
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((response) => {
    return response.json()
  }).then((res)=>{
    document.getElementById('name').value = ""
    if (res === "Error"){
      alert("Student ID is invalid")
    }else{
      alert("Student " + res + " has been logged.")
    }
  }).catch((err)=>{
      console.log(err)
  })
})