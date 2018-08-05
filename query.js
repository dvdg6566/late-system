cv2 = (e) => {
  e = String(e)
  if (e.length === 5) {
    e = "0" + e
  }
  return e[0] + e[1] + ":" + e[2] + e[3] + ":" + e[4] + e[5]
}

cv = (e) => {
  e = String(e)
  return e[6] + e[7] + "/" + e[4] + e[5] + "/" + e[0] + e[1] + e[2] + e[3]
}

document.getElementById('query-submit').addEventListener('click', (e) => {
  s = JSON.stringify(document.getElementById('query_name').value)
  fetch('http://localhost:5000/query', {
    method: 'POST',
    body: s,
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((response) => {
    return response.json()
  }).then((res) => {
    if (res.length === 0){
      alert("Student ID is invalid")
    }else{
      document.getElementById('query_name').value = ""
      while (document.getElementById('storage').firstChild) {
        document.getElementById('storage').removeChild(document.getElementById('storage').firstChild)
      }
      document.getElementById('storage').setAttribute("style", "border-color: #fff, color: #fff")
      setTimeout(() => {
        x = '<div id="first_col" style="width: 50%; float:left;"><div id="first_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Name</div></div> <div id="second_col" style="width: 50%; float:left;"><div id="second_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Class</div></div> <div id="third_col" style="width: 50%; float:left;"><div id="third_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Number of times student left school early</div></div>'
        document.getElementById('result').innerHTML = document.getElementById('result').innerHTML + x
        document.getElementById('first_append').innerHTML = document.getElementById('first_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res[0]["name"] + "</div>"
        document.getElementById('second_append').innerHTML = document.getElementById('second_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res[0]["class"] + "</div>"
        document.getElementById('third_append').innerHTML = document.getElementById('third_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res[0]["Occurence"] + "</div>"
        s = '<table class="ui table"> <thead><tr><th>Date</th><th>Time</th></tr></thead><tbody></tbody>'
        for (let i = 0; i < res[1].length; ++i) {
          s += "<tr class='"
          if (i % 2 === 0) {
            s += "positive"
          } else {
            s += "error"
          }
          s += "'><td>"
          s += cv(res[1][i]["date"])
          s += "</td><td>"
          s += cv2(res[1][i]["time"])
          s += "</td></tr>"
        }
        s += "</tbody ></table>"
        document.getElementById('new_res').innerHTML = s
      }, 1);
    }
  }).catch((err) => {
    console.log(err)
  })
})
