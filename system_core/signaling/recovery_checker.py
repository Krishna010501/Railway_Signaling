def detect_recovery(lines):
    recovery_keywords = ['Recovery', 'Recovery Mode', 'Recalibrated', 'Manual Override']
    recoveries = []
    for line in lines:
        if any(word in line for word in recovery_keywords):
            recoveries.append(line.strip())
    return recoveries
