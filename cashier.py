register = {
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
}

from decimal import Decimal

def get_biggest_change(diff):
    current_high = 0
    current_key = ""
    for k,v in register.items():
        if v <= diff and v > current_high:
            current_high = v
            current_key = k
    return current_high,current_key

if __name__ == "__main__":
    pp_ch = input("Enter PP:CH")
    #change = []
    change_words = ""
    if pp_ch:
        pp_ch_list = pp_ch.split(":")
        if (pp_ch_list and (True if (pp_ch_list[0].replace(".", "", 1).isdigit() and pp_ch_list[1].replace(".", "", 1).isdigit()) else False)):
            pp = float(pp_ch_list[0])
            ch = float(pp_ch_list[1])
            if pp == ch:
                change = "ZERO"
            elif ch < pp:
                change_words = "ERROR"
            elif ch > pp:
                diff = (ch*10 - pp*10)/10 #avoid floating point precision error
                while diff:
                    change,change_word = get_biggest_change(diff)
                    #get key for value chage
                    #change_words = [key for key,value in register.items() if value == change][0]
                    change_words = change_words + " " + change_word
                    diff = diff - change
            print(change_words)
        else:
            change_words = "ERROR"
    else:
        print("Invalid format")
        change_words = "ERROR"