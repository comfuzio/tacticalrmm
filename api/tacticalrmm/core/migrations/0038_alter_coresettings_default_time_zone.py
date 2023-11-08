# Generated by Django 4.2.7 on 2023-11-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0037_coresettings_open_ai_model_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coresettings",
            name="default_time_zone",
            field=models.CharField(
                choices=[
                    ("Africa/Maputo", "Africa/Maputo"),
                    ("America/Grenada", "America/Grenada"),
                    ("Africa/Timbuktu", "Africa/Timbuktu"),
                    ("Australia/Darwin", "Australia/Darwin"),
                    ("Singapore", "Singapore"),
                    ("America/Guayaquil", "America/Guayaquil"),
                    ("America/Los_Angeles", "America/Los_Angeles"),
                    ("UCT", "UCT"),
                    ("Etc/GMT-5", "Etc/GMT-5"),
                    ("Europe/Bratislava", "Europe/Bratislava"),
                    ("Europe/Warsaw", "Europe/Warsaw"),
                    ("America/Argentina/Mendoza", "America/Argentina/Mendoza"),
                    ("Pacific/Majuro", "Pacific/Majuro"),
                    ("America/St_Thomas", "America/St_Thomas"),
                    ("Asia/Aden", "Asia/Aden"),
                    ("Brazil/DeNoronha", "Brazil/DeNoronha"),
                    ("America/Edmonton", "America/Edmonton"),
                    ("Pacific/Rarotonga", "Pacific/Rarotonga"),
                    ("Etc/Greenwich", "Etc/Greenwich"),
                    ("America/Cuiaba", "America/Cuiaba"),
                    ("Pacific/Chuuk", "Pacific/Chuuk"),
                    ("W-SU", "W-SU"),
                    ("Antarctica/DumontDUrville", "Antarctica/DumontDUrville"),
                    ("Africa/Ndjamena", "Africa/Ndjamena"),
                    ("Israel", "Israel"),
                    ("Asia/Almaty", "Asia/Almaty"),
                    ("America/Lima", "America/Lima"),
                    ("Atlantic/Madeira", "Atlantic/Madeira"),
                    ("America/Argentina/Salta", "America/Argentina/Salta"),
                    ("Asia/Calcutta", "Asia/Calcutta"),
                    ("Africa/Nouakchott", "Africa/Nouakchott"),
                    ("America/Halifax", "America/Halifax"),
                    ("Europe/Volgograd", "Europe/Volgograd"),
                    ("Asia/Jakarta", "Asia/Jakarta"),
                    ("America/Bahia_Banderas", "America/Bahia_Banderas"),
                    ("Atlantic/Faroe", "Atlantic/Faroe"),
                    ("Africa/Banjul", "Africa/Banjul"),
                    ("Asia/Urumqi", "Asia/Urumqi"),
                    ("Asia/Sakhalin", "Asia/Sakhalin"),
                    ("Pacific/Funafuti", "Pacific/Funafuti"),
                    ("Pacific/Marquesas", "Pacific/Marquesas"),
                    ("Pacific/Easter", "Pacific/Easter"),
                    ("Africa/Brazzaville", "Africa/Brazzaville"),
                    ("Asia/Katmandu", "Asia/Katmandu"),
                    ("Asia/Famagusta", "Asia/Famagusta"),
                    ("America/Marigot", "America/Marigot"),
                    ("Australia/Broken_Hill", "Australia/Broken_Hill"),
                    ("Eire", "Eire"),
                    ("America/Kralendijk", "America/Kralendijk"),
                    ("Europe/Berlin", "Europe/Berlin"),
                    ("Brazil/West", "Brazil/West"),
                    ("America/Nuuk", "America/Nuuk"),
                    ("Africa/Luanda", "Africa/Luanda"),
                    ("Europe/Astrakhan", "Europe/Astrakhan"),
                    ("Europe/Zagreb", "Europe/Zagreb"),
                    ("Mexico/BajaSur", "Mexico/BajaSur"),
                    ("Pacific/Saipan", "Pacific/Saipan"),
                    ("America/Cancun", "America/Cancun"),
                    ("Kwajalein", "Kwajalein"),
                    ("Australia/Brisbane", "Australia/Brisbane"),
                    ("America/Ojinaga", "America/Ojinaga"),
                    ("Pacific/Truk", "Pacific/Truk"),
                    ("Asia/Qyzylorda", "Asia/Qyzylorda"),
                    ("Europe/Tiraspol", "Europe/Tiraspol"),
                    ("America/Argentina/Tucuman", "America/Argentina/Tucuman"),
                    ("America/Punta_Arenas", "America/Punta_Arenas"),
                    ("Europe/Uzhgorod", "Europe/Uzhgorod"),
                    ("Pacific/Efate", "Pacific/Efate"),
                    ("Libya", "Libya"),
                    ("America/Virgin", "America/Virgin"),
                    ("America/New_York", "America/New_York"),
                    ("Europe/Mariehamn", "Europe/Mariehamn"),
                    ("Europe/Sarajevo", "Europe/Sarajevo"),
                    ("Asia/Oral", "Asia/Oral"),
                    ("America/Fort_Wayne", "America/Fort_Wayne"),
                    ("Atlantic/Jan_Mayen", "Atlantic/Jan_Mayen"),
                    ("Atlantic/Stanley", "Atlantic/Stanley"),
                    ("Asia/Riyadh", "Asia/Riyadh"),
                    ("America/Argentina/La_Rioja", "America/Argentina/La_Rioja"),
                    ("Africa/Dakar", "Africa/Dakar"),
                    ("Africa/Abidjan", "Africa/Abidjan"),
                    ("Asia/Qostanay", "Asia/Qostanay"),
                    ("Antarctica/Rothera", "Antarctica/Rothera"),
                    ("Asia/Muscat", "Asia/Muscat"),
                    ("Asia/Amman", "Asia/Amman"),
                    ("Etc/GMT+2", "Etc/GMT+2"),
                    ("Etc/GMT0", "Etc/GMT0"),
                    (
                        "America/Argentina/ComodRivadavia",
                        "America/Argentina/ComodRivadavia",
                    ),
                    ("America/Costa_Rica", "America/Costa_Rica"),
                    ("America/Dawson", "America/Dawson"),
                    ("Europe/Ljubljana", "Europe/Ljubljana"),
                    ("MET", "MET"),
                    ("America/Asuncion", "America/Asuncion"),
                    ("America/Detroit", "America/Detroit"),
                    ("Asia/Beirut", "Asia/Beirut"),
                    ("Antarctica/McMurdo", "Antarctica/McMurdo"),
                    ("Asia/Seoul", "Asia/Seoul"),
                    ("Poland", "Poland"),
                    ("Africa/Juba", "Africa/Juba"),
                    ("America/Port-au-Prince", "America/Port-au-Prince"),
                    ("Europe/Chisinau", "Europe/Chisinau"),
                    ("Antarctica/Davis", "Antarctica/Davis"),
                    ("Etc/Zulu", "Etc/Zulu"),
                    ("Europe/London", "Europe/London"),
                    ("US/Eastern", "US/Eastern"),
                    ("America/St_Lucia", "America/St_Lucia"),
                    ("Pacific/Pohnpei", "Pacific/Pohnpei"),
                    ("Iceland", "Iceland"),
                    ("America/Argentina/Ushuaia", "America/Argentina/Ushuaia"),
                    ("Pacific/Guadalcanal", "Pacific/Guadalcanal"),
                    ("America/Ciudad_Juarez", "America/Ciudad_Juarez"),
                    ("Etc/GMT+0", "Etc/GMT+0"),
                    ("Etc/GMT", "Etc/GMT"),
                    ("Pacific/Kanton", "Pacific/Kanton"),
                    ("Australia/West", "Australia/West"),
                    ("Etc/GMT-14", "Etc/GMT-14"),
                    ("Etc/GMT+4", "Etc/GMT+4"),
                    ("Africa/Bangui", "Africa/Bangui"),
                    ("Pacific/Port_Moresby", "Pacific/Port_Moresby"),
                    ("Atlantic/St_Helena", "Atlantic/St_Helena"),
                    ("America/Aruba", "America/Aruba"),
                    ("America/Mazatlan", "America/Mazatlan"),
                    ("Chile/Continental", "Chile/Continental"),
                    ("Europe/Malta", "Europe/Malta"),
                    ("Indian/Kerguelen", "Indian/Kerguelen"),
                    ("Africa/Bujumbura", "Africa/Bujumbura"),
                    ("Asia/Ashkhabad", "Asia/Ashkhabad"),
                    ("Europe/Saratov", "Europe/Saratov"),
                    ("America/Indiana/Indianapolis", "America/Indiana/Indianapolis"),
                    ("GMT", "GMT"),
                    ("America/Paramaribo", "America/Paramaribo"),
                    ("Africa/Accra", "Africa/Accra"),
                    ("Africa/Johannesburg", "Africa/Johannesburg"),
                    ("Africa/Harare", "Africa/Harare"),
                    ("Cuba", "Cuba"),
                    ("America/Merida", "America/Merida"),
                    ("Africa/Conakry", "Africa/Conakry"),
                    ("Turkey", "Turkey"),
                    ("Africa/Ouagadougou", "Africa/Ouagadougou"),
                    ("America/North_Dakota/Beulah", "America/North_Dakota/Beulah"),
                    ("Pacific/Tahiti", "Pacific/Tahiti"),
                    ("Africa/Cairo", "Africa/Cairo"),
                    ("Asia/Ujung_Pandang", "Asia/Ujung_Pandang"),
                    ("Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur"),
                    ("Asia/Bangkok", "Asia/Bangkok"),
                    ("Asia/Aqtau", "Asia/Aqtau"),
                    ("Europe/Luxembourg", "Europe/Luxembourg"),
                    ("Europe/Zaporozhye", "Europe/Zaporozhye"),
                    ("Asia/Kuching", "Asia/Kuching"),
                    ("Europe/Madrid", "Europe/Madrid"),
                    ("ROK", "ROK"),
                    ("Europe/Helsinki", "Europe/Helsinki"),
                    ("Europe/Athens", "Europe/Athens"),
                    ("Africa/Ceuta", "Africa/Ceuta"),
                    ("Canada/Eastern", "Canada/Eastern"),
                    ("America/Thunder_Bay", "America/Thunder_Bay"),
                    ("Asia/Atyrau", "Asia/Atyrau"),
                    ("Etc/GMT-8", "Etc/GMT-8"),
                    ("ROC", "ROC"),
                    ("US/Mountain", "US/Mountain"),
                    ("Europe/Kyiv", "Europe/Kyiv"),
                    ("America/Indiana/Tell_City", "America/Indiana/Tell_City"),
                    ("Atlantic/Bermuda", "Atlantic/Bermuda"),
                    ("Asia/Shanghai", "Asia/Shanghai"),
                    ("America/Caracas", "America/Caracas"),
                    ("Brazil/East", "Brazil/East"),
                    ("Australia/Adelaide", "Australia/Adelaide"),
                    ("Australia/Hobart", "Australia/Hobart"),
                    ("Asia/Omsk", "Asia/Omsk"),
                    ("America/Porto_Velho", "America/Porto_Velho"),
                    ("Pacific/Fiji", "Pacific/Fiji"),
                    ("Europe/Tallinn", "Europe/Tallinn"),
                    ("America/Chihuahua", "America/Chihuahua"),
                    ("Chile/EasterIsland", "Chile/EasterIsland"),
                    ("Europe/Sofia", "Europe/Sofia"),
                    ("Pacific/Auckland", "Pacific/Auckland"),
                    ("America/Indiana/Petersburg", "America/Indiana/Petersburg"),
                    ("America/Iqaluit", "America/Iqaluit"),
                    ("America/Dawson_Creek", "America/Dawson_Creek"),
                    ("Etc/GMT+7", "Etc/GMT+7"),
                    ("America/Pangnirtung", "America/Pangnirtung"),
                    ("WET", "WET"),
                    ("America/Miquelon", "America/Miquelon"),
                    ("America/Denver", "America/Denver"),
                    ("America/Metlakatla", "America/Metlakatla"),
                    ("Asia/Kolkata", "Asia/Kolkata"),
                    ("Europe/Belgrade", "Europe/Belgrade"),
                    ("America/Swift_Current", "America/Swift_Current"),
                    ("Iran", "Iran"),
                    ("Canada/Newfoundland", "Canada/Newfoundland"),
                    ("Asia/Kuwait", "Asia/Kuwait"),
                    ("Africa/Monrovia", "Africa/Monrovia"),
                    ("America/Belem", "America/Belem"),
                    ("Asia/Tashkent", "Asia/Tashkent"),
                    ("America/Argentina/Catamarca", "America/Argentina/Catamarca"),
                    ("Europe/Skopje", "Europe/Skopje"),
                    ("Asia/Dhaka", "Asia/Dhaka"),
                    ("Pacific/Enderbury", "Pacific/Enderbury"),
                    ("Europe/Lisbon", "Europe/Lisbon"),
                    ("Asia/Gaza", "Asia/Gaza"),
                    ("NZ-CHAT", "NZ-CHAT"),
                    ("Etc/GMT-3", "Etc/GMT-3"),
                    ("America/Ensenada", "America/Ensenada"),
                    ("Pacific/Nauru", "Pacific/Nauru"),
                    (
                        "America/Argentina/Buenos_Aires",
                        "America/Argentina/Buenos_Aires",
                    ),
                    ("Europe/Amsterdam", "Europe/Amsterdam"),
                    ("Africa/Mogadishu", "Africa/Mogadishu"),
                    ("Egypt", "Egypt"),
                    ("Asia/Ulaanbaatar", "Asia/Ulaanbaatar"),
                    ("Atlantic/Faeroe", "Atlantic/Faeroe"),
                    ("America/Yakutat", "America/Yakutat"),
                    ("Etc/GMT-10", "Etc/GMT-10"),
                    ("America/Nipigon", "America/Nipigon"),
                    ("Etc/GMT+5", "Etc/GMT+5"),
                    ("America/Hermosillo", "America/Hermosillo"),
                    ("Australia/Eucla", "Australia/Eucla"),
                    ("Asia/Novokuznetsk", "Asia/Novokuznetsk"),
                    ("America/Shiprock", "America/Shiprock"),
                    ("Africa/Kinshasa", "Africa/Kinshasa"),
                    ("Australia/Yancowinna", "Australia/Yancowinna"),
                    ("Africa/Douala", "Africa/Douala"),
                    ("America/Chicago", "America/Chicago"),
                    ("America/Knox_IN", "America/Knox_IN"),
                    ("Asia/Singapore", "Asia/Singapore"),
                    ("US/Michigan", "US/Michigan"),
                    ("Asia/Baghdad", "Asia/Baghdad"),
                    ("America/Scoresbysund", "America/Scoresbysund"),
                    ("Etc/GMT+10", "Etc/GMT+10"),
                    ("America/Sitka", "America/Sitka"),
                    ("Asia/Colombo", "Asia/Colombo"),
                    ("Indian/Chagos", "Indian/Chagos"),
                    ("Asia/Kathmandu", "Asia/Kathmandu"),
                    ("Etc/GMT-11", "Etc/GMT-11"),
                    ("Indian/Cocos", "Indian/Cocos"),
                    ("America/Mendoza", "America/Mendoza"),
                    ("Asia/Karachi", "Asia/Karachi"),
                    ("America/Juneau", "America/Juneau"),
                    ("GB-Eire", "GB-Eire"),
                    ("Asia/Vladivostok", "Asia/Vladivostok"),
                    ("localtime", "localtime"),
                    ("Pacific/Noumea", "Pacific/Noumea"),
                    ("Africa/Kampala", "Africa/Kampala"),
                    ("Canada/Atlantic", "Canada/Atlantic"),
                    ("Pacific/Palau", "Pacific/Palau"),
                    ("America/Cambridge_Bay", "America/Cambridge_Bay"),
                    ("Africa/Malabo", "Africa/Malabo"),
                    ("Africa/Blantyre", "Africa/Blantyre"),
                    ("America/Kentucky/Monticello", "America/Kentucky/Monticello"),
                    ("America/Puerto_Rico", "America/Puerto_Rico"),
                    ("Asia/Jerusalem", "Asia/Jerusalem"),
                    ("Navajo", "Navajo"),
                    ("America/Santa_Isabel", "America/Santa_Isabel"),
                    ("Europe/Vienna", "Europe/Vienna"),
                    ("Asia/Khandyga", "Asia/Khandyga"),
                    ("America/Monterrey", "America/Monterrey"),
                    ("Etc/GMT-0", "Etc/GMT-0"),
                    ("Etc/GMT+1", "Etc/GMT+1"),
                    ("America/Thule", "America/Thule"),
                    ("Asia/Tel_Aviv", "Asia/Tel_Aviv"),
                    ("Pacific/Pitcairn", "Pacific/Pitcairn"),
                    ("Africa/Lome", "Africa/Lome"),
                    ("Africa/Lubumbashi", "Africa/Lubumbashi"),
                    ("Europe/Stockholm", "Europe/Stockholm"),
                    ("Asia/Macau", "Asia/Macau"),
                    ("Canada/Saskatchewan", "Canada/Saskatchewan"),
                    ("Europe/Kiev", "Europe/Kiev"),
                    ("Australia/Sydney", "Australia/Sydney"),
                    ("Africa/Casablanca", "Africa/Casablanca"),
                    ("Asia/Ust-Nera", "Asia/Ust-Nera"),
                    ("Asia/Samarkand", "Asia/Samarkand"),
                    ("Africa/Mbabane", "Africa/Mbabane"),
                    ("America/Curacao", "America/Curacao"),
                    ("Pacific/Wake", "Pacific/Wake"),
                    ("Canada/Mountain", "Canada/Mountain"),
                    ("Europe/Kaliningrad", "Europe/Kaliningrad"),
                    ("Indian/Reunion", "Indian/Reunion"),
                    ("Asia/Damascus", "Asia/Damascus"),
                    ("America/Araguaina", "America/Araguaina"),
                    ("America/Rosario", "America/Rosario"),
                    ("America/Rankin_Inlet", "America/Rankin_Inlet"),
                    ("Australia/ACT", "Australia/ACT"),
                    ("America/Argentina/San_Juan", "America/Argentina/San_Juan"),
                    ("Mexico/General", "Mexico/General"),
                    ("Europe/Oslo", "Europe/Oslo"),
                    ("America/Bogota", "America/Bogota"),
                    ("Asia/Yerevan", "Asia/Yerevan"),
                    ("Brazil/Acre", "Brazil/Acre"),
                    ("Europe/Tirane", "Europe/Tirane"),
                    ("Pacific/Wallis", "Pacific/Wallis"),
                    ("Etc/GMT-12", "Etc/GMT-12"),
                    ("Etc/GMT+8", "Etc/GMT+8"),
                    ("Etc/UCT", "Etc/UCT"),
                    ("Asia/Kamchatka", "Asia/Kamchatka"),
                    ("America/Montserrat", "America/Montserrat"),
                    ("America/Lower_Princes", "America/Lower_Princes"),
                    ("Australia/Lindeman", "Australia/Lindeman"),
                    ("Asia/Pontianak", "Asia/Pontianak"),
                    ("Asia/Chita", "Asia/Chita"),
                    ("Asia/Taipei", "Asia/Taipei"),
                    ("America/Regina", "America/Regina"),
                    ("EET", "EET"),
                    ("Europe/Belfast", "Europe/Belfast"),
                    ("America/Santo_Domingo", "America/Santo_Domingo"),
                    ("America/Recife", "America/Recife"),
                    ("Asia/Saigon", "Asia/Saigon"),
                    ("Asia/Chongqing", "Asia/Chongqing"),
                    ("America/Maceio", "America/Maceio"),
                    ("Etc/GMT+12", "Etc/GMT+12"),
                    ("America/Phoenix", "America/Phoenix"),
                    ("Africa/Windhoek", "Africa/Windhoek"),
                    ("Australia/Lord_Howe", "Australia/Lord_Howe"),
                    ("Pacific/Bougainville", "Pacific/Bougainville"),
                    ("Europe/Andorra", "Europe/Andorra"),
                    ("Africa/Porto-Novo", "Africa/Porto-Novo"),
                    ("Etc/GMT-2", "Etc/GMT-2"),
                    ("Asia/Dacca", "Asia/Dacca"),
                    ("America/Toronto", "America/Toronto"),
                    ("America/Guatemala", "America/Guatemala"),
                    ("Africa/Tripoli", "Africa/Tripoli"),
                    ("Asia/Jayapura", "Asia/Jayapura"),
                    ("America/Indiana/Marengo", "America/Indiana/Marengo"),
                    ("Indian/Comoro", "Indian/Comoro"),
                    ("EST", "EST"),
                    ("Asia/Bishkek", "Asia/Bishkek"),
                    ("Asia/Qatar", "Asia/Qatar"),
                    ("US/Alaska", "US/Alaska"),
                    ("Zulu", "Zulu"),
                    ("Factory", "Factory"),
                    ("Asia/Bahrain", "Asia/Bahrain"),
                    ("Antarctica/Vostok", "Antarctica/Vostok"),
                    ("PRC", "PRC"),
                    ("Pacific/Midway", "Pacific/Midway"),
                    ("Asia/Ashgabat", "Asia/Ashgabat"),
                    ("America/Sao_Paulo", "America/Sao_Paulo"),
                    ("America/Dominica", "America/Dominica"),
                    ("Europe/Guernsey", "Europe/Guernsey"),
                    ("America/Rainy_River", "America/Rainy_River"),
                    ("Pacific/Tongatapu", "Pacific/Tongatapu"),
                    ("MST", "MST"),
                    ("Atlantic/South_Georgia", "Atlantic/South_Georgia"),
                    ("Indian/Mayotte", "Indian/Mayotte"),
                    ("Asia/Tbilisi", "Asia/Tbilisi"),
                    ("Asia/Dili", "Asia/Dili"),
                    ("Australia/Melbourne", "Australia/Melbourne"),
                    ("Atlantic/Reykjavik", "Atlantic/Reykjavik"),
                    ("Asia/Kabul", "Asia/Kabul"),
                    ("Europe/Paris", "Europe/Paris"),
                    ("America/Winnipeg", "America/Winnipeg"),
                    ("America/Whitehorse", "America/Whitehorse"),
                    ("Europe/Nicosia", "Europe/Nicosia"),
                    ("Africa/Gaborone", "Africa/Gaborone"),
                    ("Asia/Pyongyang", "Asia/Pyongyang"),
                    ("Australia/Canberra", "Australia/Canberra"),
                    ("Europe/Istanbul", "Europe/Istanbul"),
                    ("America/Managua", "America/Managua"),
                    ("Europe/Rome", "Europe/Rome"),
                    ("Etc/GMT+9", "Etc/GMT+9"),
                    ("Europe/Vaduz", "Europe/Vaduz"),
                    ("America/Fort_Nelson", "America/Fort_Nelson"),
                    (
                        "America/North_Dakota/New_Salem",
                        "America/North_Dakota/New_Salem",
                    ),
                    ("Asia/Istanbul", "Asia/Istanbul"),
                    ("US/Pacific", "US/Pacific"),
                    ("America/Nome", "America/Nome"),
                    ("Etc/GMT-7", "Etc/GMT-7"),
                    ("America/Port_of_Spain", "America/Port_of_Spain"),
                    ("Asia/Phnom_Penh", "Asia/Phnom_Penh"),
                    ("Antarctica/Casey", "Antarctica/Casey"),
                    ("Africa/Freetown", "Africa/Freetown"),
                    ("Indian/Mahe", "Indian/Mahe"),
                    ("Africa/Khartoum", "Africa/Khartoum"),
                    ("Europe/Gibraltar", "Europe/Gibraltar"),
                    ("Europe/Busingen", "Europe/Busingen"),
                    ("Australia/North", "Australia/North"),
                    ("Canada/Central", "Canada/Central"),
                    ("Europe/Moscow", "Europe/Moscow"),
                    ("Europe/Prague", "Europe/Prague"),
                    ("Asia/Hovd", "Asia/Hovd"),
                    ("Pacific/Fakaofo", "Pacific/Fakaofo"),
                    ("Arctic/Longyearbyen", "Arctic/Longyearbyen"),
                    ("America/Yellowknife", "America/Yellowknife"),
                    ("America/Indianapolis", "America/Indianapolis"),
                    ("Etc/GMT-1", "Etc/GMT-1"),
                    ("Antarctica/Macquarie", "Antarctica/Macquarie"),
                    ("America/Santiago", "America/Santiago"),
                    ("America/Havana", "America/Havana"),
                    ("Etc/GMT-4", "Etc/GMT-4"),
                    ("Asia/Magadan", "Asia/Magadan"),
                    ("America/Santarem", "America/Santarem"),
                    ("Asia/Harbin", "Asia/Harbin"),
                    ("NZ", "NZ"),
                    ("Pacific/Ponape", "Pacific/Ponape"),
                    ("America/Campo_Grande", "America/Campo_Grande"),
                    ("America/La_Paz", "America/La_Paz"),
                    ("Africa/Niamey", "Africa/Niamey"),
                    ("Asia/Tomsk", "Asia/Tomsk"),
                    ("US/Central", "US/Central"),
                    ("US/Hawaii", "US/Hawaii"),
                    ("America/Montreal", "America/Montreal"),
                    ("Asia/Nicosia", "Asia/Nicosia"),
                    ("Pacific/Gambier", "Pacific/Gambier"),
                    ("America/St_Kitts", "America/St_Kitts"),
                    ("Africa/Addis_Ababa", "Africa/Addis_Ababa"),
                    ("America/Anchorage", "America/Anchorage"),
                    ("Asia/Tehran", "Asia/Tehran"),
                    ("Etc/GMT+6", "Etc/GMT+6"),
                    ("MST7MDT", "MST7MDT"),
                    ("Pacific/Guam", "Pacific/Guam"),
                    ("America/Indiana/Knox", "America/Indiana/Knox"),
                    ("America/Creston", "America/Creston"),
                    ("Pacific/Chatham", "Pacific/Chatham"),
                    ("Pacific/Yap", "Pacific/Yap"),
                    ("America/Atikokan", "America/Atikokan"),
                    ("Africa/Asmera", "Africa/Asmera"),
                    ("America/Boise", "America/Boise"),
                    ("Europe/Copenhagen", "Europe/Copenhagen"),
                    ("Pacific/Niue", "Pacific/Niue"),
                    ("Antarctica/Mawson", "Antarctica/Mawson"),
                    ("Europe/San_Marino", "Europe/San_Marino"),
                    ("Africa/Kigali", "Africa/Kigali"),
                    ("Asia/Baku", "Asia/Baku"),
                    ("US/Aleutian", "US/Aleutian"),
                    ("Africa/Lusaka", "Africa/Lusaka"),
                    ("Indian/Maldives", "Indian/Maldives"),
                    ("Africa/Libreville", "Africa/Libreville"),
                    ("Portugal", "Portugal"),
                    ("Asia/Tokyo", "Asia/Tokyo"),
                    ("Africa/Bissau", "Africa/Bissau"),
                    ("Asia/Yakutsk", "Asia/Yakutsk"),
                    ("America/Godthab", "America/Godthab"),
                    ("Europe/Samara", "Europe/Samara"),
                    ("Antarctica/Troll", "Antarctica/Troll"),
                    ("Europe/Riga", "Europe/Riga"),
                    ("America/Belize", "America/Belize"),
                    ("America/Glace_Bay", "America/Glace_Bay"),
                    ("Jamaica", "Jamaica"),
                    ("America/Blanc-Sablon", "America/Blanc-Sablon"),
                    ("America/Cayman", "America/Cayman"),
                    ("Pacific/Kiritimati", "Pacific/Kiritimati"),
                    ("Asia/Brunei", "Asia/Brunei"),
                    ("Europe/Vilnius", "Europe/Vilnius"),
                    ("Asia/Irkutsk", "Asia/Irkutsk"),
                    ("PST8PDT", "PST8PDT"),
                    ("Asia/Chungking", "Asia/Chungking"),
                    ("America/Panama", "America/Panama"),
                    ("America/Jujuy", "America/Jujuy"),
                    ("UTC", "UTC"),
                    ("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh"),
                    ("America/Eirunepe", "America/Eirunepe"),
                    ("GB", "GB"),
                    ("Africa/Maseru", "Africa/Maseru"),
                    ("Europe/Podgorica", "Europe/Podgorica"),
                    ("America/Argentina/Cordoba", "America/Argentina/Cordoba"),
                    ("Europe/Bucharest", "Europe/Bucharest"),
                    ("GMT+0", "GMT+0"),
                    ("America/Cayenne", "America/Cayenne"),
                    ("Universal", "Universal"),
                    ("Australia/NSW", "Australia/NSW"),
                    ("Japan", "Japan"),
                    ("Asia/Thimphu", "Asia/Thimphu"),
                    ("Hongkong", "Hongkong"),
                    ("Asia/Ulan_Bator", "Asia/Ulan_Bator"),
                    ("America/Resolute", "America/Resolute"),
                    ("Europe/Budapest", "Europe/Budapest"),
                    ("Asia/Yekaterinburg", "Asia/Yekaterinburg"),
                    ("Australia/Victoria", "Australia/Victoria"),
                    ("America/Guyana", "America/Guyana"),
                    ("America/Nassau", "America/Nassau"),
                    ("America/St_Johns", "America/St_Johns"),
                    ("America/Inuvik", "America/Inuvik"),
                    ("Asia/Aqtobe", "Asia/Aqtobe"),
                    ("Etc/GMT-13", "Etc/GMT-13"),
                    ("Asia/Hebron", "Asia/Hebron"),
                    ("Indian/Mauritius", "Indian/Mauritius"),
                    ("Mexico/BajaNorte", "Mexico/BajaNorte"),
                    ("Europe/Dublin", "Europe/Dublin"),
                    ("America/Manaus", "America/Manaus"),
                    ("Africa/Tunis", "Africa/Tunis"),
                    ("Europe/Minsk", "Europe/Minsk"),
                    ("Africa/Djibouti", "Africa/Djibouti"),
                    ("Europe/Simferopol", "Europe/Simferopol"),
                    ("Antarctica/South_Pole", "Antarctica/South_Pole"),
                    ("Asia/Kashgar", "Asia/Kashgar"),
                    ("Africa/Asmara", "Africa/Asmara"),
                    ("America/Tegucigalpa", "America/Tegucigalpa"),
                    ("America/Noronha", "America/Noronha"),
                    ("Europe/Ulyanovsk", "Europe/Ulyanovsk"),
                    ("Pacific/Galapagos", "Pacific/Galapagos"),
                    ("America/Goose_Bay", "America/Goose_Bay"),
                    ("America/Tortola", "America/Tortola"),
                    ("Australia/Queensland", "Australia/Queensland"),
                    ("Africa/Algiers", "Africa/Algiers"),
                    ("Asia/Yangon", "Asia/Yangon"),
                    ("Etc/GMT-9", "Etc/GMT-9"),
                    ("America/Cordoba", "America/Cordoba"),
                    ("America/Coral_Harbour", "America/Coral_Harbour"),
                    ("America/Catamarca", "America/Catamarca"),
                    ("Etc/Universal", "Etc/Universal"),
                    ("Australia/Currie", "Australia/Currie"),
                    ("Europe/Isle_of_Man", "Europe/Isle_of_Man"),
                    ("Asia/Dushanbe", "Asia/Dushanbe"),
                    ("Pacific/Johnston", "Pacific/Johnston"),
                    ("America/Anguilla", "America/Anguilla"),
                    ("America/Jamaica", "America/Jamaica"),
                    ("Indian/Christmas", "Indian/Christmas"),
                    ("America/Argentina/San_Luis", "America/Argentina/San_Luis"),
                    ("America/Adak", "America/Adak"),
                    ("Asia/Manila", "Asia/Manila"),
                    ("America/Grand_Turk", "America/Grand_Turk"),
                    ("Asia/Anadyr", "Asia/Anadyr"),
                    ("Africa/Lagos", "Africa/Lagos"),
                    ("America/Fortaleza", "America/Fortaleza"),
                    ("US/Arizona", "US/Arizona"),
                    ("America/St_Barthelemy", "America/St_Barthelemy"),
                    ("Antarctica/Palmer", "Antarctica/Palmer"),
                    ("America/Indiana/Winamac", "America/Indiana/Winamac"),
                    ("Etc/UTC", "Etc/UTC"),
                    ("Asia/Srednekolymsk", "Asia/Srednekolymsk"),
                    ("US/East-Indiana", "US/East-Indiana"),
                    ("Etc/GMT+11", "Etc/GMT+11"),
                    ("Australia/Perth", "Australia/Perth"),
                    ("Africa/Sao_Tome", "Africa/Sao_Tome"),
                    ("Greenwich", "Greenwich"),
                    ("America/Barbados", "America/Barbados"),
                    ("Africa/Dar_es_Salaam", "Africa/Dar_es_Salaam"),
                    ("Pacific/Tarawa", "Pacific/Tarawa"),
                    ("Europe/Kirov", "Europe/Kirov"),
                    ("America/Montevideo", "America/Montevideo"),
                    ("Etc/GMT-6", "Etc/GMT-6"),
                    ("Africa/Nairobi", "Africa/Nairobi"),
                    ("Asia/Makassar", "Asia/Makassar"),
                    ("Etc/GMT+3", "Etc/GMT+3"),
                    ("Pacific/Kwajalein", "Pacific/Kwajalein"),
                    ("Pacific/Samoa", "Pacific/Samoa"),
                    ("Europe/Jersey", "Europe/Jersey"),
                    ("Pacific/Kosrae", "Pacific/Kosrae"),
                    ("Asia/Rangoon", "Asia/Rangoon"),
                    ("Europe/Brussels", "Europe/Brussels"),
                    ("Asia/Barnaul", "Asia/Barnaul"),
                    ("US/Indiana-Starke", "US/Indiana-Starke"),
                    ("Canada/Yukon", "Canada/Yukon"),
                    ("Pacific/Honolulu", "Pacific/Honolulu"),
                    ("America/Vancouver", "America/Vancouver"),
                    ("Pacific/Norfolk", "Pacific/Norfolk"),
                    ("America/Menominee", "America/Menominee"),
                    ("America/Argentina/Jujuy", "America/Argentina/Jujuy"),
                    ("America/Buenos_Aires", "America/Buenos_Aires"),
                    ("Asia/Choibalsan", "Asia/Choibalsan"),
                    ("America/Mexico_City", "America/Mexico_City"),
                    ("HST", "HST"),
                    ("America/Indiana/Vincennes", "America/Indiana/Vincennes"),
                    ("Indian/Antananarivo", "Indian/Antananarivo"),
                    ("Antarctica/Syowa", "Antarctica/Syowa"),
                    ("Canada/Pacific", "Canada/Pacific"),
                    ("America/Atka", "America/Atka"),
                    ("America/Martinique", "America/Martinique"),
                    ("CET", "CET"),
                    ("Australia/LHI", "Australia/LHI"),
                    ("America/St_Vincent", "America/St_Vincent"),
                    ("Europe/Vatican", "Europe/Vatican"),
                    ("GMT-0", "GMT-0"),
                    ("Pacific/Apia", "Pacific/Apia"),
                    ("Atlantic/Azores", "Atlantic/Azores"),
                    ("America/Antigua", "America/Antigua"),
                    ("EST5EDT", "EST5EDT"),
                    ("America/Danmarkshavn", "America/Danmarkshavn"),
                    ("Atlantic/Canary", "Atlantic/Canary"),
                    ("Asia/Krasnoyarsk", "Asia/Krasnoyarsk"),
                    ("America/Kentucky/Louisville", "America/Kentucky/Louisville"),
                    ("Asia/Vientiane", "Asia/Vientiane"),
                    ("Europe/Monaco", "Europe/Monaco"),
                    ("America/Bahia", "America/Bahia"),
                    ("GMT0", "GMT0"),
                    ("Australia/Tasmania", "Australia/Tasmania"),
                    ("America/Indiana/Vevay", "America/Indiana/Vevay"),
                    ("Asia/Novosibirsk", "Asia/Novosibirsk"),
                    ("America/Boa_Vista", "America/Boa_Vista"),
                    ("CST6CDT", "CST6CDT"),
                    ("Asia/Hong_Kong", "Asia/Hong_Kong"),
                    ("Pacific/Pago_Pago", "Pacific/Pago_Pago"),
                    ("Asia/Dubai", "Asia/Dubai"),
                    ("Asia/Thimbu", "Asia/Thimbu"),
                    ("America/North_Dakota/Center", "America/North_Dakota/Center"),
                    ("US/Samoa", "US/Samoa"),
                    ("America/Tijuana", "America/Tijuana"),
                    ("Australia/South", "Australia/South"),
                    ("America/Porto_Acre", "America/Porto_Acre"),
                    ("Asia/Macao", "Asia/Macao"),
                    ("Africa/El_Aaiun", "Africa/El_Aaiun"),
                    ("Europe/Zurich", "Europe/Zurich"),
                    ("America/Rio_Branco", "America/Rio_Branco"),
                    ("Atlantic/Cape_Verde", "Atlantic/Cape_Verde"),
                    ("America/Moncton", "America/Moncton"),
                    (
                        "America/Argentina/Rio_Gallegos",
                        "America/Argentina/Rio_Gallegos",
                    ),
                    ("America/Guadeloupe", "America/Guadeloupe"),
                    ("Africa/Bamako", "Africa/Bamako"),
                    ("America/El_Salvador", "America/El_Salvador"),
                    ("America/Louisville", "America/Louisville"),
                    ("America/Matamoros", "America/Matamoros"),
                ],
                default="America/Los_Angeles",
                max_length=255,
            ),
        ),
    ]