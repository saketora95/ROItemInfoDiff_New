def lua_transfer(input_file_path, encoding):
    raw_data = []
    for line in open(input_file_path, 'r', encoding=encoding):
        if line[0] in ['[', 'u', 'i']:
            raw_data.append(line.strip('\n'))

    item_dict = {}
    id = '0'
    for line in raw_data:
        # 1st line, get item id
        if line[0] == '[':
            id = line[1:line.find(']')]
            item_dict[id] = {}

        # 2nd line, get item name
        if line[0] == 'u':
            tc_index = line.find('identifiedDisplayName')
            kr_index = line.find('identifiedResourceName')

            item_dict[id]['Name_TC'] = line[
                (tc_index + 25) : (kr_index - 3)
            ]

        # 3rd line, get item descript
        if line[0] == 'i':
            raw_descript = line[30 : line.find('}')]
            item_dict[id]['Descript'] = raw_descript.replace('\", \"', '\n').replace('\"', '')

            # Remove color code
            while True:
                code_index = item_dict[id]['Descript'].find('^')
                if code_index == -1:
                    break
                else:
                    item_dict[id]['Descript'] = item_dict[id]['Descript'][:code_index] + item_dict[id]['Descript'][code_index + 7:]
            
            # Slot number
            slot_index = line.find('slotCount')
            item_dict[id]['Slot'] = line[slot_index + 12:slot_index + 13]

    return item_dict