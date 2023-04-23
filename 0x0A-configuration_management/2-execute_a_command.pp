# killing a process killmenow using puppet
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep -f killmenow',
}
