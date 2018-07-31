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
    }).catch((err)=>{
        console.log(err)
    })
})