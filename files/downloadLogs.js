document.getElementById('res').addEventListener('click', (e) => {
    e.preventDefault()
    let tempData = new FormData()
    let tempFile = document.querySelector('input[type="file"]').files[0]
    tempData.append('studentdb', tempFile)
    console.log(tempFile)
    if(tempFile != null){
        fetch('http://localhost:5000/downloadLogs', {
            method: 'POST',
            body: tempData
        }).then((res)=>{
            return res.json()
        }).then((res) => {
            alert("Student Database has been updated.\nAvialable at '" + res + "'")
        }).catch((err) => {
            console.log(err)
        })
    }
    else{
        console.log("HELLO")
        fetch('http://localhost:5000/downloadLogsWithoutReplacement', {
            method: 'POST',
            body: "HELLO",
            headers: {'Content-Type': 'application/json'}
        }).then((res)=>{
            return res.json()
        }).then((res) => {
            alert("Student Database has been updated.\nAvialable at '" + res + "'")
        }).catch((err) => {
            console.log(err)
        })
    }
})
    
window.addEventListener('load',()=>{
    alert("If there is a new set of student database, please upload a csv file. The format is similar to sample.csv, with columns:\nname\ncard_number \nclass \nform_teacher_one \nform_teacher_two \nteachers_emails \n\n If it is simply cleaning database, do not upload any file.")
})
