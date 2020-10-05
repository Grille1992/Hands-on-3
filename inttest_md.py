import md
import os, sys

if os.path.isfile('cu.traj'):
    os.unlink('cu.traj')

md.run_md()

if os.path.isfile('cu.traj'):
    raise Exception('Cu.traj missing')
