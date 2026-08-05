'''Django Tutorial: Custom Domain Name & Free HTTPS / SSL SetupThese two lectures cover point-to-point instructions for setting up a custom domain name registered through a domain registrar (e.g., Namecheap or GoDaddy) pointing to your Linux server (e.g., Linode/DigitalOcean/AWS EC2), followed by enabling encrypted HTTPS traffic using free SSL/TLS certificates from Let's Encrypt and Certbot.  Part 1: Setting Up a Custom Domain NameTo map a purchased custom domain name (e.g., yourdomain.com) to your server's IP address:1. Configure Domain Registrar NameserversLog in to your domain provider (Namecheap, GoDaddy, Google Domains, etc.).  Navigate to Domain List / DNS Management and switch Nameservers from default to custom nameservers provided by your hosting provider (e.g., Linode Nameservers: ns1.linode.com, ns2.linode.com, etc.).2. Configure DNS Manager / RecordsIn your hosting provider's DNS Manager (or directly in your registrar's DNS settings):A Record: Points your root domain (@ / yourdomain.com) to your server's public IP address.CNAME Record: Points www to your root domain (yourdomain.com) or server IP.3. Update Django Settings (ALLOWED_HOSTS)In django_project/settings.py, allow incoming requests sent to your new domain name:  PythonALLOWED_HOSTS = [
    'YOUR_SERVER_IP',
    'yourdomain.com',
    'www.yourdomain.com',
]
4. Update Apache Virtual Host ConfigurationEdit your Apache site configuration file (/etc/apache2/sites-available/django_project.conf):  Apache<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    Alias /static /home/myuser/django_blog/static
    <Directory /home/myuser/django_blog/static>
        Require all granted
    </Directory>

    Alias /media /home/myuser/django_blog/media
    <Directory /home/myuser/django_blog/media>
        Require all granted
    </Directory>

    <Directory /home/myuser/django_blog/django_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess django_app python-path=/home/myuser/django_blog python-home=/home/myuser/django_env
    WSGIProcessGroup django_app
    WSGIScriptAlias / /home/myuser/django_blog/django_project/wsgi.py
</VirtualHost>
Restart Apache to apply changes:Bashsudo service apache2 restart'''