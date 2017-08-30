from django.core.mail import send_mail
class mail():
       
    def mail(self, AdminEmail, ToEmail):
        subject = "missing username"
        message = "Your GitHub account name is missing, please change your name by either logging into your githug profile, or by following the below link"
        sender = AdminEmail
        recipients = [ToEmail]
        send_mail(subject, message, sender, recipients)