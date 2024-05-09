# Puppet manifest to fix apache 500 error
file { '/etc/apache2/sites-available/apache2.conf':
  ensure  => file,
  content => file('/etc/apache2/apache2.conf'),
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/sites-available/apache2.conf'],
} 

exec { 'fix_apache':
  command     => '/bin/sed -i "s/SomeIncorrectDirective/CorrectDirective/g" /etc/apache2/apache2.conf',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Service['apache2'],
}
