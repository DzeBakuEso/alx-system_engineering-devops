# Puppet manifest to fix Apache 500 error for WordPress

class fix_apache_500 {
  
  # Ensure PHP MySQL module is installed
  package { 'php-mysql':
    ensure => installed,
  }

  # Ensure Apache service is running
  service { 'apache2':
    ensure    => running,
    enable    => true,
    require   => Package['php-mysql'],
  }
}

# Apply the class
include fix_apache_500
