# NOTE: Generated By hrp v4.3.0, DO NOT EDIT!

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from debugtalk import *


if __name__ == "__main__":
    import funppy
    funppy.register("return_random_string", return_random_string)
    funppy.register("return_random_phone_number", return_random_phone_number)
    funppy.register("return_random_email", return_random_email)
    funppy.register("return_random_nickname", return_random_nickname)
    funppy.register("setup_hook_dispose", setup_hook_dispose)
    funppy.register("get_user_agent", get_user_agent)
    funppy.register("sleep", sleep)
    funppy.register("sum", sum)
    funppy.register("sum_ints", sum_ints)
    funppy.register("sum_two_int", sum_two_int)
    funppy.register("sum_two_string", sum_two_string)
    funppy.register("sum_strings", sum_strings)
    funppy.register("concatenate", concatenate)
    funppy.register("setup_hook_example", setup_hook_example)
    funppy.register("teardown_hook_example", teardown_hook_example)
    funppy.serve()
