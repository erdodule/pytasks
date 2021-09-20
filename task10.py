day = int(input("Input birthday: "))
month = input("Input month of birth : ")
if month.lower() == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month.lower() == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month.lower() == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month.lower() == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month.lower() == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month.lower() == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month.lower() == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month.lower() == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month.lower() == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month.lower() == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month.lower() == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month.lower() == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)