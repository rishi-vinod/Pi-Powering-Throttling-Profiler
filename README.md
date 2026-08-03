# Pi-Powering-Throttling-Profiler
## Progress Log — Day 1

Built a helper function, `runvcgencmd()`, that wraps the Pi's built-in
`vcgencmd` utility using Python's `subprocess` module. Given a command name
(`measure_temp`, `measure_volts`, `measure_clock`, or `get_throttled`), it
runs the corresponding `vcgencmd` call, captures its raw text output, and
parses out the clean value:

- `measure_temp` → core temperature in °C
- `measure_volts` → core voltage in V
- `measure_clock` → ARM core clock frequency in Hz
- `get_throttled` → hex status code indicating undervoltage/throttling flags

This required working through:
- Using `subprocess.run()` with `capture_output=True` and `text=True` to
  call an external Linux command from Python and get its output back as a
  string.
- Parsing inconsistent string formats from each command (fixed-width
  slicing vs. `.strip()` to remove trailing units/newlines).
- Setting up a Python virtual environment (`venv`) on the Pi to keep
  project dependencies isolated from system Python.