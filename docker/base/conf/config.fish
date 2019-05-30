function fish_prompt

  if [ $SERVER_ENV = 'development' ]
    set_color -b green
    set_color black
  else if [ $SERVER_ENV = 'staging' ]
    set_color -b yellow
    set_color black
  else if [ $SERVER_ENV = 'production' ]
    set_color -b red
    set_color white
  else
    set_color -b 999
  end

  printf ' '
  printf $SERVER_ENV
  printf ' '

  set_color -b normal
  set_color yellow
  printf ' ➜ '
  set_color cyan
  printf (basename $PWD)
  printf ' 🐟 '
  set_color normal
end

eval (envkey-source)
source $HOME/.poetry/env
