document.getElementById('query-submit').addEventListener('click', (e) => {
  s = JSON.stringify(document.getElementById('query_name').value)
  console.log(s)
  fetch('http://localhost:5000/query', {
    method: 'POST',
    body: s,
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((response) => {
    return response.json()
  }).then((res) => {
    console.log(res)
    if (res.length === 0){
      alert("Student ID is invalid")
    }else{
      document.getElementById('query_name').value = ""
      console.log(res)
      while (document.getElementById('holder').firstChild) {
        document.getElementById('holder').removeChild(document.getElementById('holder').firstChild)
      }
      document.getElementById('holder').setAttribute("style", "border-color: #fff, color: #fff", )
      setTimeout(() => {
        x = '<div id="first_col" style="width: 50%; float:left;"><div id="first_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Number of times student left school early</div></div> <div id="second_col" style="width: 50%; float:left;"><div id="second_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Student Name</div></div> <div id="third_col" style="width: 50%; float:left;"><div id="third_append" style="font-weight: 900; font-size: 0.5em; margin-bottom: 1em; margin-left: 30.8px;">Student Class</div></div>'
        document.getElementById('result').innerHTML = document.getElementById('result').innerHTML + x
        document.getElementById('first_append').innerHTML = document.getElementById('first_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res["Occurence"] + "</div>"
        document.getElementById('second_append').innerHTML = document.getElementById('second_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res["name"] + "</div>"
        document.getElementById('third_append').innerHTML = document.getElementById('third_append').innerHTML + "<br><br>" + "<div style='font-weight: 100'>" + res["class"] + "</div>"
      }, 1);
    }
  }).catch((err) => {
    console.log(err)
  })
})