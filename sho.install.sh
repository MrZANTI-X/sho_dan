pkg install rdiff-backup -y
easy_install shodan
sleep 1
pip install shodan
read -p "shodan into api key " AA
shodan init "$AA"
