import json

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