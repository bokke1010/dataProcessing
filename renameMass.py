import base, os.path

# TODO: Mass convert format from yyyy-m.json to yyyy-mm.json
path = base.getPath()
inp = ["-1.","-2.","-3.","-4.","-5.","-6.","-7.","-8.","-9."]
outp = ["-01.","-02.","-03.","-04.","-05.","-06.","-07.","-08.","-09."]
for filename in os.listdir(path):
    newName = filename
    for i in range(len(inp)):
        newName = newName.replace(inp[i],outp[i])
    print(filename + " ; " + newName)
    os.rename(os.path.join(path, filename),os.path.join(path,newName) )
