document.getElementById('student-submit').addEventListener('click',(e)=>{
  s = JSON.stringify(document.getElementById('name').value)
  console.log(s)
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
    }
  }).catch((err)=>{
      console.log(err)
  })
})