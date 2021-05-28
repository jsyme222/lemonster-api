# Virtualmin insstall instructions Ubuntu20.10
[source](https://idroot.us/install-virtualmin-ubuntu-20-04/)
```bash
apt update && apt upgrade
```
```bash
apt install install software-properties-common apt-transport-https wget
```
## Install Webmin
`vim /etc/apt/sources.list`
`# Add repositories
deb http://download.webmin.com/download/repository sarge contrib
deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib
`
# Add GPG key
`wget -q http://www.webmin.com/jcameron-key.asc -O- | sudo apt-key add -`
`apt update && apt install webmin`

###FIREWALL SETTINGS
If firewall in place open port 10000
`sudo ufw allow 10000
sudo ufw reload
`
## Install Virtualmin
`curl -O http://software.virtualmin.com/gpl/scripts/install.sh`
`chmod +x ./install.sh`
`. ./install.sh`
## Access at [https://loclahost:1000](https://localhost:10000)
