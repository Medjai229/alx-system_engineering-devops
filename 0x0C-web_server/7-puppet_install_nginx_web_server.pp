# add a stable nginx version
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# update software packages
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure => 'installed',
}

# allow http
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# change folder permissions
exec { 'chmod www':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# index file
file { '/var/www/html/index.html':
  content => 'Hello World!\n',
}

# error 404 file
file { '/var/www/html/error_404.html':
  content => 'Ceci n\'est pas une page\n',
}

# nginx config file
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /var/www/html;
     index       index.html index.nginix-debian.html index.htm;

     location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
     }

     error_page 404 /error_404.html;
     location /error_404 {
        root /var/www/html;
	internal;
     }
}
",
}

# restart nginx
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
