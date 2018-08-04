cv = (e) => {
    if (e === ""){
        d = new Date()
        r = d.getFullYear()*10000 + (d.getMonth()+1)*100 + d.getDate()
        return String(r)
    }
    return e
}

window.addEventListener('load',()=>{
    alert("Please input date in YYYYMMDD format. \nIf the required date is the current date, then leave the filed blank.")
})

document.getElementById('query-day-submit').addEventListener('click', (e) => {
    s = JSON.stringify(cv(document.getElementById('query-day').value))
    console.log(s)
    setTimeout(() => {
        fetch('http://localhost:5000/queryDay', {
            method: 'POST',
            body: s,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            return response.json()
        }).then((res) => {
            console.log(res)
        }).catch((err) => {
            console.log(err)
        })
     }, 1);
})