def load_tv_shows(filename):
    tv_shows = []

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 7:
            continue

        title = parts[0].strip()
        seasons_str = parts[1].strip()
        episodes_str = parts[2].strip()
        genre = parts[3].strip()
        firstrelease_str = parts[4].strip()
        lastrelease_str = parts[5].strip()
        network = parts[6].strip()

        try:
            seasons = int(seasons_str)
            episodes = int(episodes_str)
            firstrelease = int(firstrelease_str) if firstrelease_str.isdigit() else firstrelease_str
            lastrelease = int(lastrelease_str) if lastrelease_str.isdigit() else lastrelease_str
        except ValueError:
            continue

        tv_show = {
            "title": title,
            "seasons": seasons,
            "episodes": episodes,
            "genre": genre,
            "first release": firstrelease,
            "last release": lastrelease,
            "network": network
        }
        tv_shows.append(tv_show)

    return tv_shows


def print_menu():
    print("TV Show Recommender")
    print("-----------------")
    print("1. Show all TV shows")
    print("2. Search by genre")
    print("3. Search by year")
    print("4. Search by network")
    print("5. Recommend TV shows")
    print("6. Exit")


def show_all_shows(tv_shows):
    for m in tv_shows:
        print(f"{m['title']} - seasons: ({m['seasons']}) - episodes: {m['episodes']} - genre: {m['genre']} - first release: {m['first release']} - last release: {m['last release']} - network: {m['network']}")


def search_by_genre(tv_shows):
    g = input("Enter genre: ").strip()
    matched = []

    for m in tv_shows:
        if m["genre"].lower() == g.lower():
            matched.append(m)

    if not matched:
        print("No TV shows found on this genre.")
    else:
        for m in matched:
            print(f"{m['title']} - seasons: ({m['seasons']}) - episodes: {m['episodes']} - first release: {m['first release']} - last release: {m['last release']} - network: {m['network']}")


def search_by_year(tv_shows):
    y_str = input("Enter year: ").strip()

    if not y_str.isdigit():
        print("Please enter a valid year (numbers only).")
        return

    y = int(y_str)

    matched = []
    for m in tv_shows:
        fr = m['first release']
        lr = m['last release']

        # handle “present” or “ongoing” last release
        if isinstance(lr, str) and not lr.isdigit():
            lr = 9999

        if isinstance(fr, str) and not fr.isdigit():
            continue

        if fr <= y <= lr:
            matched.append(m)

    if not matched:
        print("No TV shows found active in that year.")
    else:
        for m in matched:
            print(f"{m['title']} - seasons: {m['seasons']} - episodes: {m['episodes']} - genre: {m['genre']} - network: {m['network']}")


def search_by_network(tv_shows):
    network = input("Enter the network: ").strip()

    matched = []
    for m in tv_shows:
        if network.lower() == m['network'].lower():
            matched.append(m)

    if not matched:
        print("No movies found with on this network.")
    else:
        for m in matched:
            print(f"{m['title']} - seasons: ({m['seasons']}) - episodes: {m['episodes']} - genre: {m['genre']} - first release: {m['first release']} - last release: {m['last release']}")


def recommend_tv_show(tv_shows):
    fav_genre = input("Enter your favourite genre: ").strip().lower()

    matched = []
    for m in tv_shows:
        if m["genre"].lower() == fav_genre:
            matched.append(m)

    if not matched:
        print("No TV show found in that genre. Try another one.")
        return

    # Sort by number of episodes, descending
    sorted_tv_shows = sorted(matched, key=lambda m: m["episodes"], reverse=True)

    print("Top recommendations:")
    for m in sorted_tv_shows[:3]:
        print(
            f"{m['title']} - seasons: {m['seasons']} - episodes: {m['episodes']} "
            f"- first release: {m['first release']} - last release: {m['last release']} "
            f"- network: {m['network']}"
        )


def main():
    tv_shows = load_tv_shows("TVShows.csv")

    if not tv_shows:
        print("No show loaded. Check TVShows.csv.")
        return

    # LOOP until user chooses Exit
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_all_shows(tv_shows)

        elif choice == "2":
            search_by_genre(tv_shows)

        elif choice == "3":
            search_by_year(tv_shows)

        elif choice == "4":
            search_by_network(tv_shows)

        elif choice == "5":
            recommend_tv_show(tv_shows)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")



if __name__ == "__main__":
    main()