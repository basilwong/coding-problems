"""
Did not meet memory requirements for full points. 
"""
def process_script(i, script_list):
    ret = list()
    while i < len(script_list):
        num_temp = list()

        # Special case: Start of program
        if script_list[i].isdigit():
            while script_list[i].isdigit():
                num_temp.append(script_list[i])
                i += 1
            multiplier = int("".join(num_temp))
            if script_list[i] == "(":
                i += 1
                processed, j = process_script(i, script_list)
                i = j
                ret.extend(processed * multiplier)
            else:
                print("Something wrong.")

        # Special case: End of program
        elif script_list[i] == ")":
            return (ret, i + 1)

        # Normal case: letter
        else:
            ret.append(script_list[i])
            i += 1

    return (ret, i)



def navigate(script):
    processed_script, n = process_script(0, list(script))
    MOVEMENT_DICT = {
                "N" : (0, -1),
                "S": (0, 1),
                "W": (-1, 0),
                "E": (1, 0)
                }
    EDGE = 10**9
    location = [0, 0]
    for move in processed_script:
        location[0], location[1] = (MOVEMENT_DICT[move][0] + location[0]) % EDGE, (MOVEMENT_DICT[move][1] + location[1]) % EDGE

    return [x + 1 for x in location]




if __name__ =="__main__":
    cases = input()
    for case in range(int(cases)):
        script = input()
        w, h = navigate(script)
        print("Case #"+ str(case + 1) + ": " + str(w) + " " + str(h))
