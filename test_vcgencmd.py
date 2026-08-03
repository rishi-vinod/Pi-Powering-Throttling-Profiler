import subprocess

def runvcgencmd(command):
    if ("measure_temp" == command):
        return (subprocess.run(["vcgencmd","measure_temp"], capture_output = True, text = True)).stdout[5:9]
    elif ("measure_volts" == command):
        return (subprocess.run(["vcgencmd","measure_volts"], capture_output = True, text = True)).stdout[5:].strip("V\n")
    elif ("get_throttled" == command):
        return (subprocess.run(["vcgencmd","get_throttled"], capture_output = True, text = True)).stdout[10:].strip("\n")
    elif ("measure_clock" == command):
        return (subprocess.run(["vcgencmd","measure_clock", "arm"], capture_output = True, text = True)).stdout[13:].strip("\n")

print(runvcgencmd("measure_temp"))