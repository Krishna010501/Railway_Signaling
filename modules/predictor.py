def run_prediction(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    fault_events = []
    recovery_events = []
    total_lines = len(lines)

    for line in lines:
        if 'Fault:' in line:
            fault_events.append(line.strip())
        elif any(keyword in line for keyword in ['Recovery', 'Recovery Mode', 'Recalibrated', 'Manual Override']):
            recovery_events.append(line.strip())

    print("\n🔍 Prediction Summary")
    print("=" * 60)
    print(f"Total Log Entries        : {total_lines}")
    print(f"Detected Fault Events    : {len(fault_events)}")
    print(f"Detected Recovery Events : {len(recovery_events)}")

    print("\n⚠️ Fault Events")
    print("-" * 60)
    for fault in fault_events:
        print(fault)

    print("\n✅ Recovery Events")
    print("-" * 60)
    for recovery in recovery_events:
        print(recovery)
