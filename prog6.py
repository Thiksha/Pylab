
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("prathiksha.16it@cmr.edu.in", "Prathiksha@1998") 

# message to be sent 
message = "hello"

# sending the mail 
s.sendmail("prathiksha.16it@cmr.edu.in", "prathiksha.16it@cmr.edu.in", message) 

# terminating the session 
s.quit() 
