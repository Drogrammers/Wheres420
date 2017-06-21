#!/usr/bin/env python3.6
"""
        Where's 4:20?
    This script lets you answer that question,
    although remember! It's not always 420 somewhere
    (since timezones shift of an integer amount of hours
    from each other), but it's gonna be soon enough!
"""
import os
import time
import random

timezones = ["Europe/Andorra", "Asia/Dubai", "Asia/Kabul", "Europe/Tirane", "Asia/Yerevan", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Mawson", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "America/Argentina/Buenos_Aires", "America/Argentina/Cordoba", "America/Argentina/Salta", "America/Argentina/Jujuy", "America/Argentina/Tucuman", "America/Argentina/Catamarca", "America/Argentina/La_Rioja", "America/Argentina/San_Juan", "America/Argentina/Mendoza", "America/Argentina/San_Luis", "America/Argentina/Rio_Gallegos", "America/Argentina/Ushuaia", "Pacific/Pago_Pago", "Europe/Vienna", "Australia/Lord_Howe", "Antarctica/Macquarie", "Australia/Hobart", "Australia/Currie", "Australia/Melbourne", "Australia/Sydney", "Australia/Broken_Hill", "Australia/Brisbane", "Australia/Lindeman", "Australia/Adelaide", "Australia/Darwin", "Australia/Perth", "Australia/Eucla", "Asia/Baku", "America/Barbados", "Asia/Dhaka", "Europe/Brussels", "Europe/Sofia", "Atlantic/Bermuda", "Asia/Brunei", "America/La_Paz", "America/Noronha", "America/Belem", "America/Fortaleza", "America/Recife", "America/Araguaina", "America/Maceio", "America/Bahia", "America/Sao_Paulo", "America/Campo_Grande", "America/Cuiaba", "America/Santarem", "America/Porto_Velho", "America/Boa_Vista", "America/Manaus", "America/Eirunepe", "America/Rio_Branco", "America/Nassau", "Asia/Thimphu", "Europe/Minsk", "America/Belize", "America/St_Johns", "America/Halifax", "America/Glace_Bay", "America/Moncton", "America/Goose_Bay", "America/Blanc-Sablon", "America/Toronto", "America/Nipigon", "America/Thunder_Bay", "America/Iqaluit", "America/Pangnirtung", "America/Atikokan", "America/Winnipeg", "America/Rainy_River", "America/Resolute", "America/Rankin_Inlet", "America/Regina", "America/Swift_Current", "America/Edmonton", "America/Cambridge_Bay", "America/Yellowknife", "America/Inuvik", "America/Creston", "America/Dawson_Creek", "America/Fort_Nelson", "America/Vancouver", "America/Whitehorse", "America/Dawson", "Indian/Cocos", "Europe/Zurich", "Africa/Abidjan", "Pacific/Rarotonga", "America/Santiago", "America/Punta_Arenas", "Pacific/Easter", "Asia/Shanghai", "Asia/Urumqi", "America/Bogota", "America/Costa_Rica", "America/Havana", "Atlantic/Cape_Verde", "America/Curacao", "Indian/Christmas", "Asia/Nicosia", "Asia/Famagusta", "Europe/Prague", "Europe/Berlin", "Europe/Copenhagen", "America/Santo_Domingo", "Africa/Algiers", "America/Guayaquil", "Pacific/Galapagos", "Europe/Tallinn", "Africa/Cairo", "Africa/El_Aaiun", "Europe/Madrid", "Africa/Ceuta", "Atlantic/Canary", "Europe/Helsinki", "Pacific/Fiji", "Atlantic/Stanley", "Pacific/Chuuk", "Pacific/Pohnpei", "Pacific/Kosrae", "Atlantic/Faroe", "Europe/Paris", "Europe/London", "Asia/Tbilisi", "America/Cayenne", "Africa/Accra", "Europe/Gibraltar", "America/Godthab", "America/Danmarkshavn", "America/Scoresbysund", "America/Thule", "Europe/Athens", "Atlantic/South_Georgia", "America/Guatemala", "Pacific/Guam", "Africa/Bissau", "America/Guyana", "Asia/Hong_Kong", "America/Tegucigalpa", "America/Port-au-Prince", "Europe/Budapest", "Asia/Jakarta", "Asia/Pontianak", "Asia/Makassar", "Asia/Jayapura", "Europe/Dublin", "Asia/Jerusalem", "Asia/Kolkata", "Indian/Chagos", "Asia/Baghdad", "Asia/Tehran", "Atlantic/Reykjavik", "Europe/Rome", "America/Jamaica", "Asia/Amman", "Asia/Tokyo", "Africa/Nairobi", "Asia/Bishkek", "Pacific/Tarawa", "Pacific/Enderbury", "Pacific/Kiritimati", "Asia/Pyongyang", "Asia/Seoul", "Asia/Almaty", "Asia/Qyzylorda", "Asia/Aqtobe", "Asia/Aqtau", "Asia/Atyrau", "Asia/Oral", "Asia/Beirut", "Asia/Colombo", "Africa/Monrovia", "Europe/Vilnius", "Europe/Luxembourg", "Europe/Riga", "Africa/Tripoli", "Africa/Casablanca", "Europe/Monaco", "Europe/Chisinau", "Pacific/Majuro", "Pacific/Kwajalein", "Asia/Yangon", "Asia/Ulaanbaatar", "Asia/Hovd", "Asia/Choibalsan", "Asia/Macau", "America/Martinique", "Europe/Malta", "Indian/Mauritius", "Indian/Maldives", "America/Mexico_City", "America/Cancun", "America/Merida", "America/Monterrey", "America/Matamoros", "America/Mazatlan", "America/Chihuahua", "America/Ojinaga", "America/Hermosillo", "America/Tijuana", "America/Bahia_Banderas", "Asia/Kuala_Lumpur", "Asia/Kuching", "Africa/Maputo", "Africa/Windhoek", "Pacific/Noumea", "Pacific/Norfolk", "Africa/Lagos", "America/Managua", "Europe/Amsterdam", "Europe/Oslo", "Asia/Kathmandu", "Pacific/Nauru", "Pacific/Niue", "Pacific/Auckland", "Pacific/Chatham", "America/Panama", "America/Lima", "Pacific/Tahiti", "Pacific/Marquesas", "Pacific/Gambier", "Pacific/Port_Moresby", "Pacific/Bougainville", "Asia/Manila", "Asia/Karachi", "Europe/Warsaw", "America/Miquelon", "Pacific/Pitcairn", "America/Puerto_Rico", "Asia/Gaza", "Asia/Hebron", "Europe/Lisbon", "Atlantic/Madeira", "Atlantic/Azores", "Pacific/Palau", "America/Asuncion", "Asia/Qatar", "Indian/Reunion", "Europe/Bucharest", "Europe/Belgrade", "Europe/Kaliningrad", "Europe/Moscow", "Europe/Simferopol", "Europe/Volgograd", "Europe/Kirov", "Europe/Astrakhan", "Europe/Saratov", "Europe/Ulyanovsk", "Europe/Samara", "Asia/Yekaterinburg", "Asia/Omsk", "Asia/Novosibirsk", "Asia/Barnaul", "Asia/Tomsk", "Asia/Novokuznetsk", "Asia/Krasnoyarsk", "Asia/Irkutsk", "Asia/Chita", "Asia/Yakutsk", "Asia/Khandyga", "Asia/Vladivostok", "Asia/Ust-Nera", "Asia/Magadan", "Asia/Sakhalin", "Asia/Srednekolymsk", "Asia/Kamchatka", "Asia/Anadyr", "Asia/Riyadh", "Pacific/Guadalcanal", "Indian/Mahe", "Africa/Khartoum", "Europe/Stockholm", "Asia/Singapore", "America/Paramaribo", "America/El_Salvador", "Asia/Damascus", "America/Grand_Turk", "Africa/Ndjamena", "Indian/Kerguelen", "Asia/Bangkok", "Asia/Dushanbe", "Pacific/Fakaofo", "Asia/Dili", "Asia/Ashgabat", "Africa/Tunis", "Pacific/Tongatapu", "Europe/Istanbul", "America/Port_of_Spain", "Pacific/Funafuti", "Asia/Taipei", "Europe/Kiev", "Europe/Uzhgorod", "Europe/Zaporozhye", "Pacific/Wake", "America/New_York", "America/Detroit", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Indiana/Indianapolis", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Vevay", "America/Chicago", "America/Indiana/Tell_City", "America/Indiana/Knox", "America/Menominee", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/North_Dakota/Beulah", "America/Denver", "America/Boise", "America/Phoenix", "America/Los_Angeles", "America/Anchorage", "America/Juneau", "America/Sitka", "America/Metlakatla", "America/Yakutat", "America/Nome", "America/Adak", "Pacific/Honolulu", "America/Montevideo", "Asia/Samarkand", "Asia/Tashkent", "America/Caracas", "Asia/Ho_Chi_Minh", "Pacific/Efate", "Pacific/Wallis", "Pacific/Apia", "Africa/Johannesburg"]

