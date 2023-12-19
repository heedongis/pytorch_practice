import re

string = '''
{
"국가코드":[
 {
  "codeTypeCode": "country",
  "codeName": "KR",
  "description": "아프가니스탄",
  "code_en": "Afghanistan"
 },
 {
  "codeTypeCode": "country",
  "codeName": "GH",
  "description": "올란드 제도",
  "code_en": "Åland Islands"
 },
 {
  "codeTypeCode": "country",
  "codeName": "GA",
  "description": "알바니아",
  "code_en": "Albania"
 },
 {
  "codeTypeCode": "country" ,
  "codeName": "GY",
  "description": "알제리",
  "code_en": "Algeria"
 },
 {
  "codeTypeCode": "country" ,
  "codeName": "GM",
  "description": "아메리칸사모아",
  "code_en": "American Samoa"
 },
 {
  "codeTypeCode": "country",
  "codeName": "GG",
  "description": "안도라",
  "code_en": "Angola"
 },
 {
  "codeTypeCode": "country",
  "codeName": "GP",
  "description": "앙골라",
  "code_en": "Angola"
 },
 {
  "codeTypeCode": "country",
  "codeName": "GT",
  "description": "앵귈라",
  "code_en": "Anguilla"
 },
 {
  "codeTypeCode": "country" 9,
  "codeName": "GU",
  "description": "남극",
  "code_en": "Antarctica"
 },
 {
  "codeTypeCode": "country" 10,
  "codeName": "GD",
  "description": "앤티가 바부다",
  "code_en": "Antigua and Barbuda"
 },
 {
  "codeTypeCode": "country" 11,
  "codeName": "GR",
  "description": "아르헨티나",
  "code_en": "Argentina"
 },
 {
  "codeTypeCode": "country" 12,
  "codeName": "GL",
  "description": "아르메니아",
  "code_en": "Armenia"
 },
 {
  "codeTypeCode": "country" 13,
  "codeName": "GN",
  "description": "아루바",
  "code_en": "Aruba"
 },
 {
  "codeTypeCode": "country" 14,
  "codeName": "GW",
  "description": "오스트레일리아",
  "code_en": "Australia"
 },
 {
  "codeTypeCode": "country" 15,
  "codeName": "NA",
  "description": "오스트리아",
  "code_en": "Austria"
 },
 {
  "codeTypeCode": "country" 16,
  "codeName": "NR",
  "description": "아제르바이잔",
  "code_en": "Azerbaijan"
 },
 {
  "codeTypeCode": "country" 17,
  "codeName": "NG",
  "description": "바하마",
  "code_en": "Bahamas"
 },
 {
  "codeTypeCode": "country" 18,
  "codeName": "AQ",
  "description": "바레인",
  "code_en": "Bahrain"
 },
 {
  "codeTypeCode": "country" 19,
  "codeName": "ZA",
  "description": "방글라데시",
  "code_en": "Bangladesh"
 },
 {
  "codeTypeCode": "country" 20,
  "codeName": "NL",
  "description": "바베이도스",
  "code_en": "Barbados"
 },
 {
  "codeTypeCode": "country" 21,
  "codeName": "AN",
  "description": "벨라루스",
  "code_en": "Belarus"
 },
 {
  "codeTypeCode": "country" 22,
  "codeName": "NP",
  "description": "벨기에",
  "code_en": "Belgium"
 },
 {
  "codeTypeCode": "country" 23,
  "codeName": "NO",
  "description": "벨리즈",
  "code_en": "Belize"
 },
 {
  "codeTypeCode": "country" 24,
  "codeName": "NF",
  "description": "베냉",
  "code_en": "Benin"
 },
 {
  "codeTypeCode": "country" 25,
  "codeName": "NC",
  "description": "버뮤다",
  "code_en": "Bermuda ls."
 },
 {
  "codeTypeCode": "country" 26,
  "codeName": "NZ",
  "description": "부탄",
  "code_en": "Bhutan"
 },
 {
  "codeTypeCode": "country" 27,
  "codeName": "NU",
  "description": "볼리비아",
  "code_en": "Bolivia"
 },
 {
  "codeTypeCode": "country" 28,
  "codeName": "NE",
  "description": "보스니아 헤르체고비나",
  "code_en": "Bosnia and Herzegovina"
 },
 {
  "codeTypeCode": "country" 29,
  "codeName": "NI",
  "description": "보츠와나",
  "code_en": "Botswana"
 },
 {
  "codeTypeCode": "country" 30,
  "codeName": "DK",
  "description": "부베섬",
  "code_en": "Bouvet Island"
 },
 {
  "codeTypeCode": "country" 31,
  "codeName": "DO",
  "description": "브라질",
  "code_en": "Brazil"
 },
 {
  "codeTypeCode": "country" 32,
  "codeName": "DM",
  "description": "영국령 인도양 지역",
  "code_en": "British Indian Ocean Territory"
 },
 {
  "codeTypeCode": "country" 33,
  "codeName": "DE",
  "description": "영국령 버진아일랜드",
  "code_en": "British Virgin Islands"
 },
 {
  "codeTypeCode": "country" 34,
  "codeName": "TL",
  "description": "브루나이",
  "code_en": "Brunei Darussalam"
 },
 {
  "codeTypeCode": "country" 35,
  "codeName": "LA",
  "description": "불가리아",
  "code_en": "Bulgaria"
 },
 {
  "codeTypeCode": "country" 36,
  "codeName": "LR",
  "description": "부르키나파소",
  "code_en": "Burkina Faso"
 },
 {
  "codeTypeCode": "country" 37,
  "codeName": "LV",
  "description": "부룬디",
  "code_en": "Burundi"
 },
 {
  "codeTypeCode": "country" 38,
  "codeName": "RU",
  "description": "카보베르데",
  "code_en": "Cabo Verde"
 },
 {
  "codeTypeCode": "country" 39,
  "codeName": "LB",
  "description": "캄보디아",
  "code_en": "Cambodia"
 },
 {
  "codeTypeCode": "country" 40,
  "codeName": "LS",
  "description": "카메룬",
  "code_en": "Cameroon"
 },
 {
  "codeTypeCode": "country" 41,
  "codeName": "RE",
  "description": "캐나다",
  "code_en": "Canada"
 },
 {
  "codeTypeCode": "country" 42,
  "codeName": "RO",
  "description": "케이맨 제도",
  "code_en": "Cayman Islands"
 },
 {
  "codeTypeCode": "country" 43,
  "codeName": "LU",
  "description": "중앙아프리카 공화국",
  "code_en": "Central African Republic"
 },
 {
  "codeTypeCode": "country" 44,
  "codeName": "RW",
  "description": "차드",
  "code_en": "Chad"
 },
 {
  "codeTypeCode": "country" 45,
  "codeName": "LY",
  "description": "칠레",
  "code_en": "Chile"
 },
 {
  "codeTypeCode": "country" 46,
  "codeName": "LT",
  "description": "중국",
  "code_en": "China"
 },
 {
  "codeTypeCode": "country" 47,
  "codeName": "LI",
  "description": "크리스마스 섬",
  "code_en": "Christmas Island"
 },
 {
  "codeTypeCode": "country" 48,
  "codeName": "MG",
  "description": "코코스 제도",
  "code_en": "Cocos  Islands"
 },
 {
  "codeTypeCode": "country" 49,
  "codeName": "MQ",
  "description": "콜롬비아",
  "code_en": "Colombia"
 },
 {
  "codeTypeCode": "country" 50,
  "codeName": "MH",
  "description": "코모로",
  "code_en": "Comoros"
 },
 {
  "codeTypeCode": "country" 51,
  "codeName": "YT",
  "description": "콩고 공화국",
  "code_en": "Congo"
 },
 {
  "codeTypeCode": "country" 52,
  "codeName": "MO",
  "description": "콩고 민주 공화국",
  "code_en": "Congo "
 },
 {
  "codeTypeCode": "country" 53,
  "codeName": "MK",
  "description": "쿡 제도",
  "code_en": "Cook Islands"
 },
 {
  "codeTypeCode": "country" 54,
  "codeName": "MW",
  "description": "코스타리카",
  "code_en": "Costa Rica"
 },
 {
  "codeTypeCode": "country" 55,
  "codeName": "MY",
  "description": "코트디부아르",
  "code_en": "Côte d'Ivoire"
 },
 {
  "codeTypeCode": "country" 56,
  "codeName": "ML",
  "description": "크로아티아",
  "code_en": "Croatia"
 },
 {
  "codeTypeCode": "country" 57,
  "codeName": "IM",
  "description": "쿠바",
  "code_en": "Cuba"
 },
 {
  "codeTypeCode": "country" 58,
  "codeName": "MX",
  "description": "키프로스",
  "code_en": "Cyprus"
 },
 {
  "codeTypeCode": "country" 59,
  "codeName": "MC",
  "description": "체코",
  "code_en": "Czechia"
 },
 {
  "codeTypeCode": "country" 60,
  "codeName": "MA",
  "description": "덴마크",
  "code_en": "Danmark"
 },
 {
  "codeTypeCode": "country" 61,
  "codeName": "MU",
  "description": "지부티",
  "code_en": "Djibouti"
 },
 {
  "codeTypeCode": "country" 62,
  "codeName": "MR",
  "description": "도미니카 연방",
  "code_en": "Dominica"
 },
 {
  "codeTypeCode": "country" 63,
  "codeName": "MZ",
  "description": "도미니카공화국",
  "code_en": "Dominican Republic"
 },
 {
  "codeTypeCode": "country" 64,
  "codeName": "ME",
  "description": "동티모르",
  "code_en": "East Timor Leste"
 },
 {
  "codeTypeCode": "country" 65,
  "codeName": "MS",
  "description": "에콰도르",
  "code_en": "Ecuador"
 },
 {
  "codeTypeCode": "country" 66,
  "codeName": "MD",
  "description": "이집트",
  "code_en": "Egypt"
 },
 {
  "codeTypeCode": "country" 67,
  "codeName": "MV",
  "description": "엘살바도르",
  "code_en": "El Salvador"
 },
 {
  "codeTypeCode": "country" 68,
  "codeName": "MT",
  "description": "적도 기니",
  "code_en": "Equatorial Guinea"
 },
 {
  "codeTypeCode": "country" 69,
  "codeName": "MN",
  "description": "에리트레아",
  "code_en": "Eritrea"
 },
 {
  "codeTypeCode": "country" 70,
  "codeName": "US",
  "description": "에스토니아",
  "code_en": "Estonia"
 },
 {
  "codeTypeCode": "country" 71,
  "codeName": "UM",
  "description": "에스와티니",
  "code_en": "Eswatini"
 },
 {
  "codeTypeCode": "country" 72,
  "codeName": "VI",
  "description": "에티오피아",
  "code_en": "Ethiopia"
 },
 {
  "codeTypeCode": "country" 73,
  "codeName": "MM",
  "description": "포클랜드 제도",
  "code_en": "Falkland Islands "
 },
 {
  "codeTypeCode": "country" 74,
  "codeName": "FM",
  "description": "페로 제도",
  "code_en": "Faroe Islands"
 },
 {
  "codeTypeCode": "country" 75,
  "codeName": "VU",
  "description": "피지",
  "code_en": "Fiji"
 },
 {
  "codeTypeCode": "country" 76,
  "codeName": "BH",
  "description": "핀란드",
  "code_en": "Finland"
 },
 {
  "codeTypeCode": "country" 77,
  "codeName": "BB",
  "description": "프랑스",
  "code_en": "France"
 },
 {
  "codeTypeCode": "country" 78,
  "codeName": "VA",
  "description": "프랑스령 기아나",
  "code_en": "French Guiana"
 },
 {
  "codeTypeCode": "country" 79,
  "codeName": "BS",
  "description": "프랑스령 폴리네시아",
  "code_en": "French Polynesia"
 },
 {
  "codeTypeCode": "country" 80,
  "codeName": "BD",
  "description": "프랑스령 남방 및 남극",
  "code_en": "French Southern Territories"
 },
 {
  "codeTypeCode": "country" 81,
  "codeName": "BM",
  "description": "가봉",
  "code_en": "Gabon"
 },
 {
  "codeTypeCode": "country" 82,
  "codeName": "BJ",
  "description": "감비아",
  "code_en": "Gambia"
 },
 {
  "codeTypeCode": "country" 83,
  "codeName": "VE",
  "description": "조지아",
  "code_en": "Georgia"
 },
 {
  "codeTypeCode": "country" 84,
  "codeName": "VN",
  "description": "독일",
  "code_en": "Germany"
 },
 {
  "codeTypeCode": "country" 85,
  "codeName": "BE",
  "description": "가나",
  "code_en": "Ghana"
 },
 {
  "codeTypeCode": "country" 86,
  "codeName": "BY",
  "description": "지브롤터",
  "code_en": "Gibraltar"
 },
 {
  "codeTypeCode": "country" 87,
  "codeName": "BZ",
  "description": "그리스",
  "code_en": "Greece"
 },
 {
  "codeTypeCode": "country" 88,
  "codeName": "BA",
  "description": "그린란드",
  "code_en": "Greenland"
 },
 {
  "codeTypeCode": "country" 89,
  "codeName": "BW",
  "description": "그레나다",
  "code_en": "Grenada"
 },
 {
  "codeTypeCode": "country" 90,
  "codeName": "BO",
  "description": "과들루프",
  "code_en": "Guadeloupe"
 },
 {
  "codeTypeCode": "country" 91,
  "codeName": "BI",
  "description": "괌",
  "code_en": "Guam"
 },
 {
  "codeTypeCode": "country" 92,
  "codeName": "BF",
  "description": "과테말라",
  "code_en": "Guatemala"
 },
 {
  "codeTypeCode": "country" 93,
  "codeName": "BV",
  "description": "건지섬",
  "code_en": "Guernsey"
 },
 {
  "codeTypeCode": "country" 94,
  "codeName": "BT",
  "description": "기니",
  "code_en": "Guinea"
 },
 {
  "codeTypeCode": "country" 95,
  "codeName": "MP",
  "description": "기니비사우",
  "code_en": "Guinea-Bissau"
 },
 {
  "codeTypeCode": "country" 96,
  "codeName": "BG",
  "description": "가이아나",
  "code_en": "Guyana"
 },
 {
  "codeTypeCode": "country" 97,
  "codeName": "BR",
  "description": "아이티",
  "code_en": "Haiti"
 },
 {
  "codeTypeCode": "country" 98,
  "codeName": "BN",
  "description": "허드 맥도널드 제도",
  "code_en": "Heard Island and McDonald Islands"
 },
 {
  "codeTypeCode": "country" 99,
  "codeName": "WS",
  "description": "온두라스",
  "code_en": "Honduras"
 },
 {
  "codeTypeCode": "country" 100,
  "codeName": "SA",
  "description": "홍콩",
  "code_en": "Hong Kong"
 },
 {
  "codeTypeCode": "country" 101,
  "codeName": "GS",
  "description": "헝가리",
  "code_en": "Hungary"
 },
 {
  "codeTypeCode": "country" 102,
  "codeName": "SM",
  "description": "아이슬란드",
  "code_en": "Iceland"
 },
 {
  "codeTypeCode": "country" 103,
  "codeName": "ST",
  "description": "인도",
  "code_en": "India"
 },
 {
  "codeTypeCode": "country" 104,
  "codeName": "PM",
  "description": "인도네시아",
  "code_en": "Indonesia"
 },
 {
  "codeTypeCode": "country" 105,
  "codeName": "EH",
  "description": "이란",
  "code_en": "Iran "
 },
 {
  "codeTypeCode": "country" 106,
  "codeName": "SN",
  "description": "이라크",
  "code_en": "Iraq"
 },
 {
  "codeTypeCode": "country" 107,
  "codeName": "RS",
  "description": "아일랜드",
  "code_en": "Ireland"
 },
 {
  "codeTypeCode": "country" 108,
  "codeName": "SC",
  "description": "맨섬",
  "code_en": "Isle of Man"
 },
 {
  "codeTypeCode": "country" 109,
  "codeName": "LS",
  "description": "이스라엘",
  "code_en": "Israel"
 },
 {
  "codeTypeCode": "country" 110,
  "codeName": "VC",
  "description": "이탈리아",
  "code_en": "Italy"
 },
 {
  "codeTypeCode": "country" 111,
  "codeName": "KN",
  "description": "자메이카",
  "code_en": "Jamaica"
 },
 {
  "codeTypeCode": "country" 112,
  "codeName": "SH",
  "description": "일본",
  "code_en": "Japan"
 },
 {
  "codeTypeCode": "country" 113,
  "codeName": "SO",
  "description": "저지섬",
  "code_en": "Jersey"
 },
 {
  "codeTypeCode": "country" 114,
  "codeName": "SB",
  "description": "요르단",
  "code_en": "Jordan"
 },
 {
  "codeTypeCode": "country" 115,
  "codeName": "SD",
  "description": "카자흐스탄",
  "code_en": "Kazakhstan"
 },
 {
  "codeTypeCode": "country" 116,
  "codeName": "SR",
  "description": "케냐",
  "code_en": "Kenya"
 },
 {
  "codeTypeCode": "country" 117,
  "codeName": "LK",
  "description": "키리바시",
  "code_en": "Kiribati"
 },
 {
  "codeTypeCode": "country" 118,
  "codeName": "SJ",
  "description": "조선민주주의인민공화국",
  "code_en": "Korea "
 },
 {
  "codeTypeCode": "country" 119,
  "codeName": "SE",
  "description": "대한민국",
  "code_en": "Korea "
 },
 {
  "codeTypeCode": "country" 120,
  "codeName": "CH",
  "description": "쿠웨이트",
  "code_en": "Kuwait"
 },
 {
  "codeTypeCode": "country" 121,
  "codeName": "ES",
  "description": "키르기스스탄",
  "code_en": "Kyrgyzstan"
 },
 {
  "codeTypeCode": "country" 122,
  "codeName": "SK",
  "description": "라오스",
  "code_en": "Laos"
 },
 {
  "codeTypeCode": "country" 123,
  "codeName": "SI",
  "description": "라트비아",
  "code_en": "Latvija"
 },
 {
  "codeTypeCode": "country" 124,
  "codeName": "SY",
  "description": "레바논",
  "code_en": "Lebanon"
 },
 {
  "codeTypeCode": "country" 125,
  "codeName": "SL",
  "description": "레소토",
  "code_en": "Lesotho"
 },
 {
  "codeTypeCode": "country" 126,
  "codeName": "SX",
  "description": "리비아",
  "code_en": "Libya"
 },
 {
  "codeTypeCode": "country" 127,
  "codeName": "SG",
  "description": "리히텐슈타인",
  "code_en": "Liechtenstein"
 },
 {
  "codeTypeCode": "country" 128,
  "codeName": "AE",
  "description": "리투아니아",
  "code_en": "Lithuania"
 },
 {
  "codeTypeCode": "country" 129,
  "codeName": "AW",
  "description": "룩셈부르크",
  "code_en": "Luxembourg"
 },
 {
  "codeTypeCode": "country" 130,
  "codeName": "AM",
  "description": "마카오",
  "code_en": "Macau"
 },
 {
  "codeTypeCode": "country" 131,
  "codeName": "AR",
  "description": "마다가스카르",
  "code_en": "Madagascar"
 },
 {
  "codeTypeCode": "country" 132,
  "codeName": "AS",
  "description": "말라위",
  "code_en": "Malawi"
 },
 {
  "codeTypeCode": "country" 133,
  "codeName": "IS",
  "description": "말레이시아",
  "code_en": "Malaysia"
 },
 {
  "codeTypeCode": "country" 134,
  "codeName": "HT",
  "description": "몰디브",
  "code_en": "Maldives"
 },
 {
  "codeTypeCode": "country" 135,
  "codeName": "IE",
  "description": "말리",
  "code_en": "Mali"
 },
 {
  "codeTypeCode": "country" 136,
  "codeName": "AZ",
  "description": "몰타",
  "code_en": "Malta"
 },
 {
  "codeTypeCode": "country" 137,
  "codeName": "AF",
  "description": "마셜 제도",
  "code_en": "Marshall Is."
 },
 {
  "codeTypeCode": "country" 138,
  "codeName": "AD",
  "description": "마르티니크",
  "code_en": "Martinique"
 },
 {
  "codeTypeCode": "country" 139,
  "codeName": "AL",
  "description": "모리타니",
  "code_en": "Mauritania"
 },
 {
  "codeTypeCode": "country" 140,
  "codeName": "DZ",
  "description": "모리셔스",
  "code_en": "Mauritius"
 },
 {
  "codeTypeCode": "country" 141,
  "codeName": "AO",
  "description": "마요트",
  "code_en": "Mayotte"
 },
 {
  "codeTypeCode": "country" 142,
  "codeName": "AG",
  "description": "멕시코",
  "code_en": "Mexico"
 },
 {
  "codeTypeCode": "country" 143,
  "codeName": "AI",
  "description": "미크로네시아 연방",
  "code_en": "Micronesia"
 },
 {
  "codeTypeCode": "country" 144,
  "codeName": "ER",
  "description": "몰도바",
  "code_en": "Moldova "
 },
 {
  "codeTypeCode": "country" 145,
  "codeName": "SZ",
  "description": "모나코",
  "code_en": "Monaco"
 },
 {
  "codeTypeCode": "country" 146,
  "codeName": "EE",
  "description": "몽골",
  "code_en": "Mongolia"
 },
 {
  "codeTypeCode": "country" 147,
  "codeName": "EC",
  "description": "몬테네그로",
  "code_en": "Montenegro"
 },
 {
  "codeTypeCode": "country" 148,
  "codeName": "ET",
  "description": "몬트세랫",
  "code_en": "Montserrat"
 },
 {
  "codeTypeCode": "country" 149,
  "codeName": "SV",
  "description": "모로코",
  "code_en": "Morocco"
 },
 {
  "codeTypeCode": "country" 150,
  "codeName": "GB",
  "description": "모잠비크",
  "code_en": "Mozambique"
 },
 {
  "codeTypeCode": "country" 151,
  "codeName": "VG",
  "description": "나미비아",
  "code_en": "Namibia"
 },
 {
  "codeTypeCode": "country" 152,
  "codeName": "IO",
  "description": "나우루",
  "code_en": "Nauru"
 },
 {
  "codeTypeCode": "country" 153,
  "codeName": "YE",
  "description": "네덜란드령 안틸레스",
  "code_en": "Nederlandse Antillen"
 },
 {
  "codeTypeCode": "country" 154,
  "codeName": "OM",
  "description": "네팔",
  "code_en": "Nepal"
 },
 {
  "codeTypeCode": "country" 155,
  "codeName": "AU",
  "description": "네덜란드",
  "code_en": "Netherlands"
 },
 {
  "codeTypeCode": "country" 156,
  "codeName": "AT",
  "description": "누벨칼레도니",
  "code_en": "New Caledonia"
 },
 {
  "codeTypeCode": "country" 157,
  "codeName": "HN",
  "description": "뉴질랜드",
  "code_en": "New Zealand"
 },
 {
  "codeTypeCode": "country" 158,
  "codeName": "AX",
  "description": "니카라과",
  "code_en": "Nicaragua"
 },
 {
  "codeTypeCode": "country" 159,
  "codeName": "JO",
  "description": "니제르",
  "code_en": "Niger"
 },
 {
  "codeTypeCode": "country" 160,
  "codeName": "UG",
  "description": "나이지리아",
  "code_en": "Nigeria"
 },
 {
  "codeTypeCode": "country" 161,
  "codeName": "UY",
  "description": "니우에",
  "code_en": "Niue"
 },
 {
  "codeTypeCode": "country" 162,
  "codeName": "UZ",
  "description": "노퍽 섬",
  "code_en": "Norfuk Ailen"
 },
 {
  "codeTypeCode": "country" 163,
  "codeName": "UA",
  "description": "북마케도니아",
  "code_en": "North Macedonia"
 },
 {
  "codeTypeCode": "country" 164,
  "codeName": "WF",
  "description": "북마리아나 제도",
  "code_en": "Northern Mariana Is."
 },
 {
  "codeTypeCode": "country" 165,
  "codeName": "IQ",
  "description": "노르웨이",
  "code_en": "Norway"
 },
 {
  "codeTypeCode": "country" 166,
  "codeName": "IR",
  "description": "오만",
  "code_en": "Oman"
 },
 {
  "codeTypeCode": "country" 167,
  "codeName": "IL",
  "description": "파키스탄",
  "code_en": "Pakistan"
 },
 {
  "codeTypeCode": "country" 168,
  "codeName": "EG",
  "description": "팔라우",
  "code_en": "Palau"
 },
 {
  "codeTypeCode": "country" 169,
  "codeName": "IT",
  "description": "팔레스타인",
  "code_en": "Palestine, State of"
 },
 {
  "codeTypeCode": "country" 170,
  "codeName": "IN",
  "description": "파나마",
  "code_en": "Panama"
 },
 {
  "codeTypeCode": "country" 171,
  "codeName": "codeTypeCode", "country"
  "description": "파푸아뉴기니",
  "code_en": "Papua New Guinea"
 },
 {
  "codeTypeCode": "country" 172,
  "codeName": "JP",
  "description": "파라과이",
  "code_en": "Paraguay"
 },
 {
  "codeTypeCode": "country" 173,
  "codeName": "JM",
  "description": "페루",
  "code_en": "Peru"
 },
 {
  "codeTypeCode": "country" 174,
  "codeName": "ZM",
  "description": "필리핀",
  "code_en": "Philippines"
 },
 {
  "codeTypeCode": "country" 175,
  "codeName": "JE",
  "description": "핏케언 제도",
  "code_en": "Pitcairn"
 },
 {
  "codeTypeCode": "country" 176,
  "codeName": "GQ",
  "description": "폴란드",
  "code_en": "Poland"
 },
 {
  "codeTypeCode": "country" 177,
  "codeName": "KP",
  "description": "포르투갈",
  "code_en": "Portugal"
 },
 {
  "codeTypeCode": "country" 178,
  "codeName": "GE",
  "description": "푸에르토리코",
  "code_en": "Puerto Rico"
 },
 {
  "codeTypeCode": "country" 179,
  "codeName": "CN",
  "description": "카타르",
  "code_en": "Qatar"
 },
 {
  "codeTypeCode": "country" 180,
  "codeName": "CF",
  "description": "라이베리아",
  "code_en": "Republic of Liberia"
 },
 {
  "codeTypeCode": "country" 181,
  "codeName": "GI",
  "description": "미얀마",
  "code_en": "Republic of the Union of Myanmar"
 },
 {
  "codeTypeCode": "country" 182,
  "codeName": "GI",
  "description": "레위니옹",
  "code_en": "Reunion "
 },
 {
  "codeTypeCode": "country" 183,
  "codeName": "ZW",
  "description": "루마니아",
  "code_en": "Romania"
 },
 {
  "codeTypeCode": "country" 184,
  "codeName": "TD",
  "description": "러시아",
  "code_en": "Russia"
 },
 {
  "codeTypeCode": "country" 185,
  "codeName": "CZ",
  "description": "르완다",
  "code_en": "Rwanda"
 },
 {
  "codeTypeCode": "country" 186,
  "codeName": "CL",
  "description": "세인트헬레나",
  "code_en": "Saint Helena, Ascension and Tristan da Cunha"
 },
 {
  "codeTypeCode": "country" 187,
  "codeName": "CM",
  "description": "세인트키츠 네비스",
  "code_en": "Saint Kitts and Nevis"
 },
 {
  "codeTypeCode": "country" 188,
  "codeName": "CV",
  "description": "세인트루시아",
  "code_en": "Saint Lucia"
 },
 {
  "codeTypeCode": "country" 189,
  "codeName": "KZ",
  "description": "생피에르 미클롱",
  "code_en": "Saint Pierre and Miquelon"
 },
 {
  "codeTypeCode": "country" 190,
  "codeName": "QA",
  "description": "세인트빈센트 그레나딘",
  "code_en": "Saint Vincent and the Grenadines"
 },
 {
  "codeTypeCode": "country" 191,
  "codeName": "KH",
  "description": "사모아",
  "code_en": "Samoa"
 },
 {
  "codeTypeCode": "country" 192,
  "codeName": "CA",
  "description": "산마리노",
  "code_en": "San Marino"
 },
 {
  "codeTypeCode": "country" 193,
  "codeName": "KE",
  "description": "상투메 프린시페",
  "code_en": "Sao Tome and Principe"
 },
 {
  "codeTypeCode": "country" 194,
  "codeName": "KY",
  "description": "사우디아라비아",
  "code_en": "Saudi Arabia"
 },
 {
  "codeTypeCode": "country" 195,
  "codeName": "KM",
  "description": "세네갈",
  "code_en": "Senegal"
 },
 {
  "codeTypeCode": "country" 196,
  "codeName": "CR",
  "description": "세르비아",
  "code_en": "Serbia"
 },
 {
  "codeTypeCode": "country" 197,
  "codeName": "CC",
  "description": "세이셸",
  "code_en": "Seychelles"
 },
 {
  "codeTypeCode": "country" 198,
  "codeName": "CI",
  "description": "시에라리온",
  "code_en": "Sierra Leone"
 },
 {
  "codeTypeCode": "country" 199,
  "codeName": "CO",
  "description": "싱가포르",
  "code_en": "Singapore"
 },
 {
  "codeTypeCode": "country" 200,
  "codeName": "CG",
  "description": "신트마르턴",
  "code_en": "Sint Maarten"
 },
 {
  "codeTypeCode": "country" 201,
  "codeName": "CD",
  "description": "슬로바키아",
  "code_en": "Slovakia"
 },
 {
  "codeTypeCode": "country" 202,
  "codeName": "CU",
  "description": "슬로베니아",
  "code_en": "Slovenia"
 },
 {
  "codeTypeCode": "country" 203,
  "codeName": "KW",
  "description": "솔로몬 제도",
  "code_en": "Solomon Islands"
 },
 {
  "codeTypeCode": "country" 204,
  "codeName": "CK",
  "description": "소말리아",
  "code_en": "Somalia"
 },
 {
  "codeTypeCode": "country" 205,
  "codeName": "HR",
  "description": "남아프리카 공화국",
  "code_en": "South Africa"
 },
 {
  "codeTypeCode": "country" 206,
  "codeName": "CX",
  "description": "사우스조지아 사우스샌드위치 제도",
  "code_en": "South Georgia and the South Sandwich Islands"
 },
 {
  "codeTypeCode": "country" 207,
  "codeName": "KG",
  "description": "스페인",
  "code_en": "Spain"
 },
 {
  "codeTypeCode": "country" 208,
  "codeName": "KI",
  "description": "스리랑카",
  "code_en": "Sri Lanka"
 },
 {
  "codeTypeCode": "country" 209,
  "codeName": "CY",
  "description": "수단",
  "code_en": "Sudan"
 },
 {
  "codeTypeCode": "country" 210,
  "codeName": "TW",
  "description": "수리남",
  "code_en": "Suriname"
 },
 {
  "codeTypeCode": "country" 211,
  "codeName": "TJ",
  "description": "스발바르 얀마옌",
  "code_en": "Svalbard and Jan Mayen"
 },
 {
  "codeTypeCode": "country" 212,
  "codeName": "TZ",
  "description": "스웨덴",
  "code_en": "Sweden"
 },
 {
  "codeTypeCode": "country" 213,
  "codeName": "TH",
  "description": "스위스",
  "code_en": "Switzerland"
 },
 {
  "codeTypeCode": "country" 214,
  "codeName": "TC",
  "description": "시리아",
  "code_en": "Syrian Arab Republic"
 },
 {
  "codeTypeCode": "country" 215,
  "codeName": "TR",
  "description": "타이완",
  "code_en": "Taiwan"
 },
 {
  "codeTypeCode": "country" 216,
  "codeName": "TG",
  "description": "타지키스탄",
  "code_en": "Tajikistan"
 },
 {
  "codeTypeCode": "country" 217,
  "codeName": "TK",
  "description": "탄자니아",
  "code_en": "Tanzania, the United Republic of"
 },
 {
  "codeTypeCode": "country" 218,
  "codeName": "TO",
  "description": "태국",
  "code_en": "Thailand"
 },
 {
  "codeTypeCode": "country" 219,
  "codeName": "TM",
  "description": "토고",
  "code_en": "Togo"
 },
 {
  "codeTypeCode": "country" 220,
  "codeName": "TV",
  "description": "토켈라우",
  "code_en": "Tokelau"
 },
 {
  "codeTypeCode": "country" 221,
  "codeName": "TN",
  "description": "통가",
  "code_en": "Tonga"
 },
 {
  "codeTypeCode": "country" 222,
  "codeName": "TT",
  "description": "트리니다드 토바고",
  "code_en": "TrincodeTypeCodead "country" and Tobago"
 },
 {
  "codeTypeCode": "country" 223,
  "codeName": "PA",
  "description": "튀니지",
  "code_en": "Tunisia"
 },
 {
  "codeTypeCode": "country" 224,
  "codeName": "PY",
  "description": "터키",
  "code_en": "Turkey"
 },
 {
  "codeTypeCode": "country" 225,
  "codeName": "PK",
  "description": "투르크메니스탄",
  "code_en": "Turkmenistan"
 },
 {
  "codeTypeCode": "country" 226,
  "codeName": "PG",
  "description": "터크스 케이커스 제도",
  "code_en": "Turks and Caicos Islands"
 },
 {
  "codeTypeCode": "country" 227,
  "codeName": "PW",
  "description": "투발루",
  "code_en": "Tuvalu"
 },
 {
  "codeTypeCode": "country" 228,
  "codeName": "PS",
  "description": "우간다",
  "code_en": "Uganda"
 },
 {
  "codeTypeCode": "country" 229,
  "codeName": "FO",
  "description": "우크라이나",
  "code_en": "Ukraine"
 },
 {
  "codeTypeCode": "country" 230,
  "codeName": "PE",
  "description": "아랍에미리트",
  "code_en": "United Arab Emirates"
 },
 {
  "codeTypeCode": "country" 231,
  "codeName": "PT",
  "description": "영국",
  "code_en": "United Kingdom of Great Britain and Northern Ireland"
 },
 {
  "codeTypeCode": "country" 232,
  "codeName": "FK",
  "description": "미국령 군소 제도",
  "code_en": "United States Minor Outlying Islands"
 },
 {
  "codeTypeCode": "country" 233,
  "codeName": "PL",
  "description": "미국",
  "code_en": "United States of America"
 },
 {
  "codeTypeCode": "country" 234,
  "codeName": "PR",
  "description": "미국령 버진아일랜드",
  "code_en": "United States Virgin Islands"
 },
 {
  "codeTypeCode": "country" 235,
  "codeName": "FR",
  "description": "우르과이",
  "code_en": "Uruguay"
 },
 {
  "codeTypeCode": "country" 236,
  "codeName": "GF",
  "description": "우즈베키스탄",
  "code_en": "Uzbekistan"
 },
 {
  "codeTypeCode": "country" 237,
  "codeName": "TF",
  "description": "바누아투",
  "code_en": "Vanuatu"
 },
 {
  "codeTypeCode": "country" 238,
  "codeName": "PF",
  "description": "바티칸 시국",
  "code_en": "Vatican City"
 },
 {
  "codeTypeCode": "country" 239,
  "codeName": "FJ",
  "description": "베네수엘라",
  "code_en": "Venezuela "
 },
 {
  "codeTypeCode": "country" 240,
  "codeName": "FI",
  "description": "베트남",
  "code_en": "Viet Nam"
 },
 {
  "codeTypeCode": "country" 241,
  "codeName": "PH",
  "description": "왈리스 퓌튀나",
  "code_en": "Wallis and Futuna"
 },
 {
  "codeTypeCode": "country" 242,
  "codeName": "PN",
  "description": "서사하라",
  "code_en": "Western Sahara"
 },
 {
  "codeTypeCode": "country" 243,
  "codeName": "HM",
  "description": "예멘",
  "code_en": "Yemen"
 },
 {
  "codeTypeCode": "country" 244,
  "codeName": "HU",
  "description": "잠비아",
  "code_en": "Zambia"
 },
 {
  "codeTypeCode": "country" 245,
  "codeName": "HK",
  "description": "짐바브웨",
  "code_en": "Zimbabwe"
 }
],
"언어코드":[
 {
  "codeTypeCode": "country" 1,
  "codeName": "AF",
  "description": "아프리칸스어 ",
  "code_en": " Afrikaans"
 },
 {
  "codeTypeCode": "country" 2,
  "codeName": "ALS",
  "description": "알자스어",
  "code_en": " Alsatian"
 },
 {
  "codeTypeCode": "country" 3,
  "codeName": "AR",
  "description": "아랍어 ",
  "code_en": " Arabic"
 },
 {
  "codeTypeCode": "country" 4,
  "codeName": "AZ",
  "description": "아제르바이잔어 ",
  "code_en": " Azerbaijani"
 },
 {
  "codeTypeCode": "country" 5,
  "codeName": "BA",
  "description": "바슈키르어 ",
  "code_en": " Bashkir"
 },
 {
  "codeTypeCode": "country" 6,
  "codeName": "BE",
  "description": "벨라루스어 ",
  "code_en": " Belarusian"
 },
 {
  "codeTypeCode": "country" 7,
  "codeName": "BG",
  "description": "불가리아어 ",
  "code_en": " Bulgarian"
 },
 {
  "codeTypeCode": "country" 8,
  "codeName": "BH",
  "description": "비하리어",
  "code_en": " Bihari"
 },
 {
  "codeTypeCode": "country" 9,
  "codeName": "BI",
  "description": "비슐라마",
  "code_en": " Bislama "
 },
 {
  "codeTypeCode": "country" 10,
  "codeName": "BM",
  "description": "밤바라어",
  "code_en": " Bambara "
 },
 {
  "codeTypeCode": "country" 11,
  "codeName": "BN",
  "description": "벵골어",
  "code_en": " Bengali "
 },
 {
  "codeTypeCode": "country" 12,
  "codeName": "BR",
  "description": "브레통어 ",
  "code_en": " Breton "
 },
 {
  "codeTypeCode": "country" 13,
  "codeName": "BS",
  "description": "보스니아어 ",
  "code_en": " Bosnian "
 },
 {
  "codeTypeCode": "country" 14,
  "codeName": "CA",
  "description": "카탈루냐어 ",
  "code_en": " Catalan "
 },
 {
  "codeTypeCode": "country" 15,
  "codeName": "CE",
  "description": "체첸어 ",
  "code_en": " Chechen "
 },
 {
  "codeTypeCode": "country" 16,
  "codeName": "CEB",
  "description": "세부어 ",
  "code_en": " Cebuano "
 },
 {
  "codeTypeCode": "country" 17,
  "codeName": "CH",
  "description": "차모로어",
  "code_en": " Chamorro "
 },
 {
  "codeTypeCode": "country" 18,
  "codeName": "CO",
  "description": "코르시카어",
  "code_en": " Corsican "
 },
 {
  "codeTypeCode": "country" 19,
  "codeName": "CR",
  "description": "크리어",
  "code_en": " Cree "
 },
 {
  "codeTypeCode": "country" 20,
  "codeName": "CS",
  "description": "체코어 ",
  "code_en": " Czech "
 },
 {
  "codeTypeCode": "country" 21,
  "codeName": "DA",
  "description": "덴마크어 ",
  "code_en": " Danish "
 },
 {
  "codeTypeCode": "country" 22,
  "codeName": "DE",
  "description": "독일어 ",
  "code_en": " German "
 },
 {
  "codeTypeCode": "country" 23,
  "codeName": "DV",
  "description": "디베히어",
  "code_en": " Divehi "
 },
 {
  "codeTypeCode": "country" 24,
  "codeName": "EL",
  "description": "현대 그리스어 ",
  "code_en": " Greek, Modern "
 },
 {
  "codeTypeCode": "country" 25,
  "codeName": "EN",
  "description": "영어 ",
  "code_en": " English "
 },
 {
  "codeTypeCode": "country" 26,
  "codeName": "EO",
  "description": "에스페란토 ",
  "code_en": " Esperanto "
 },
 {
  "codeTypeCode": "country" 27,
  "codeName": "ES",
  "description": "에스파냐어 ",
  "code_en": " Spanish "
 },
 {
  "codeTypeCode": "country" 28,
  "codeName": "ET",
  "description": "에스토니아어 ",
  "code_en": " Estonian "
 },
 {
  "codeTypeCode": "country" 29,
  "codeName": "EU",
  "description": "바스크어 ",
  "code_en": " Basque "
 },
 {
  "codeTypeCode": "country" 30,
  "codeName": "FA",
  "description": "페르시아어 ",
  "code_en": " Persian "
 },
 {
  "codeTypeCode": "country" 31,
  "codeName": "FF",
  "description": "풀라어",
  "code_en": " Fulah "
 },
 {
  "codeTypeCode": "country" 32,
  "codeName": "FI",
  "description": "핀란드어 ",
  "code_en": " Finnish "
 },
 {
  "codeTypeCode": "country" 33,
  "codeName": "FJ",
  "description": "피지어",
  "code_en": " Fijian "
 },
 {
  "codeTypeCode": "country" 34,
  "codeName": "FO",
  "description": "페로어 ",
  "code_en": " Faroese "
 },
 {
  "codeTypeCode": "country" 35,
  "codeName": "FR",
  "description": "프랑스어 ",
  "code_en": " French "
 },
 {
  "codeTypeCode": "country" 36,
  "codeName": "FY",
  "description": "프리지아어",
  "code_en": " Frisian "
 },
 {
  "codeTypeCode": "country" 37,
  "codeName": "GA",
  "description": "아일랜드어",
  "code_en": " Irish "
 },
 {
  "codeTypeCode": "country" 38,
  "codeName": "GD",
  "description": "게일어 ",
  "code_en": " Gaelic Scottish Gaelic "
 },
 {
  "codeTypeCode": "country" 39,
  "codeName": "GL",
  "description": "갈리시아어",
  "code_en": " Gallegan "
 },
 {
  "codeTypeCode": "country" 40,
  "codeName": "GN",
  "description": "과라니어",
  "code_en": " Guarani "
 },
 {
  "codeTypeCode": "country" 41,
  "codeName": "GRC",
  "description": "고대 그리스어 ",
  "code_en": " Greek, Ancient "
 },
 {
  "codeTypeCode": "country" 42,
  "codeName": "GU",
  "description": "구자라티어",
  "code_en": " Gujarati "
 },
 {
  "codeTypeCode": "country" 43,
  "codeName": "GV",
  "description": "맨어 ",
  "code_en": " Manx "
 },
 {
  "codeTypeCode": "country" 44,
  "codeName": "HA",
  "description": "하우사어",
  "code_en": " Hausa "
 },
 {
  "codeTypeCode": "country" 45,
  "codeName": "HE",
  "description": "히브리어 ",
  "code_en": " Hebrew "
 },
 {
  "codeTypeCode": "country" 46,
  "codeName": "HI",
  "description": "힌디어 ",
  "code_en": " Hindi "
 },
 {
  "codeTypeCode": "country" 47,
  "codeName": "HR",
  "description": "크로아티아어 ",
  "code_en": " Croatian "
 },
 {
  "codeTypeCode": "country" 48,
  "codeName": "HSB",
  "description": "상소르브어 ",
  "code_en": " Upper Sorbian "
 },
 {
  "codeTypeCode": "country" 49,
  "codeName": "HT",
  "description": "아이티크리올어",
  "code_en": " Haitian Haitian Creole "
 },
 {
  "codeTypeCode": "country" 50,
  "codeName": "HU",
  "description": "헝가리어 ",
  "code_en": " Hungarian "
 },
 {
  "codeTypeCode": "country" 51,
  "codeName": "HY",
  "description": "아르메니아어",
  "code_en": " Armenian "
 },
 {
  "codeTypeCode": "country" 52,
  "codeName": "HZ",
  "description": "헤레로어 ",
  "code_en": " Herero "
 },
 {
  "codeTypeCode": "country" 53,
  "codeName": "IA",
  "description": "인터링구아 ",
  "code_en": " Interlingua International Auxiliary "
 },
 {
  "codeTypeCode": "country" 54,
  "codeName": "codeTypeCode", "country"
  "description": "인도네시아어 ",
  "code_en": " Indonesian "
 },
 {
  "codeTypeCode": "country" 55,
  "codeName": "II",
  "description": "이어 ",
  "code_en": " Sichuan Yi "
 },
 {
  "codeTypeCode": "country" 56,
  "codeName": "IK",
  "description": "이누피아크어 ",
  "code_en": " Inupiaq "
 },
 {
  "codeTypeCode": "country" 57,
  "codeName": "IO",
  "description": "이도 ",
  "code_en": " codeTypeCodeo  "country""
 },
 {
  "codeTypeCode": "country" 58,
  "codeName": "IS",
  "description": "아이슬란드어 ",
  "code_en": " Icelandic "
 },
 {
  "codeTypeCode": "country" 59,
  "codeName": "IT",
  "description": "이탈리아어 ",
  "code_en": " Italian "
 },
 {
  "codeTypeCode": "country" 60,
  "codeName": "IU",
  "description": "이누이트어",
  "code_en": " Inuktitut "
 },
 {
  "codeTypeCode": "country" 61,
  "codeName": "JA",
  "description": "일본어 ",
  "code_en": " Japanese "
 },
 {
  "codeTypeCode": "country" 62,
  "codeName": "JV",
  "description": "자바어",
  "code_en": " Javanese "
 },
 {
  "codeTypeCode": "country" 63,
  "codeName": "KA",
  "description": "그루지야어 ",
  "code_en": " Georgian "
 },
 {
  "codeTypeCode": "country" 64,
  "codeName": "KG",
  "description": "콩고어",
  "code_en": " Kongo "
 },
 {
  "codeTypeCode": "country" 65,
  "codeName": "KI",
  "description": "키쿠유어",
  "code_en": " Kikuyu "
 },
 {
  "codeTypeCode": "country" 66,
  "codeName": "KJ",
  "description": "콰냐마어",
  "code_en": " Kuanyama Kwanyama "
 },
 {
  "codeTypeCode": "country" 67,
  "codeName": "KK",
  "description": "카자흐어 ",
  "code_en": " Kazakh "
 },
 {
  "codeTypeCode": "country" 68,
  "codeName": "KL",
  "description": "그린란드어 ",
  "code_en": " Kalaallisut "
 },
 {
  "codeTypeCode": "country" 69,
  "codeName": "KM",
  "description": "크메르어 ",
  "code_en": " Khmer "
 },
 {
  "codeTypeCode": "country" 70,
  "codeName": "KN",
  "description": "칸나다어",
  "code_en": " Kannada "
 },
 {
  "codeTypeCode": "country" 71,
  "codeName": "KO",
  "description": "한국어 ",
  "code_en": " Korean "
 },
 {
  "codeTypeCode": "country" 72,
  "codeName": "KR",
  "description": "카누리어",
  "code_en": " Kanuri "
 },
 {
  "codeTypeCode": "country" 73,
  "codeName": "KS",
  "description": "카슈미르어 ",
  "code_en": " Kashmiri "
 },
 {
  "codeTypeCode": "country" 74,
  "codeName": "KU",
  "description": "쿠르드어 ",
  "code_en": " Kurdish "
 },
 {
  "codeTypeCode": "country" 75,
  "codeName": "KV",
  "description": "페름어 ",
  "code_en": " Komi "
 },
 {
  "codeTypeCode": "country" 76,
  "codeName": "KY",
  "description": "키르기스어",
  "code_en": " Kirghiz "
 },
 {
  "codeTypeCode": "country" 77,
  "codeName": "LA",
  "description": "라틴어 ",
  "code_en": " Latin "
 },
 {
  "codeTypeCode": "country" 78,
  "codeName": "LB",
  "description": "룩셈부르크어 ",
  "code_en": " Luxembourgish "
 },
 {
  "codeTypeCode": "country" 79,
  "codeName": "LG",
  "description": "간다어",
  "code_en": " Ganda "
 },
 {
  "codeTypeCode": "country" 80,
  "codeName": "LI",
  "description": "림뷔르흐어",
  "code_en": " Limburgan Limburger; Limburgish "
 },
 {
  "codeTypeCode": "country" 81,
  "codeName": "LN",
  "description": "링갈라어",
  "code_en": " Lingala "
 },
 {
  "codeTypeCode": "country" 82,
  "codeName": "LO",
  "description": "라오어 ",
  "code_en": " Lao "
 },
 {
  "codeTypeCode": "country" 83,
  "codeName": "LT",
  "description": "리투아니아어 ",
  "code_en": " Lithuanian "
 },
 {
  "codeTypeCode": "country" 84,
  "codeName": "LU",
  "description": "루바-카탕가어",
  "code_en": " Luba-Katanga "
 },
 {
  "codeTypeCode": "country" 85,
  "codeName": "LV",
  "description": "라트비아어 ",
  "code_en": " Latvian "
 },
 {
  "codeTypeCode": "country" 86,
  "codeName": "MG",
  "description": "마다가스카르어",
  "code_en": " Malagasy "
 },
 {
  "codeTypeCode": "country" 87,
  "codeName": "MAK",
  "description": "마카사르어",
  "code_en": " Makasar "
 },
 {
  "codeTypeCode": "country" 88,
  "codeName": "MI",
  "description": "마오리어",
  "code_en": " Maori "
 },
 {
  "codeTypeCode": "country" 89,
  "codeName": "MK",
  "description": "마케도니아어 ",
  "code_en": " Macedonian "
 },
 {
  "codeTypeCode": "country" 90,
  "codeName": "ML",
  "description": "말라얄람어",
  "code_en": " Malayalam "
 },
 {
  "codeTypeCode": "country" 91,
  "codeName": "MS",
  "description": "말레이어 ",
  "code_en": " Malay "
 },
 {
  "codeTypeCode": "country" 92,
  "codeName": "MN",
  "description": "몽골어 ",
  "code_en": " Mongolian "
 },
 {
  "codeTypeCode": "country" 93,
  "codeName": "MO",
  "description": "몰도바어 ",
  "code_en": " Moldavian "
 },
 {
  "codeTypeCode": "country" 94,
  "codeName": "MR",
  "description": "마라타어",
  "code_en": " Marathi "
 },
 {
  "codeTypeCode": "country" 95,
  "codeName": "MT",
  "description": "몰타어 ",
  "code_en": " Maltese "
 },
 {
  "codeTypeCode": "country" 96,
  "codeName": "NA",
  "description": "나우루어 ",
  "code_en": " Nauru "
 },
 {
  "codeTypeCode": "country" 97,
  "codeName": "ND",
  "description": "북느데벨 ",
  "code_en": " Ndebele,  North; North Ndebele  "
 },
 {
  "codeTypeCode": "country" 98,
  "codeName": "NDS",
  "description": "저지 색슨어",
  "code_en": " Low Saxon language"
 },
 {
  "codeTypeCode": "country" 99,
  "codeName": "NE",
  "description": "네팔어 ",
  "code_en": " Nepali "
 },
 {
  "codeTypeCode": "country" 100,
  "codeName": "NG",
  "description": "느동가 ",
  "code_en": " Ndonga "
 },
 {
  "codeTypeCode": "country" 101,
  "codeName": "NL",
  "description": "네덜란드어 ",
  "code_en": " Dutch,  Flemish "
 },
 {
  "codeTypeCode": "country" 102,
  "codeName": "NO",
  "description": "노르웨이어 ",
  "code_en": " Norwegian "
 },
 {
  "codeTypeCode": "country" 103,
  "codeName": "NR",
  "description": "남느드벨 ",
  "code_en": " Ndebele,  South; South Ndebele "
 },
 {
  "codeTypeCode": "country" 104,
  "codeName": "NV",
  "description": "나바호어",
  "code_en": " Navajo; Navaho "
 },
 {
  "codeTypeCode": "country" 105,
  "codeName": "OC",
  "description": "프로방스어",
  "code_en": " Occitan "
 },
 {
  "codeTypeCode": "country" 106,
  "codeName": "OJ",
  "description": "오지브와어",
  "code_en": " Ojibwa "
 },
 {
  "codeTypeCode": "country" 107,
  "codeName": "OM",
  "description": "갈라어 ",
  "code_en": " Oromo "
 },
 {
  "codeTypeCode": "country" 108,
  "codeName": "OR",
  "description": "오리야어",
  "code_en": " Oriya "
 },
 {
  "codeTypeCode": "country" 109,
  "codeName": "OS",
  "description": "오세트어",
  "code_en": " Ossetian; Ossetic "
 },
 {
  "codeTypeCode": "country" 110,
  "codeName": "PA",
  "description": "펀자브어 ",
  "code_en": " Panjabi; Punjabi "
 },
 {
  "codeTypeCode": "country" 111,
  "codeName": "PI",
  "description": "팔리어",
  "code_en": " Pali "
 },
 {
  "codeTypeCode": "country" 112,
  "codeName": "PL",
  "description": "폴란드어 ",
  "code_en": " Polish "
 },
 {
  "codeTypeCode": "country" 113,
  "codeName": "PS",
  "description": "파슈툰어 ",
  "code_en": " Pushto "
 },
 {
  "codeTypeCode": "country" 114,
  "codeName": "PRS",
  "description": "다리어 ",
  "code_en": " Dari "
 },
 {
  "codeTypeCode": "country" 115,
  "codeName": "PT",
  "description": "포르투갈어 ",
  "code_en": " Portuguese "
 },
 {
  "codeTypeCode": "country" 116,
  "codeName": "QU",
  "description": "케추아어",
  "code_en": " Quechua "
 },
 {
  "codeTypeCode": "country" 117,
  "codeName": "RM",
  "description": "레토-로만어",
  "code_en": " Raeto-Romance "
 },
 {
  "codeTypeCode": "country" 118,
  "codeName": "RO",
  "description": "루마니아어 ",
  "code_en": " Romanian "
 },
 {
  "codeTypeCode": "country" 119,
  "codeName": "RN",
  "description": "룬디어",
  "code_en": " Rundi "
 },
 {
  "codeTypeCode": "country" 120,
  "codeName": "RU",
  "description": "러시아어 ",
  "code_en": " Russian "
 },
 {
  "codeTypeCode": "country" 121,
  "codeName": "RW",
  "description": "르완다어",
  "code_en": " Kinyarwanda "
 },
 {
  "codeTypeCode": "country" 122,
  "codeName": "SA",
  "description": "산스크리트",
  "code_en": " Sanskrit "
 },
 {
  "codeTypeCode": "country" 123,
  "codeName": "SC",
  "description": "사르데냐어",
  "code_en": " Sardinian "
 },
 {
  "codeTypeCode": "country" 124,
  "codeName": "SCN",
  "description": "시칠리아어",
  "code_en": " Sicilian "
 },
 {
  "codeTypeCode": "country" 125,
  "codeName": "SD",
  "description": "신드어 ",
  "code_en": " Sindhi "
 },
 {
  "codeTypeCode": "country" 126,
  "codeName": "SE",
  "description": "북사미어 ",
  "code_en": " Northern Sami "
 },
 {
  "codeTypeCode": "country" 127,
  "codeName": "SG",
  "description": "상고어 ",
  "code_en": " Sango "
 },
 {
  "codeTypeCode": "country" 128,
  "codeName": "SI",
  "description": "싱할라어  ",
  "code_en": " Sinhalese "
 },
 {
  "codeTypeCode": "country" 129,
  "codeName": "SK",
  "description": "슬로바키아어 ",
  "code_en": " Slovak "
 },
 {
  "codeTypeCode": "country" 130,
  "codeName": "SIMPLE",
  "code_en": " Simple English "
 },
 {
  "codeTypeCode": "country" 131,
  "codeName": "SL",
  "description": "슬로베니아어 ",
  "code_en": " Slovenian "
 },
 {
  "codeTypeCode": "country" 132,
  "codeName": "SM",
  "description": "사모아어",
  "code_en": " Samoan "
 },
 {
  "codeTypeCode": "country" 133,
  "codeName": "SN",
  "description": "쇼나어",
  "code_en": " Shona "
 },
 {
  "codeTypeCode": "country" 134,
  "codeName": "SO",
  "description": "소말리어 카테고리 소말리어",
  "code_en": " Somali "
 },
 {
  "codeTypeCode": "country" 135,
  "codeName": "SQ",
  "description": "알바니아어 ",
  "code_en": " Albanian "
 },
 {
  "codeTypeCode": "country" 136,
  "codeName": "SR",
  "description": "세르비아어 ",
  "code_en": " Serbian "
 },
 {
  "codeTypeCode": "country" 137,
  "codeName": "SS",
  "description": "스와티어",
  "code_en": " Swati "
 },
 {
  "codeTypeCode": "country" 138,
  "codeName": "ST",
  "description": "남소토어",
  "code_en": " Sotho,  Southern "
 },
 {
  "codeTypeCode": "country" 139,
  "codeName": "SU",
  "description": "순다어",
  "code_en": " Sundanese "
 },
 {
  "codeTypeCode": "country" 140,
  "codeName": "SV",
  "description": "스웨덴어 ",
  "code_en": " Swedish "
 },
 {
  "codeTypeCode": "country" 141,
  "codeName": "SW",
  "description": "스와힐리어 ",
  "code_en": " Swahili "
 },
 {
  "codeTypeCode": "country" 142,
  "codeName": "TA",
  "description": "타밀어 ",
  "code_en": " Tamil "
 },
 {
  "codeTypeCode": "country" 143,
  "codeName": "TE",
  "description": "텔루구어 ",
  "code_en": " Telugu "
 },
 {
  "codeTypeCode": "country" 144,
  "codeName": "TG",
  "description": "타지크어 ",
  "code_en": " Tajik "
 },
 {
  "codeTypeCode": "country" 145,
  "codeName": "TH",
  "description": "타이어  ",
  "code_en": " Thai "
 },
 {
  "codeTypeCode": "country" 146,
  "codeName": "TI",
  "description": "티그리냐어",
  "code_en": " Tigrinya  "
 },
 {
  "codeTypeCode": "country" 147,
  "codeName": "TK",
  "description": "투르크멘어 ",
  "code_en": " Turkmen "
 },
 {
  "codeTypeCode": "country" 148,
  "codeName": "TL",
  "description": "타갈로그",
  "code_en": " Tagalog "
 },
 {
  "codeTypeCode": "country" 149,
  "codeName": "TN",
  "description": "츠와나어 ",
  "code_en": " Tswana "
 },
 {
  "codeTypeCode": "country" 150,
  "codeName": "TO",
  "description": "통가어",
  "code_en": " Tonga,  Tonga Islands "
 },
 {
  "codeTypeCode": "country" 151,
  "codeName": "TR",
  "description": "터키어",
  "code_en": " Turkish  "
 },
 {
  "codeTypeCode": "country" 152,
  "codeName": "TS",
  "description": "총가어",
  "code_en": " Tsonga "
 },
 {
  "codeTypeCode": "country" 153,
  "codeName": "TT",
  "description": "타타르어 ",
  "code_en": " Tatar "
 },
 {
  "codeTypeCode": "country" 154,
  "codeName": "TW",
  "description": "트위어",
  "code_en": " Twi "
 },
 {
  "codeTypeCode": "country" 155,
  "codeName": "TY",
  "description": "타이티어",
  "code_en": " Tahitian "
 },
 {
  "codeTypeCode": "country" 156,
  "codeName": "UG",
  "description": "위구르어 ",
  "code_en": " Uighur "
 },
 {
  "codeTypeCode": "country" 157,
  "codeName": "UK",
  "description": "우크라이나어 ",
  "code_en": " Ukrainian  "
 },
 {
  "codeTypeCode": "country" 158,
  "codeName": "UR",
  "description": "우르두어 ",
  "code_en": " Urdu  "
 },
 {
  "codeTypeCode": "country" 159,
  "codeName": "UZ",
  "description": "우즈베크어 ",
  "code_en": " Uzbek "
 },
 {
  "codeTypeCode": "country" 160,
  "codeName": "VE",
  "description": "벤다어",
  "code_en": " Venda "
 },
 {
  "codeTypeCode": "country" 161,
  "codeName": "VI",
  "description": "베트남어 ",
  "code_en": " Vietnamese  "
 },
 {
  "codeTypeCode": "country" 162,
  "codeName": "VO",
  "description": "볼라퓌크",
  "code_en": " Volapük "
 },
 {
  "codeTypeCode": "country" 163,
  "codeName": "WA",
  "description": "왈론어",
  "code_en": " Walloon "
 },
 {
  "codeTypeCode": "country" 164,
  "codeName": "WO",
  "description": "월로프어",
  "code_en": " Wolof "
 },
 {
  "codeTypeCode": "country" 165,
  "codeName": "XH",
  "description": "코사어",
  "code_en": " Xhosa "
 },
 {
  "codeTypeCode": "country" 166,
  "codeName": "YI",
  "description": "이디시어 ",
  "code_en": " YcodeTypeCodedi "country"sh "
 },
 {
  "codeTypeCode": "country" 167,
  "codeName": "YO",
  "description": "요루바어",
  "code_en": " Yoruba "
 },
 {
  "codeTypeCode": "country" 168,
  "codeName": "ZH",
  "description": "중국어 ",
  "code_en": " Chinese "
 },
 {
  "codeTypeCode": "country" 169,
  "codeName": "ZH-MIN-NAN",
  "description": "중국 민난어 ",
  "code_en": " Chinese "
 },
 {
  "codeTypeCode": "country" 170
 },
 {
  "codeTypeCode": "country" 171
 },
 {
  "codeTypeCode": "country" 172
 },
 {
  "codeTypeCode": "country" 173
 },
 {
  "codeTypeCode": "country" 174
 },
 {
  "codeTypeCode": "country" 175
 },
 {
  "codeTypeCode": "country" 176
 },
 {
  "codeTypeCode": "country" 177
 },
 {
  "codeTypeCode": "country" 178
 },
 {
  "codeTypeCode": "country" 179
 },
 {
  "codeTypeCode": "country" 180
 },
 {
  "codeTypeCode": "country" 181
 },
 {
  "codeTypeCode": "country" 182
 },
 {
  "codeTypeCode": "country" 183
 },
 {
  "codeTypeCode": "country" 184
 },
 {
  "codeTypeCode": "country" 185
 },
 {
  "codeTypeCode": "country" 186
 },
 {
  "codeTypeCode": "country" 187
 },
 {
  "codeTypeCode": "country" 188
 },
 {
  "codeTypeCode": "country" 189
 },
 {
  "codeTypeCode": "country" 190
 },
 {
  "codeTypeCode": "country" 191
 },
 {
  "codeTypeCode": "country" 192
 },
 {
  "codeTypeCode": "country" 193
 },
 {
  "codeTypeCode": "country" 194
 },
 {
  "codeTypeCode": "country" 195
 },
 {
  "codeTypeCode": "country" 196
 },
 {
  "codeTypeCode": "country" 197
 },
 {
  "codeTypeCode": "country" 198
 },
 {
  "codeTypeCode": "country" 199
 },
 {
  "codeTypeCode": "country" 200
 },
 {
  "codeTypeCode": "country" 201
 },
 {
  "codeTypeCode": "country" 202
 },
 {
  "codeTypeCode": "country" 203
 },
 {
  "codeTypeCode": "country" 204
 },
 {
  "codeTypeCode": "country" 205
 },
 {
  "codeTypeCode": "country" 206
 },
 {
  "codeTypeCode": "country" 207
 },
 {
  "codeTypeCode": "country" 208
 },
 {
  "codeTypeCode": "country" 209
 },
 {
  "codeTypeCode": "country" 210
 },
 {
  "codeTypeCode": "country" 211
 },
 {
  "codeTypeCode": "country" 212
 },
 {
  "codeTypeCode": "country" 213
 },
 {
  "codeTypeCode": "country" 214
 },
 {
  "codeTypeCode": "country" 215
 },
 {
  "codeTypeCode": "country" 216
 },
 {
  "codeTypeCode": "country" 217
 },
 {
  "codeTypeCode": "country" 218
 },
 {
  "codeTypeCode": "country" 219
 },
 {
  "codeTypeCode": "country" 220
 },
 {
  "codeTypeCode": "country" 221
 },
 {
  "codeTypeCode": "country" 222
 },
 {
  "codeTypeCode": "country" 223
 },
 {
  "codeTypeCode": "country" 224
 },
 {
  "codeTypeCode": "country" 225
 },
 {
  "codeTypeCode": "country" 226
 },
 {
  "codeTypeCode": "country" 227
 },
 {
  "codeTypeCode": "country" 228
 },
 {
  "codeTypeCode": "country" 229
 },
 {
  "codeTypeCode": "country" 230
 },
 {
  "codeTypeCode": "country" 231
 },
 {
  "codeTypeCode": "country" 232
 },
 {
  "codeTypeCode": "country" 233
 },
 {
  "codeTypeCode": "country" 234
 },
 {
  "codeTypeCode": "country" 235
 },
 {
  "codeTypeCode": "country" 236
 },
 {
  "codeTypeCode": "country" 237
 },
 {
  "codeTypeCode": "country" 238
 },
 {
  "codeTypeCode": "country" 239
 },
 {
  "codeTypeCode": "country" 240
 },
 {
  "codeTypeCode": "country" 241
 },
 {
  "codeTypeCode": "country" 242
 },
 {
  "codeTypeCode": "country" 243
 },
 {
  "codeTypeCode": "country" 244
 },
 {
  "codeTypeCode": "country" 245
 }
]
}'''

new_str = re.sub(r"[0-9]", "", string)
print(new_str)