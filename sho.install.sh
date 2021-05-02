pkg install termux-api -y
pkg install rdiff-backup -y
easy_install shodan
sleep 1
pip install shodan
read -p "shodan into api key " AA
shodan init "$AA"
read -p "update now (y/n) " SGF
case $SGF in
y*)
   echo "update now " 
   git clone https://github.com/zanti1/sho_dan.git
   clear
;;
n*)
   echo "ok !"
;;
esac
