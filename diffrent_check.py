import difflib

def compare_dict(old_dict, new_dict, result_path, encoding):

    write_file = open(result_path, 'w', encoding='utf-8')

    for item_id in new_dict:
        # Both dict exist
        if item_id in old_dict:

            # But diffrent
            if old_dict[item_id] != new_dict[item_id]:

                print('        - 發現 [ 內容變更 ]: {0} - {1}'.format(item_id, new_dict[item_id]['Name_TC']))
                differ = difflib.Differ()
                diff = differ.compare(old_dict[item_id]['Descript'].splitlines(), new_dict[item_id]['Descript'].splitlines())

                temp_text = ''
                if old_dict[item_id]['Name_TC'] != new_dict[item_id]['Name_TC'] or old_dict[item_id]['Slot'] != new_dict[item_id]['Slot']:
                    temp_text += '- [ID: {0}] {1}{2}\n+ '.format(
                        item_id,
                        old_dict[item_id]['Name_TC'],
                        ' [{0}]'.format(old_dict[item_id]['Slot']) if old_dict[item_id]['Slot'] != 0 else ''
                    )

                temp_text += '[ID: {0}] {1}{2} (內容變更)\n{3}\n\n----- ----- -----\n\n'.format(
                    item_id,
                    new_dict[item_id]['Name_TC'],
                    ' [{0}]'.format(new_dict[item_id]['Slot']) if new_dict[item_id]['Slot'] != 0 else '',
                    '\n'.join([line for line in diff if not line.startswith('? ')]),
                )

                write_file.write(temp_text)

        # New item
        else:
            print('        - 發現 [ 新增道具 ]: {0} - {1}'.format(item_id, new_dict[item_id]['Name_TC']))
            if new_dict[item_id]['Slot'] == 0:
                write_file.write(
                    '[ID: {0}] {1} (新增道具)\n{2}\n\n----- ----- -----\n\n'.format(
                        item_id,
                        new_dict[item_id]['Name_TC'],
                        new_dict[item_id]['Descript'],
                    )
                )
            else:
                write_file.write(
                    '[ID: {0}] {1} [{2}] (新增道具)\n{3}\n\n----- ----- -----\n\n'.format(
                        item_id,
                        new_dict[item_id]['Name_TC'],
                        new_dict[item_id]['Slot'],
                        new_dict[item_id]['Descript'],
                    )
                )

    write_file.write('文件到此結束.')