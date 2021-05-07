#hello user 
#mode by Mr. zanti -X
import requests, re , colorama
colorama.init()
print("hello user")
print("""
[  1 ] US
[  2 ] JP
[  3 ] IT
[  4 ] KR
[  5 ] FR
[  6 ] DE
[  7 ] TW
[  8 ] RU
[  9 ] GB
[ 10 ] CZ
[ 11 ] TR
[ 12 ] AT
[ 13 ] CH
[ 14 ] ES
[ 15 ] CA
[ 16 ] SE
[ 17 ] IL
[ 18 ] PL
[ 19 ] NO
[ 20 ] RO
[ 21 ] IN
[ 22 ] VN
[ 23 ] BE
[ 24 ] BR
[ 25 ] BG
[ 26 ] ID
[ 27 ] DK
[ 28 ] MX
[ 29 ] FI
[ 30 ] CN
[ 31 ] CL
[ 32 ] ZA
[ 33 ] SK
[ 34 ] HU
[ 35 ] IE
[ 36 ] EG
[ 37 ] UA
[ 38 ] RS
[ 39 ] HK
[ 40 ] GR
""")
try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 91+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("serach = ", ip)
except:
    pass
finally:
    exit()

