# apt-get update
exec {'apt-get update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin']
}
->
# install nginx
package {'nginx':
  ensure => 'present',
}
->
# add Hello World!
file {'/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n'
}
->
file {'/usr/share/nginx/html/404.html':
  ensure  => 'file',
  path    => '/usr/share/nginx/html/404.html',
  content => "Ceci n'est pas une page\n",
}
->
file {'/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-enabled/default',
  content => 
'server {
	add_header X-Served-By $hostname;

        listen 80 default_server;

        error_page 404 /404.html;

        location = /404.html {
                root /usr/share/nginx/html;
                internal;
        }

        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

        location / {
                try_files $uri $uri/ =404;
        }
}',
}
->
exec {'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin']
}
->
service {'nginx':
  ensure => 'running',
  name   => 'nginx',
}
