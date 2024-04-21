# Setting up my client config file

file_line { 'ignore passwd auth':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'set identity file':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => 'IdentifyFile ~/.ssh/school
  replace => true,
}
