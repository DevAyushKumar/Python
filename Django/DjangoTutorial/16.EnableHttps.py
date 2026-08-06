'''Part 2: Enabling HTTPS with Free SSL via Let's Encrypt & CertbotLet’s Encrypt provides free, automated SSL/TLS certificates. Certbot automatically acquires the certificate and configures Apache to handle HTTPS traffic.  1. Install Certbot for ApacheOn your Ubuntu server, install the required Certbot dependencies:Bashsudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt update
sudo apt install python-certbot-apache
2. Obtain & Install SSL CertificateRun Certbot specifying the Apache plugin:Bashsudo certbot --apache -d yourdomain.com -d www.yourdomain.com
Interactive Prompts:Enter an email address for urgent renewal and security notices.Agree to the Terms of Service.Select whether to automatically redirect HTTP traffic to HTTPS (Option 2: Redirect is strongly recommended to enforce secure connections across your site).Certbot will generate a new HTTPS Apache config file (django_project-le-ssl.conf) automatically.3. Update Django Security Settings for HTTPSTo ensure Django handles secure cookies and redirects correctly over HTTPS, update your production settings in django_project/settings.py:  Python# Force HTTPS redirect inside Django (optional if Apache already handles 301 redirects)
SECURE_SSL_REDIRECT = True

# Secure Session & CSRF Cookies over HTTPS only
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Protect against MIME type sniffing & XSS
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
Run Django’s deployment security check to verify your production setup:Bashpython manage.py check --deploy
4. Automatic Certificate Renewal TestLet’s Encrypt certificates last 90 days. Certbot installs a system cron job or systemd timer to renew them automatically. You can verify automatic renewal with a dry run:Bashsudo certbot renew --dry-run
Finally, restart Apache:Bashsudo service apache2 restart'''