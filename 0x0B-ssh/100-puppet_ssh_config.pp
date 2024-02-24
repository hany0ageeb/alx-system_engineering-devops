# 4. Client configuration file (w/ Puppet)
file { '/root/.ssh/config':
  ensure  => 'file',
  content => 'Host 100.26.241.78
        IdentityFile ~/.ssh/school
        PasswordAuthentication no',
}
