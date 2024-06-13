# Increase the limit of nginx requests

exec { 'increase_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
