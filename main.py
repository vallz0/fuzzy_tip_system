from fuzzy_logic import FuzzyTipSystem

def main() -> None:
    fuzzy_system = FuzzyTipSystem()
    quality = 8.5
    service = 6.5

    calculated_tip = fuzzy_system.compute_tip(quality, service)
    print(f"Calculated tip: {calculated_tip:.2f}")

    fuzzy_system.save_tip_graph()
    print("Graphs saved in the 'Images' folder.")


if __name__ == "__main__":
    main()
