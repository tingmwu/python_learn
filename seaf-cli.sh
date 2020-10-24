# choose a folder where to store the seafile client settings e.g ~/seafile-client


mkdir ~/seafile-client            # create the settings folder

seaf-cli init -d ~/seafile-client  # initialise seafile client with this folder

seaf-cli start

echo seaf-cli sync -l [the id of the librar] -s  [the url + port of server] -d [the folder which the library will be synced with] -u [username on server] -p [password]