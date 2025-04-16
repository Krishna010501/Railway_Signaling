import argparse
from system_core.train_control.simulator import simulate_train_movement
from system_core.signaling.fault_detector import detect_faults
from system_core.signaling.recovery_checker import detect_recovery

def main():
    parser = argparse.ArgumentParser(description="Railway Signaling CLI")
    parser.add_argument("--mode", choices=["simulate", "predict"], required=True)
    parser.add_argument("--file", type=str, help="Path to log file for prediction")

    args = parser.parse_args()

    if args.mode == "simulate":
        simulate_train_movement()

    elif args.mode == "predict":
        if args.file:
            with open(args.file, 'r') as f:
                lines = f.readlines()
            faults = detect_faults(lines)
            recoveries = detect_recovery(lines)

            print("\n🔍 Prediction Summary")
            print("=" * 60)
            print(f"Total Log Entries        : {len(lines)}")
            print(f"Detected Fault Events    : {len(faults)}")
            print(f"Detected Recovery Events : {len(recoveries)}")

            print("\n⚠️ Fault Events")
            print("-" * 60)
            for f in faults:
                print(f)

            print("\n✅ Recovery Events")
            print("-" * 60)
            for r in recoveries:
                print(r)
        else:
            print("⚠️ Please provide a log file using --file")

if __name__ == "__main__":
    main()
