import pandas as pd
import matplotlib.pyplot as plt

# File paths
deliveries_path = "/Users/adityachaubey/Downloads/archive (1)/deliveries.csv"
matches_path = "/Users/adityachaubey/Downloads/archive (1)/matches.csv"

# Load datasets
deliveries_df = pd.read_csv(deliveries_path)
matches_df = pd.read_csv(matches_path)

# Clean column names
deliveries_df.columns = deliveries_df.columns.str.strip().str.lower()
matches_df.columns = matches_df.columns.str.strip().str.lower()

# Confirm column names
print("Deliveries columns:", deliveries_df.columns.tolist())

# Objective 1: First 5 records
print("\nFirst 5 records:\n", deliveries_df.head())

# Objective 2: Top 5 run scorers
top_batsmen = deliveries_df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Run Scorers:\n", top_batsmen)

# Objective 3: Top 5 wicket takers
dismissals = deliveries_df[deliveries_df["dismissal_kind"].notnull()]
top_bowlers = dismissals.groupby("bowler")["dismissal_kind"].count().sort_values(ascending=False).head(5)
print("\nTop 5 Wicket Takers:\n", top_bowlers)

# Objective 4: Most sixes by team
sixes_by_team = deliveries_df[deliveries_df["batsman_runs"] == 6] \
    .groupby("batting_team")["batsman_runs"].count().sort_values(ascending=False)
print("\nSixes Hit by Teams:\n", sixes_by_team)

# Objective 5: Number of matches played each year
matches_per_year = matches_df["season"].value_counts().sort_index()
print("\nMatches Played Each Year:\n", matches_per_year)



# Top Batsmen
top_batsmen.plot(kind='bar', title='Top 5 Run Scorers', ylabel='Runs', xlabel='Batter', color='skyblue')
plt.tight_layout()
plt.show()

# Top Bowlers
top_bowlers.plot(kind='bar', title='Top 5 Wicket Takers', ylabel='Wickets', xlabel='Bowler', color='orange')
plt.tight_layout()
plt.show()

# Sixes by Team
sixes_by_team.plot(kind='bar', title='Sixes by Team', ylabel='Number of Sixes', xlabel='Team', color='green')
plt.tight_layout()
plt.show()

# Matches per Year
matches_per_year.plot(kind='bar', title='Matches Played per Season', ylabel='Number of Matches', xlabel='Season', color='purple')
plt.tight_layout()
plt.show()


# DONUT CHART: Sixes Percentage by Team
sixes_labels = sixes_by_team.index
sixes_sizes = sixes_by_team.values

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    sixes_sizes, labels=sixes_labels, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4)
)
plt.setp(autotexts, size=10, weight="bold")
plt.title("Sixes Contribution by Team (Donut Chart)")
plt.tight_layout()
plt.show()

# SCATTER PLOT: Runs vs Balls for Top 10 Batters
top_10_batters = deliveries_df.groupby("batter").agg({
    "batsman_runs": "sum",
    "ball": "count"
}).sort_values(by="batsman_runs", ascending=False).head(10).reset_index()

plt.figure(figsize=(8, 6))
plt.scatter(top_10_batters["ball"], top_10_batters["batsman_runs"], color='crimson', s=100, alpha=0.7)
for i in range(len(top_10_batters)):
    plt.text(top_10_batters["ball"][i] + 2, top_10_batters["batsman_runs"][i],
             top_10_batters["batter"][i], fontsize=9)

plt.xlabel("Balls Faced")
plt.ylabel("Total Runs")
plt.title("Runs vs Balls Faced (Top 10 Batters)")
plt.grid(True)
plt.tight_layout()
plt.show()
