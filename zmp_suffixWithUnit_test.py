def suffixWithUnit(number):
	if number < 0:
		return 'N/A'

	K = 1E3
	M = 1E6
	K_UNIT = 'Kilo'
	M_UNIT = 'Mega'
	result = ''
	m_part = 0
	m_res = 0
	unit = ''

	if int(number/M) > 0:
		m_part = int(number/M)
		m_res = int(number%M)
		unit = M_UNIT
	elif int(number/K) > 0:
		m_part = int(number/K)
		m_res = int(number%K)
		unit = K_UNIT
	else:
		return str(number)
	
	result = str(m_part) + str('.') + str(m_res) +' '+ unit

	return result

res1 = suffixWithUnit(-1)
print(res1)

res1 = suffixWithUnit(123)
print(res1)

res1 = suffixWithUnit(1234)
print(res1)

res1 = suffixWithUnit(12345)
print(res1)

res1 = suffixWithUnit(1234567)
print(res1)

res1 = suffixWithUnit(12345678)
print(res1)