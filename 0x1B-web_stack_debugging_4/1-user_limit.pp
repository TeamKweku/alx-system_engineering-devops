# A puppet manifest that changes user rate limit
exec { 'change_limit_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'change_limit_to_40':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}

