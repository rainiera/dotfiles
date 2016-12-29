# debian "jessie"

# update repoz
sudo apt-get update

# git
sudo apt-get install git

# tmux
sudo apt-get install tmux

# zsh
sudo apt-get install zsh
sudo sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
sudo chsh rainiera -s /bin/zsh

# vim
git clone git://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
echo 'set number' >> ~/.vimrc
echo 'set mouse=a' >> ~/.vimrc

# pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

# venv
sudo pip install virtualenv

# pyenv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"

# 2.7.13
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
pyenv install 2.7.13

# 3.6.0 ¯\_(ツ)_/¯
pyenv install 3.6.0

# pyenv-virtualenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
exec "$SHELL"
pyenv virtualenv 2.7.13 venv
pyenv activate venv

# rabbitmq + celery
sudo apt-get install rabbitmq-server
pip install celery

# erlang + elixir
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb
sudo apt-get update
sudo apt-get install esl-erlang
sudo apt-get install elixir

# assist with user installs
echo 'export PATH="$PATH:/home/rainiera/.local/bin"' >> ~/.zshrc

# scipy stack
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

# github
git config --global user.email "rainier@utexas.edu"
git config --global user.name "rainiera"

# add keys - follow interactive prompt
# TODO `expect` or use GitHub API
ssh-keygen -t rsa -b 4096 -C "rainier@utexas.edu"
# ssh-add ~/.ssh/id_rsa
# cat ~/.ssh/id_rsa.pub
# copy-paste new key here: https://github.com/settings/keys
