from bbb_processing import load_match_data
import os

# Path to the JSON files
TESTS_JSON_PATH = os.path.join("Tests", "tests_json")

def main():
    # Load and process the match data
    df = load_match_data(TESTS_JSON_PATH)
    
    # Display info about the loaded data
    if not df.empty:
        print("\nDataset Info:")
        print(f"Number of matches: {df['match_id'].nunique()}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        print(f"\nTotal deliveries: {len(df)}")
        print(f"Total innings: {df['innings'].nunique()}")
        
        print("\nTeams in dataset:")
        all_teams = sorted(set(df['team1'].unique()) | set(df['team2'].unique()))
        for team in all_teams:
            print(f"- {team}")
        
        print("\nBasic Statistics:")
        print(f"Average runs per ball: {df['runs_total'].mean():.2f}")
        print(f"Total wickets: {df['player_out'].notna().sum()}")
        print(f"Total extras: {df['extras_type'].notna().sum()}")
    else:
        print("\nNo data loaded. Please check the JSON files in the tests_json directory.")

if __name__ == "__main__":
    main() 