## call student names
import sys

from dask.rewrite import args
def verify_path(path = []):
    import os
    if len(path)==2: # if the function was called with a directory of the students
        path_to_json = path[1] # make the path what ever was called
        if not path_to_json.endswith("\\students"):
            raise ValueError("""Path entered doesn't end with 'students'. Probably wrong path.
                You may try calling the file without any path and it might work, otherwise try writing the correct path to the students folder""")

    else:
        # get path where file is saved (not where it is run from). it's longer but it's safer
        app_path = os.path.realpath(__file__)
        # take away the slashes and lose "application\\call_students.py":
        split_path = app_path.split('\\')[0:-2]
        if len(split_path) == 1:  # in case it is run on a different system, slashes might be forward slashes
            split_path = app_path.split('/')[0:-2]
            if len(split_path) == 1:
                raise FileNotFoundError("The script can't separate the file path of where 'call_students' is located and so it can't go back and approach the 'students' folder.")

            # add "students" folder to the path
            split_path.append("students")
            # join the strings and create a path
            path_to_json = "/".join(split_path)

        else:
            # add "students" folder to the path
            split_path.append("students")
            path_to_json = "\\".join(split_path)

    return path_to_json

def call_students(path = []):
    import os, json
    path_to_json = verify_path(path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which names will be added
    name_list = list()
    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_dict = json.load(current_json_file)
            # get name from text of current json file:
            current_name = current_json_dict['name']
            # add name to list:
            name_list.append(current_name)
    # sort names (case insensitive)
    sorted_list = sorted(name_list, key=str.casefold)
    return (sorted_list)

def name_to_json(name, path=[]):
    import os, json
    path_to_json = verify_path(path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which names will be added
    name_list = list()

    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_loaded = json.load(current_json_file)
            # get name from text of current json file:
            current_name = current_json_loaded['name']
            if current_name == name:
                break

    return (current_json_loaded)



def search_engine(dictionary_entered = {}, path=[]):
    import os, json
    path_to_json = verify_path(path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which names will be added
    name_list = list()
    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_dict = json.load(current_json_file)
            overlapping_keys = set(dictionary_entered).intersection(set(current_json_dict))
            for key in overlapping_keys:
                # print(f'key: {key}\n')
                # print(f'dictionary_entered[key]: {dictionary_entered[key]} VS current_json_dict: {current_json_dict[key]}')
                if len(dictionary_entered[key]) > 1 and (type(dictionary_entered[key]) == list) and current_json_dict[key]:
                    # print('len is >1 and type is list\n')
                    for val in [str(v.lower()) for v in dictionary_entered[key]]: # syntax to make all elements in list lowercase
                        if type(current_json_dict[key])==list:
                            to_compare = [str(v.lower()) for v in current_json_dict[key]]
                        else:
                            to_compare = current_json_dict[key].lower()

                        if val in to_compare:
                            # get name from text of current json file:
                            current_name = current_json_dict['name']
                            # print(f'current_name: {current_name}\n')
                            # add name to list:
                            if current_name not in name_list:
                                name_list.append(current_name)
                elif current_json_dict[key]:
                    # print(f'\n{dictionary_entered[key].lower()}')
                    # print(f'\n{current_json_dict[key].lower()}')
                    if type(current_json_dict[key])==list:
                        to_compare = [str(v.lower()) for v in current_json_dict[key]]
                    else:
                        to_compare = str(current_json_dict[key].lower())

                    if type(dictionary_entered[key]) == list:
                        entered = [str(v.lower()) for v in dictionary_entered[key]][0]
                    else:
                        entered = dictionary_entered[key].lower()

                    if entered in to_compare:
                        # get name from text of current json file:
                        current_name = current_json_dict['name']
                        # print(f'current_name2: {current_name}\n')
                        # add name to list:
                        if current_name not in name_list:
                            name_list.append(current_name)

    sorted_list = sorted(name_list, key=str.casefold)
    return sorted_list


def get_key_list(path=[]):
    import os, json
    path_to_json = verify_path(path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which keys will be added
    key_list = list(["name"])
    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_dict = json.load(current_json_file)
            keys = list(current_json_dict.keys())
            key_list.extend([i for i in keys if i not in key_list])

    return key_list

def main(args):
    print(call_students(args))

if __name__ == '__main__':
    main(sys.argv)

