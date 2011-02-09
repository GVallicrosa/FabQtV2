import os
import shutil

def applyConfig(model, toolDict, advanced = False, options = None):
    ## delete configs
    path = os.path.expanduser('~') + '/.skeinforge/profiles'
    if os.path.exists(path):
        shutil.rmtree(path)
    #########
    # CARVE #
    #########      
    ## edit files
    toolname = model.getModelMaterial()
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
    ########
    # RAFT #
    ########      
    ## edit files
    mod = []
    try:
        fh = open("profiles/extrusion/FAB/raft.csv", "r")
        for line in fh:
            if 'Activate' in line:
                if advanced:
                    line = 'Activate Raft\t' + options.dict['activateRaft'] + '\n' # True
                else:
                    line = 'Activate Raft\t' + 'False' + '\n'
            if advanced:
                if 'Add Raft' in line:
                    line = 'Add Raft, Elevate Nozzle, Orbit and Set Altitude:\t' + options.dict['addRaft'] + '\n'# True
                if 'Base Infill' in line:
                    line = 'Base Infill Density (ratio):\t' + options.dict['baseDensity'] + '\n' # 0.5
                if 'Base Layer Thickness' in line:
                    line = 'Base Layer Thickness over Layer Thickness:\t' + options.dict['baseOver'] + '\n' # 2.0
                if 'Base Layers' in line:
                    line = 'Base Layers (integer):\t' + options.dict['baseLayers'] + '\n' # 1
                if 'Interface Infill' in line:
                    line = 'Interface Infill Density (ratio):\t' + options.dict['interfaceDensity'] + '\n'	# 0.5
                if 'Interface Layer Thickness' in line:
                    line = 'Interface Layer Thickness over Layer Thickness:\t' + options.dict['interfaceOver'] + '\n' # 1.0
                if 'Interface Layers' in line:
                    line = 'Interface Layers (integer):\t' + options.dict['interfaceLayers'] + '\n' # 2
                if 'Raft Margin' in line:
                    line = 'Raft Margin (mm):\t' + options.dict['raftMargin'] + '\n' # 3.0
            mod.append(line)
        fh.close()
    except IOError:
        print "Couldn't open file"
    try:
        fh = open("profiles/extrusion/FAB/raft.csv", "w")
        fh.writelines(mod)
        fh.close()
    except IOError:
        print "Couldn't save file"
    ## copy new configs
    shutil.copytree('profiles', path)
