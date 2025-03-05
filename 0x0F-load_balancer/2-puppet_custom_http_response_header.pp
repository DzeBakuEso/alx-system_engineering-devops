# 2-puppet_custom_http_response_header.pp
# This Puppet script configures a custom HTTP header for Nginx on an Ubuntu server

# Ensure that nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Create a custom Nginx configuration for HTTP headers
file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure  => file,
  content => "add_header X-Served-By ${::hostname};\n",
  notify  => Service['nginx'], # Notify Nginx service to reload when the file changes
}

# Ensure the default nginx configuration is in place
file { '/etc/nginx/sites-available/default':
  ensure  => present,  # Keep existing configuration
  notify  => Service['nginx'],
}
