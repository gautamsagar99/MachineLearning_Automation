import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "***********@gmail.com"
host_pass = "***************"
guest_address = "*********@gmail.com"
subject = "Regarding failure of main.py having less accuracy then the desired one"
content = '''Hello, 
				Developer this is an email regarding to your last commit. It seems that your main.py has not reached to the desired accuracy level.
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')

