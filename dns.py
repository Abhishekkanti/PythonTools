import dns.resolver


result = dns.resolver.query('mail.google.com', 'MX')
for exdata in result:
    print (' MX Record:', exdata.exchange )