'''Django Tutorial Part 14: Deploying to a Linux Server (Ubuntu & Apache)This lecture covers deploying a Django application from scratch to an Ubuntu Linux server (such as Linode/DigitalOcean/AWS EC2). It details securing the server with SSH keys and firewalls, setting up Apache with mod_wsgi, configuring static files, and securely managing environment variables in production.  1. Initial Server Setup & SecurityCreating a Non-Root UserLog in as root and create a dedicated administrative user:Bashssh root@YOUR_SERVER_IP

# Create user and grant sudo permissions
adduser myuser
usermod -aG sudo myuser
SSH Key Authentication SetupDisable password authentication in favor of public key authentication:Bash# On your local machine: copy key to server
ssh-copy-id myuser@YOUR_SERVER_IP

# Log back into server as myuser
ssh myuser@YOUR_SERVER_IP
Firewall Configuration (UFW)Enable the Uncomplicated Firewall (UFW) to restrict incoming connections:Bashsudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow www
sudo ufw enable
2. Environment & Project Dependencies SetupInstall required system packages, set up Python venv, and pull down the project:Bash# Install Python, pip, Apache, and WSGI module
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev apache2 libapache2-mod-wsgi-py3 git

# Create virtual environment inside your user directory
cd ~
python3 -m venv django_env
source django_env/bin/activate

# Clone project repository
git clone https://github.com/your-username/django_blog.git
cd django_blog

# Install dependencies
pip install -r requirements.txt
3. Production Configuration (settings.py & JSON Config)Avoid putting secret keys, email passwords, and database credentials directly in settings.py. Store them in a secure JSON configuration file on the server (e.g., /etc/config.json).Create /etc/config.jsonJSON{
    "SECRET_KEY": "your-production-secret-key",
    "EMAIL_USER": "your-email@gmail.com",
    "EMAIL_PASS": "your-app-password",
    "AWS_ACCESS_KEY_ID": "your-aws-key",
    "AWS_SECRET_ACCESS_KEY": "your-aws-secret-key",
    "AWS_STORAGE_BUCKET_NAME": "your-bucket-name"
}
Update django_project/settings.pyPythonimport json

# Load secret configuration from JSON file
with open('/etc/config.json') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']

# Turn off DEBUG in production
DEBUG = False

# Add your domain or server IP
ALLOWED_HOSTS = ['YOUR_SERVER_IP', 'yourdomain.com']

# Static files management for Apache
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
Collect static files into STATIC_ROOT:Bashpython manage.py collectstatic
4. Apache & Mod_WSGI ConfigurationCreate an Apache virtual host file to route web traffic through WSGI to your Django application.Create /etc/apache2/sites-available/django_project.confApache<VirtualHost *:80>
    ServerName YOUR_SERVER_IP

    # Static file directory configuration
    Alias /static /home/myuser/django_blog/static
    <Directory /home/myuser/django_blog/static>
        Require all granted
    </Directory>

    # Media file directory configuration (if hosted locally instead of S3)
    Alias /media /home/myuser/django_blog/media
    <Directory /home/myuser/django_blog/media>
        Require all granted
    </Directory>

    # WSGI Daemon Mode setup
    <Directory /home/myuser/django_blog/django_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess django_app python-path=/home/myuser/django_blog python-home=/home/myuser/django_env
    WSGIProcessGroup django_app
    WSGIScriptAlias / /home/myuser/django_blog/django_project/wsgi.py
</VirtualHost>
Enable Site & Restart ApacheBash# Enable the new site configuration
sudo a2ensite django_project

# Disable default Apache site
sudo a2dissite 000-default

# Fix permission issues for SQLite / uploaded media (if using local database)
sudo chown :www-data /home/myuser/django_blog/db.sqlite3
sudo chown :www-data /home/myuser/django_blog

# Restart Apache service
sudo service apache2 restart'''