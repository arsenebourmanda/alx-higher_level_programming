#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if (idx < 0 and idx >(len(my_list)-1)):
            return
        else:
            print("{}".format(my_list[idx]))