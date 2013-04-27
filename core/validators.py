# core/validators.py
from __future__ import unicode_literals

import smtplib

from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator, email_re
from django.core.exceptions import ValidationError

import dns.resolver


class EmailValidator(EmailValidator):

    def __call__(self, value):
        super(EmailValidator, self).__call__(value)
        try:
            hostname = value.split('@')[-1]
        except KeyError:
            raise ValidationError(_('Enter a valid email address.'))

        try:
            for server in [str(r.exchange).rstrip('.')
                           for r in dns.resolver.query(hostname, 'MX')]:
                try:
                    smtp = smtplib.SMTP()
                    smtp.connect(server)
                    status = smtp.helo()
                    if status[0] != 250:
                        continue
                    smtp.mail('')
                    status = smtp.rcpt(value)
                    if status[0] != 250:
                        raise ValidationError(_('Invalid email address.'))
                    break
                except smtplib.SMTPServerDisconnected:
                    break
                except smtplib.SMTPConnectError:
                    continue
        except dns.resolver.NXDOMAIN:
            raise ValidationError(_('Nonexistent domain.'))
        except dns.resolver.NoAnswer:
            raise ValidationError(_('Nonexistent email address.'))

# usage
validate_email = EmailValidator(
    email_re,
    _('Enter a valid email address.'),
    'invalid'
)