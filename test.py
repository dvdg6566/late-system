import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cepy3testing@gmail.com", "testing777")

fromaddr = "cepy3testing@gmail.com"
toaddr = "czhdaniel@gmail.com,potato7154@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing"
msg.attach(MIMEText("Hello123", 'plain'))

server.sendmail(fromaddr,toaddr, msg.as_string())
server.quit()