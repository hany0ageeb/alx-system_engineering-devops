include stdlib
exec {'apt-get update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin']
}
package {'nginx':
  ensure => 'present',
}
file {'/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => 'Hello World!'
}
file {'/usr/share/nginx/html/404.html':
  ensure  => 'file',
  path    => '/usr/share/nginx/html/404.html',
  content => "Ceci n'est pas une page
",
}
file_line {'redirec_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => '	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'server_name _;',
}
file_line {'404':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => '
	error_page 404 /404.html;
	location = /404.html {
		root /usr/share/nginx/html;
		internal;
	}',
  after  => 'listen 80 default_server;',
}
exec {'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin']
}
