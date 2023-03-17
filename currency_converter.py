import sys
import re

data = """AUDUSD=0.8371
CADUSD=0.8711
USDCNY=6.1715
EURUSD=1.2315
GBPUSD=1.5683
NZDUSD=0.7750
USDJPY=119.95
EURCZK=27.6028
EURDKK=7.4405
EURNOK=8.6651"""

try:
	args = sys.argv
	input_ = args[1]
	output_ = args[2]
	currency = float(args[3])
except:
	input_ = output_ = currency = None

def convertCurrency(input_=input_, output_=output_, currency=currency):
	if input_ + output_ in data:
		_, real, comp = re.findall(f'({input_}{output_})=(\d+).(\d+)\n', data)[0]
		return float(real + '.' + comp) * int(currency)
	elif output_ + input_ in data:
		_, real, comp = re.findall(f'({output_}{input_})=(\d+).(\d+)\n', data)[0]
		return (1 / float(real + '.' + comp)) * int(currency)

	else:
		return "Invalid Currency Codes"
	
print(convertCurrency())

	
	