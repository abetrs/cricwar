import pandas as pd
import json
import os
from pathlib import Path
from tqdm.auto import tqdm
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def process_delivery(delivery, match_info, innings_num, batting_team, over_num):
    """Process a single delivery and combine it with match information."""
    try:
        return {
            'match_id': match_info['match_type_number'],
            'team1': match_info['teams'][0],
            'team2': match_info['teams'][1],
            'venue': match_info['venue'],
            'date': match_info['dates'][0],
            'winner': match_info['outcome'].get('winner', None),
            'innings': innings_num,
            'batting_team': batting_team,
            'over_number': over_num,
            'batter': delivery['batter'],
            'bowler': delivery['bowler'],
            'non_striker': delivery['non_striker'],
            'runs_batter': delivery['runs']['batter'],
            'runs_extras': delivery['runs'].get('extras', 0),
            'runs_total': delivery['runs']['total'],
            'extras_type': list(delivery['extras'].keys())[0] if 'extras' in delivery and delivery['extras'] else None,
            'player_out': delivery.get('wicket', {}).get('player_out', None),
            'dismissal_kind': delivery.get('wicket', {}).get('kind', None),
            'fielders': ','.join(f['name'] for f in delivery.get('wicket', {}).get('fielders', [])) if 'wicket' in delivery and 'fielders' in delivery['wicket'] else None
        }
    except Exception as e:
        logger.error(f"Error processing delivery: {str(e)}")
        return None

def process_match(file_path):
    """Process a single match file and return its deliveries."""
    try:
        # Log file processing
        filename = os.path.basename(file_path)
        logger.info(f"Processing: {filename}")
        
        # Read and parse the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            match_data = json.load(f)
            
        if 'info' not in match_data or 'innings' not in match_data:
            logger.error(f"Missing required fields in {filename}")
            return []
            
        match_info = match_data['info']
        deliveries = []
        
        # Process each innings
        for innings_num, innings in enumerate(match_data['innings'], 1):
            batting_team = innings['team']
            
            # Process each over
            for over in innings['overs']:
                over_num = over['over']
                
                # Process each delivery
                for delivery in over['deliveries']:
                    delivery_data = process_delivery(
                        delivery,
                        match_info,
                        innings_num,
                        batting_team,
                        over_num
                    )
                    if delivery_data:  # Only append if we got valid data
                        deliveries.append(delivery_data)
                        
        logger.info(f"Completed {filename} with {len(deliveries)} deliveries")
        return deliveries
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")
        return []

def load_match_data(json_dir):
    """
    Load all JSON files from the specified directory and combine them into a single DataFrame.
    Each JSON file represents a single match's ball-by-ball data.
    
    Args:
        json_dir (str): Path to the directory containing JSON match files
        
    Returns:
        pd.DataFrame: DataFrame containing ball-by-ball data from all matches
    """
    # Get list of JSON files
    json_files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith('.json')]
    if not json_files:
        logger.warning(f"No JSON files found in {json_dir}")
        return pd.DataFrame()
        
    logger.info(f"Found {len(json_files)} JSON files")
    
    # Process all files
    all_deliveries = []
    for file_path in tqdm(json_files, desc="Processing matches"):
        deliveries = process_match(file_path)
        all_deliveries.extend(deliveries)
    
    if not all_deliveries:
        logger.warning("No valid match data found")
        return pd.DataFrame()
        
    logger.info(f"Successfully processed {len(all_deliveries)} deliveries")
    
    # Create DataFrame
    df = pd.DataFrame(all_deliveries)
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    logger.info(f"Data loading completed successfully. DataFrame shape: {df.shape}")
    return df 