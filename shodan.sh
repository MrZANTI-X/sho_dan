A1="\e[0;31m" #Red
A2="\e[0;33m" # Yellow
A3="\e[0;34m" # Blue
A4="\e[0;32m" #green
bash banner.sh
line() {
echo -en $A2 '
[  0 ] clear-Desplay
[  1 ] shodan-install
[  2 ] run-shodan
[  3 ] shodan-version
[  4 ] open-shodan
[  5 ] shodan-api
[  6 ] count-webcam
[  7 ] count-cctv
[  8 ] shodan-host
[  9 ] myip
[ 10 ] shodan-info
[ 11 ] ip-scan
[  S ] data-read
[  A ] about
'
}
line
read -p "enter : " data
case $data in
0)
  echo "clear-Desplay "
  clear
;;
1)
  echo "shodan-install "
  bash sho.install.sh
  clear
;;
2)
  echo "ren-shodan"
  bash sho-dan.sh
;;
3)
  echo "shodan-version "
  shodan version
;;
4)
  echo "open-shodan "
  termux-open-url https://www.shodan.io/
;;
5)
  echo "shodan-api"
  read -p "En : " hart
  shodan init $hart
  clear
;;
6)
  echo "count-webcam"
  shodan count 'webcamxp'
;;
7)
  echo "count-cctv"
  shodan count cctv
;;
8)
  echo "shodan-host"
  read -p "enter ip : " SSD
  shodan host $SSD
;;
9)
  echo "myip "
  shodan myip
;;
10)
  echo "shodan-info"
  shodan info 
;;
11)
  echo "ip-scan "
  python ip-scaner.py
;;
S*)
  echo "data-file"
  read -p "enter file name " AAS
  read -p "enter serach enquiry " AQW
  shodan download $AAS $AQW
;;
A*)
  echo "about "
  termux-open-url https://youtube.com/channel/UCFm8ZvT8ZZ6RpqpWKRy9ZMg
;;
esac
