# app.py - super simple invasive species list (starter)
#import json
#
#with open('InvasiveSpeciesapp/species.json','r') as file:
#    SPECIES = json.load(file)

SPECIES = [
    {
        "name_en": "Mimosa (Silver Wattle)",
        "name_pt": "Acácia-dealbata (Mimosa)",
        "scientific": "Acacia dealbata",
        "districts": ["Lisboa"],
        "action": "REPORT",
        "summary": "Fast-growing invasive tree that outcompetes native vegetation."
    },
    {
        "name_en": "Ice plant",
        "name_pt": "Chorão-das-praias",
        "scientific": "Carpobrotus edulis",
        "districts": ["Portugal-wide"],
        "action": "REMOVE (private land) / REPORT (public land)",
        "summary": "Spreads quickly and smothers native dune plants."
    }
]

def species_for_district(district: str):
    results = []
    for s in SPECIES:
        if "Portugal-wide" in s["districts"] or district in s["districts"]:
            results.append(s)
    return results

def main():
    print("Invasive plants near you")
    district = input("Enter district (default Lisboa): ").strip()
    #district = "Lisboa"
    if district == "":
        district = "Lisboa"

    results = species_for_district(district)

    print("\nResults:")
    if len(results) == 0:
        print("No species found (this is just starter sample data).")
        return

    for i, s in enumerate(results, start=1):
        print(f"\n{i}. {s['name_en']} ({s['scientific']})")
        print(f"   PT: {s['name_pt']}")
        print(f"   Action: {s['action']}")
        print(f"   Summary: {s['summary']}")

if __name__ == "__main__":
    main()