original_offset = time.altzone

def is420zone(hours: int = 0, minutes: int = None) -> bool:
    """
     Returns a bool indicating if the current timezone
     is one of the lucky ones about to have a 420 happening
     in 59 minutes or less!
    """
    if not hours or not minutes:
        _ = time.localtime()
        hours, minutes = _.tm_hour, _.tm_min
    if (hours == 15 and minutes > 20) or (hours == 16 and minutes < 20):
        return True
    return False

def picktimezone():
    """
    For all the timezones, sets it as the current timezone
    (for the current python interpreter's instance only)
    and collects those zone about to have a 420 soon in
    a list, which it returns.
    """
    results = []
    for zone in timezones:
        os.environ['TZ'] = zone
        time.tzset()
        if is420zone():
            results.append(zone)
    return results

def wheres420() -> str:
    """
    Returns a string indicating where in the world it is 420
    or where it is about to be. Notice that if it is 420 in your
    current timezone, it will simply report that.
    """
    result = "It's "
    _ = time.localtime()
    hours, minutes = _.tm_hour, _.tm_min
    if minutes != 20:
        result += "going to be "
    result += "420 in "
    if is420zone(hours, minutes):
            result += "your current timezone "
    else:
        tz = random.choice(picktimezone()).split('/')
        result += f'{tz[1].replace("_", " ")} (which is in {tz[0]}) '
    if minutes != 20:
        result += " in {} minutes".format((60-minutes)+20 if minutes > 20 else 20-minutes)
    return result + '!'

if __name__ == "__main__":
    print(wheres420())
