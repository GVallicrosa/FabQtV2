import os
import shutil

def applyConfig(model, toolDict):
    ## delete configs
    path = os.path.expanduser('~') + '/.skeinforge/profiles'
    if os.path.exists(path):
        shutil.rmtree(path)      
    ## edit files
    toolname = model.readModelMaterial()
    tool = toolDict[str(toolname)]
    mod = []
    try:
        fh = open("profiles/extrusion/FAB/carve.csv", "r")
        for line in fh:
            if 'Thickness' in line:
                line = 'Layer Thickness (mm):\t' + tool.pathHeight + '\n'
            mod.append(line)
        fh.close()
    except IOError:
        print "Couldn't open file"
    try:
        fh = open("profiles/extrusion/FAB/carve.csv", "w")
        fh.writelines(mod)
        fh.close()
    except IOError:
        print "Couldn't save file"
    ## copy
    shutil.copytree('profiles', path)
