#changing config file
file_line { 'Turning off passwordauthentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line { 'IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
