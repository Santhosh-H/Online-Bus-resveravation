def sending_mail(to_adress,subject,body):
    from pickle import load as view
    with open("Mail_credentials.dat","rb") as Email_Credentials_file:
        data = view(Email_Credentials_file)
        sender_id = data[0]
        sender_pass = data[1]
        
    import smtplib
    with smtplib.SMTP('smtp.gmail.com',587) as smptp:
        smptp.ehlo()
        smptp.starttls()
        smptp.ehlo()
        smptp.login(sender_id,sender_pass)
        msge = f'Subject: {subject}\n\n{body}'
        smptp.sendmail('Eato',to_adress,msge)