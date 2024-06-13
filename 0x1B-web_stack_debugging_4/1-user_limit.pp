# Change OS Config

exec { 'increase_hard_user_limit':
  command => 'sed -i "/holberton hard/s/5/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
exec { 'increase_soft_user_limit':
  command => 'sed -i "/holberton soft/s/4/50000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
