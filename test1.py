import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key="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")
from_email = Email("jmj6ry@virginia.edu")
to_email = To("anjesat@outlook.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)