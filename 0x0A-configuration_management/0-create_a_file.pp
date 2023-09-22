# Puppet manifest to create a file at /tmp/school
# with specified permission, owner, group and content

file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
