def xstr(s):
    if s is None:
        return ''
    s = str(s).replace('"', " ")
    return s


def splitDate(period):
    start_date, end_date = "",""
    period = period.replace("–","-")
    split_period = period.split("-")
    second_split_space = period.split(" ")
    if len(split_period) > 1:
        start_date = split_period[0]
        end_date = split_period[1]
    elif len(split_period) == 1 and len(second_split_space) == 1:
        start_date = period
        end_date = period
    elif len(second_split_space) == 2 and second_split_space[0].isnumeric() and second_split_space[1].isnumeric():
        start_date = second_split_space[0]
        end_date = second_split_space[1]
    return start_date, end_date


def obj_print(s):
    new_s = '"' + str(s) + '".'
    return new_s