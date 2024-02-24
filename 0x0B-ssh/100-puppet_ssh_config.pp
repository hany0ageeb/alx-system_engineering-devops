# 4. Client configuration file (w/ Puppet
include stdlib
file_line {'Host':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'Host 100.26.241.78',
  replace => 'true',
}
file_line {'IdentityFile':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => 'true',
}
file_line {'no password':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => 'true'
}
