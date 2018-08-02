document.getElementById('res').addEventListener('click', (e) => {
    e.preventDefault()
    let tempData = new FormData()
    let tempFile = document.querySelector('input[type="file"]').files[0]
    tempData.append('studentdb', tempFile)
    fetch('http://localhost:5000/uploads', {
        method: 'POST',
        body: tempData
    }).then((response) => {
        return response.json()
    }).then((data) => {
        console.log(data)
    }).catch((err) => {
        console.log(err)
    })
})