import smtplib as x

y = x.SMTP("smtp.gmail.com",587)

y.starttls()

y.login("retrsak@gmail.com","*********")

subject = "testing of smtp"
body = "lets check this out if this is running or not if u got the message then congrats u learned new thing" \
       "this is second message lets check this out"

Message = f"subject:{subject}\n\n{body}"

xyz = ['rsaka99@gmail.com','rahulsaka11@hotmail.com']

y.sendmail("retrsak",xyz,Message)

print("mail sent from retrsak@gmail.com")

y.quit()