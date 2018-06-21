import json

JSON_A = {
	"locker_5_light": 1,
	"locker_5_unlock": 2,
	"locker_6_light": 1,
	"locker_6_unlock": 1,
	"locker_1_door": 1,
	"locker_1_item": 1,
	"locker_2_door": 1,
	"locker_2_item": 2,
	"locker_5_door": 1,
	"locker_5_item": 5,
	"locker_6_door": 1,
	"locker_6_item": 1,
	"locker_1_light": 0,
	"locker_1_unlock": 1,
	"locker_2_light": 1,
	"locker_2_unlock": 1,
	"locker_3_light": 1,
	"locker_3_unlock": 1,
	"locker_4_light": 1,
	"locker_4_unlock": 1,
	"locker_3_door": 1,
	"locker_3_item":3,
	"locker_4_door": 1,
	"locker_4_item": 0
	}

JSON_B = {
	'1': {
		'door': 1,
		'item': 1,
		'light': 0,
		'unlock': 1
	},
	'2': {
		'door': 1,
		'item': 2,
		'light': 1,
		'unlock': 1
	},
	'3': {
		'door': 1,
		'item': 3,
		'light': 1,
		'unlock': 1
	},
	'4': {
		'door': 1,
		'item': 0,
		'light': 1,
		'unlock': 1
	},
	'5': {
		'door': 1,
		'item': 5,
		'light': 1,
		'unlock': 2
	},
	'6': {
		'door': 1,
		'item': 1,
		'light': 1,
		'unlock': 1
	}
}

JSON_C =[
	{
		'message': 'rx_locker_12',
		'signals': {
			'locker_1_door': 1,
			'locker_1_item': 1,
			'locker_2_door': 1,
			'locker_2_item': 2
		}
	},
	{
		'message': 'rx_locker_34',
		'signals': {
			'locker_3_door': 1,
			'locker_3_item': 3,
			'locker_4_door': 1,
			'locker_4_item': 0
		}
	},
	{
		'message': 'rx_locker_56',
		'signals': {
			'locker_5_door': 1,
			'locker_5_item': 5,
			'locker_6_door': 1,
			'locker_6_item': 1
		}
	}
]

with open('JSON_A.txt', 'w') as outfile:
	json.dump(JSON_A, outfile)

with open('JSON_B.txt', 'w') as outfile:
	json.dump(JSON_B, outfile)

with open('JSON_C.txt', 'w') as outfile:
	json.dump(JSON_C, outfile)

JA = {}

with open('JSON_A.txt') as json_file:
	data = json.load(json_file)
	JA = data
	# print('JSON_A')
	# print(json.dumps(data, indent=4, sort_keys=True))
	# print

JB = {}
with open('JSON_B.txt') as json_file:
	JB = json.load(json_file)



# with open('JSON_C.txt') as json_file:
# 	data = json.load(json_file)
	# for parsed in data:
	# 	print(parsed)
	# print(data)
	# print('JSON_C')
	# print(json.dumps(data, indent=4, sort_keys=True))
	# print


def convertToJSON_B(JSON_A):
	if JSON_A is None:
		return 'N/A'

	result = {}
	for p in JSON_A:
		par = str(p)
		lo, num, it = par.split('_')
		key = str(num)
		if key in result:
			result[key][it] = JSON_A[par]
		else:
			new_item = {
						'door': -1,
						'item': -1,
						'light': -1,
						'unlock': -1
						}
						
			result[key] = new_item
			result[key][it] = JSON_A[par]
	return result


def convertToJSON_C(JSON_B):
	if JSON_A is None:
		return 'N/A'

	result = []
	for p in JSON_B:
		index = int(p)

		#index check: must within [1, len(JSON_B)]
		if index <= 0 or index > len(JSON_B):
			print('out of range: '+ par)
			continue
		else: # correct index
			input_data = JSON_B[str(p)]

			#key to which element belongs to 
			new_key_1 = 'locker_'+str(index)+'_door'
			new_key_2 = 'locker_'+str(index)+'_item'
			# print('new_key_1: {}'.format(new_key_1))
			# print('new_key_2: {}'.format(new_key_2))
			#values to which element belongs to 
			new_door = input_data['door']
			new_item = input_data['item']
			# print('new_door_1: {}'.format(new_door))
			# print('new_item_2: {}'.format(new_item))

			exist = False
			#check if exist
			for ele in range(len(result)):
				p_in = result[ele]["message"]
				if str(index) in p_in:
					exist = True

			if not exist:
				ele_start = index
				if index%2 == 0: #in case of 6 for example
					ele_start = index -1
				ele_end = ele_start+1
				# print('start: {}\tend:{}'.format(ele_start,ele_end))
				new_pair = {
							'message': 'rx_locker_' +str(ele_start)+str(ele_end),
							'signals': {
								'locker_'+str(ele_start)+'_door': -1,
								'locker_'+str(ele_start)+'_item': -1,
								'locker_'+str(ele_end)+'_door': -1,
								'locker_'+str(ele_end)+'_item': -1
								}
							}
				# if len(result) <= 0:
				# 	result = [new_item]
				# else:
				result.append(new_pair.copy())

			ele_index = index/2
			if index%2 == 0:
				ele_index -=1
			result[ele_index]['signals'][new_key_1] = new_door
			result[ele_index]['signals'][new_key_2] = new_item

	return result


#TEST 1
jb = convertToJSON_B(JA)

# dumpclean(jb)
# print(json.dumps(jb, indent=4, sort_keys=True))

with open('JSON_A2B.txt', 'w') as outfile:
	json.dump(jb, outfile)


with open('JSON_A2B.txt') as json_file:
	data = json.load(json_file)
	print('JSON_A2B')
	print(json.dumps(data, indent=4, sort_keys=True))
	print


#TEST 2
jc = convertToJSON_C(JB)

# dumpclean(jb)
# print(json.dumps(jb, indent=4, sort_keys=True))

with open('JSON_B2C.txt', 'w') as outfile:
	json.dump(jc, outfile)


with open('JSON_B2C.txt') as json_file:
	data = json.load(json_file)
	print('JSON_B2C')
	print(json.dumps(data, indent=4, sort_keys=True))
	print