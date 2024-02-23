# Using Puppet, install flask from pip3.
# Requirements:
#	1. Install flask
#	2. Version must be 2.1.0
#
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
