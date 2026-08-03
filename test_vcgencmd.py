import subprocess

result = subprocess.run(["vcgencmd","measure_temp"], capture_output = True, text = True)

temp = float(result.stdout[5:9])

print(result)
print(temp)
