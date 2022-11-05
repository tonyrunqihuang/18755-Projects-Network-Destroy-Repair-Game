from runner import Runner
from utils.misc import *


if __name__ == '__main__':
    set_seed()
    args = get_args()
    runner = Runner(args)
    result = runner.run()
