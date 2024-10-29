import difflib

def compare_dict(old_dict, new_dict, result_path):
    write_file = open(result_path, 'w', encoding='utf-8')

    for item_id in new_dict:
        # Both dict exist
        if item_id in old_dict:

            # But diffrent
            if old_dict[item_id] != new_dict[item_id]:
                print('# - 發現 [ 敘述變更 ]: {0} - {1}'.format(item_id, new_dict[item_id]['Name_TC']))
                differ = difflib.Differ()
                diff = differ.compare(old_dict[item_id]['Descript'].splitlines(), new_dict[item_id]['Descript'].splitlines())

                write_file.write(
                    '[ID: {0}] {1} (敘述變更)\n{2}\n\n----- ----- -----\n\n'.format(
                        item_id,
                        new_dict[item_id]['Name_TC'],
                        '\n'.join([line for line in diff if not line.startswith('? ')]),
                    )
                )

        # New item
        else:
            print('# - 發現 [ 新增道具 ]: {0} - {1}'.format(item_id, new_dict[item_id]['Name_TC']))
            write_file.write(
                '[ID: {0}] {1} (新增道具)\n{2}\n\n----- ----- -----\n\n'.format(
                    item_id,
                    new_dict[item_id]['Name_TC'],
                    new_dict[item_id]['Descript'],
                )
            )

    write_file.write('文件到此結束.')