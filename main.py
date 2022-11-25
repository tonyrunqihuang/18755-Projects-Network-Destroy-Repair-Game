from runner import Runner
from utils.misc import *


if __name__ == '__main__':
    args = get_args()
    set_seed(args.seed)
    runner = Runner(args)
    result = runner.run()
