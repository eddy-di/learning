import subprocess
# need to watch last video to get more understanding
result = subprocess.run(["dir", "/D/python/Works"])
print(type(result))