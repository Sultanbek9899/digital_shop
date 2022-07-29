import pdfkit
from io import BytesIO

from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse

from backend.config.celery import app
from backend.apps.service.models import Product


@app.task(bind=True)
def send_email_with_report(self):
    products = Product.objects.all()
    template = get_template("report.html")
    html=render_to_string("report.html",{"products":products})
    options = {
        'page-size': 'A4',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    # config = pdfkit.configuration(wkhtmltopdf=bytes('/usr/bin/wkhtmltopdf', 'utf-8'))
    # pdf=pdfkit.from_string(html, configuration=config)
    from_email = settings.EMAIL_HOST_USER
    to_email = settings.REPORT_EMAIL_RECEIVER
    message = EmailMessage(
        "Quantity Report",
        "asfasf",
        from_email,
        [to_email]
    )
    # message.attach("quantity_report.pdf", pdf, "application/pdf")
    # message.content_subtype="pdf"
    # message.encoding = 'utf-8'
    message.send()