# Puppet manifest to fix apache 500 error
file{'/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => file('/path/to/000-default.conf'),
}

service{'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/sites-available/000-default.conf'],
} 
