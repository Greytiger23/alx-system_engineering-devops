# Increase the worker connections for Nginx
class nginx {
  file { '/etc/nginx/sites-available/default':
    content => "
	worker_connections 1024;
	keepalive_timeout 5;
	",
  }

  # Restart Nginx service to apply changes
  service { 'nginx':
    ensure => running,
    enable => true,
    restart => true,
  }
}
