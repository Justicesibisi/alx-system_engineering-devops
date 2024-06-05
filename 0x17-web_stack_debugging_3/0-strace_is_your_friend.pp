# Ensure the /var/www/html/index.php file exists
file { '/var/www/html/index.php':
  ensure  => file,
  content => "<?php\n  phpinfo();\n?>",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure the Apache service is running
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.php'],
}

