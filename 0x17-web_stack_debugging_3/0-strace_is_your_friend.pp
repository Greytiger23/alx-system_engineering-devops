# 0-strace_is_your_friend.pp

exec { 'fix_apache':
  command     => '/bin/sed -i "s/SomeIncorrectDirective/CorrectDirective/g" /etc/apache2/apache2.conf',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Service['apache2'],
}
