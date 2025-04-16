def detect_faults(lines):
    faults = []
    for line in lines:
        if 'Fault:' in line:
            faults.append(line.strip())
    return faults
