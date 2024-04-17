# change ulimit in file /etc/default/nginx
file {'/etc/default/nginx':
  ensure  => 'present',
  path    => '/etc/default/nginx',
  content => '# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 4096"',
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure => 'running',
  enable => true,
}
