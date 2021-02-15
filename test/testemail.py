import smtplib
from email.mime.text import MIMEText

emailskempins = "skempins@sjrwmd.com"
emailteams = "3d5f61e9.sjrwmd.com@amer.teams.ms"
emaillist = emailskempins+","+emailteams
# create list from emaillist string
recipients = emaillist.split(",")

msg = MIMEText("""test email body""")

msg["Subject"] = "test email"
msg["From"] = "oracle"
msg["To"] = emaillist

print(msg)

try:
	smtpObj = smtplib.SMTP("localhost")
	smtpObj.sendmail("oracle", recipients, msg.as_string())
	print("sent email")
except:
	print("could not send email")

