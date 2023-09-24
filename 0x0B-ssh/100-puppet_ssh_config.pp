# config puppet to make changes to configuration file

file {  "/etc/ssh/ssh_config":
  owner	=> 'root',
  group	=> 'root',
  mode    => '0644',
  content =>  "
    Host 18.206.202.36
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",

}
