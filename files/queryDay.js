cv = (e) => {
  if (e === ""){
    d = new Date()
    r = d.getFullYear()*10000 + (d.getMonth()+1)*100 + d.getDate()
    return String(r)
  }
  return e
}

cv2 = (e) => {
  e = String(e)
  if (e.length === 5){
    e = "0" + e
  }
  return e[0] + e[1] + ":" + e[2] + e[3] + ":" + e[4] + e[5]
}

window.addEventListener('load',()=>{
  alert("Please input date in YYYYMMDD format. \nIf the required date is the current date, then leave the filed blank.")
})

document.getElementById('query-day-submit').addEventListener('click', (e) => {
  s = JSON.stringify(cv(document.getElementById('query-day').value))
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
      if (typeof(res) === "string"){alert(res)}
      else{
        s = '<table class="ui table"> <thead><tr><th>Name</th><th>Class</th><th>Time</th></tr></thead><tbody></tbody>'
        for (let i = 0; i < res.length; ++i){
          s += "<tr class='"
          if(i%2===0){s+= "positive"}
          else {s += "error"}
          s += "'><td>"
          s += res[i]["name"]
          s += "</td ><td>"
          s += res[i]["class"]
          s += "</td><td>"
          s += cv2(res[i]["time"])
          s += "</td></tr>"
        }
        s += "</tbody ></table>"
        document.getElementById('response').innerHTML = s
      }
    }).catch((err) => {
      console.log(err)
    })
  }, 1);
})