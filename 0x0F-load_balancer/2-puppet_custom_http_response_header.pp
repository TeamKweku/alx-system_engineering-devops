# setup a new ubuntu server with nginx and custom HTTP header

# update system
exec {  'update system':
  command => '/usr/bin/apt-get update',
}

# install nginx server
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

# create custom index.html
file {  '/var/www/html/index.html':
  content => 'Hello World!',
}

# redirect 301 Moved Permanently
exec {  'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=xJJsoquu70o/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Add custom HTTP headers 
exec {  'HTTP header':
  command  =>  'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# start nginx servcie
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
