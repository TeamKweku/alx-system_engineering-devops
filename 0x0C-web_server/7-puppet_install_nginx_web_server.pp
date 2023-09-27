# a puppet manifest that installs and configures nginx

# install nginx 
class { 'nginx': }

# Configure Nginx to listen on port 80
file {  '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {\n  listen 80;\n  root /var/www/html;\n  index index.html;\n  location / {\n    add_header Content-Type text/html;\n    return 200 'Hello World!';\n  }\n  location /redirect_me {\n    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n  }\n}\n",
}

# Enable the default site
nginx::resource::vhost { 'default':
  ensure   => 'present',
  www_root => '/var/www/html',
}

# Test the Nginx configuration and reload Nginx
exec { 'nginx-config-test':
  command => '/usr/sbin/nginx -t',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/sites-available/default'], Nginx::Resource::Vhost['default']],
}
