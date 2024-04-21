# Setting up my client config file

file { '/etc/ssh/ssh_config':
  ensure =>file,
  content=> "Host *
  	IdentityFile ~/.ssh/school
  	PasswordAuthentication no
  ",
}
