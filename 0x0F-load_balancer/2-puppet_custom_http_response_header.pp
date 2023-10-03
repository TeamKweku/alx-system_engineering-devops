# Class: nginx_config
#
# This class manages the configuration of the Nginx web server
# setting custom headers
#

class nginx_config {

  package { 'nginx':
    ensure => 'installed',
  }

  file { '/var/www/html':
    ensure => 'directory',
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!\n',
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page\n",
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By '${facts['networking']['hostname']}';
        root /var/www/html;
        index index.html index.htm;

        location /redirect_me {
          return 301 https://www.youtube.com/watch?v=xJJsoquu70o/;
        }

        error_page 404 /404.html;
        location /404 {
          root /var/www/html;
          internal;
        }
      }
    ",
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_config
