from flask import Blueprint, jsonify
import json
import random
import os

sports_joke_bp = Blueprint('sports_joke', __name__)

# Load data
def load_football_data():
    with open("data/football/teams.json", 'r') as file:
        teams = json.load(file)
    with open("data/football/players.json", 'r') as file:
        players = json.load(file)
    with open("data/football/matches.json", 'r') as file:
        matches = json.load(file)
    return teams, players, matches

def load_jokes():
    with open("data/jokes.json", 'r') as file:
        jokes = json.load(file)
    return jokes

# Football endpoints
@sports_joke_bp.route('/teams')
def get_all_teams():
    try:
        teams, _, _ = load_football_data()
        return jsonify(teams)
    except FileNotFoundError:
        return jsonify({'error': 'Football data not found'}), 404

@sports_joke_bp.route('/teams/<team_id>')
def get_team(team_id):
    try:
        teams, players, matches = load_football_data()
        
        # Find team
        team = next((t for t in teams if t['id'] == int(team_id)), None)
        if not team:
            return jsonify({'error': 'Team not found'}), 404
        
        # Find team players
        team_players = [p for p in players if p['team_id'] == int(team_id)]
        
        # Find team matches
        team_matches = [m for m in matches if m['home_team_id'] == int(team_id) or m['away_team_id'] == int(team_id)]
        
        response = {
            'team': team,
            'players': team_players,
            'matches': team_matches
        }
        
        return jsonify(response)
    except FileNotFoundError:
        return jsonify({'error': 'Football data not found'}), 404

@sports_joke_bp.route('/players/<player_id>')
def get_player(player_id):
    try:
        teams, players, _ = load_football_data()
        
        # Find player
        player = next((p for p in players if p['id'] == int(player_id)), None)
        if not player:
            return jsonify({'error': 'Player not found'}), 404
        
        # Find player's team
        team = next((t for t in teams if t['id'] == player['team_id']), {})
        
        response = {
            'player': player,
            'team': team
        }
        
        return jsonify(response)
    except FileNotFoundError:
        return jsonify({'error': 'Football data not found'}), 404

# Joke endpoints
@sports_joke_bp.route('/jokes')
def get_all_jokes():
    try:
        jokes = load_jokes()
        return jsonify(jokes)
    except FileNotFoundError:
        return jsonify({'error': 'Jokes not found'}), 404

@sports_joke_bp.route('/jokes/random')
def get_random_joke():
    try:
        jokes = load_jokes()
        random_joke = random.choice(jokes)
        return jsonify(random_joke)
    except FileNotFoundError:
        return jsonify({'error': 'Jokes not found'}), 404

@sports_joke_bp.route('/jokes/<category>')
def get_jokes_by_category(category):
    try:
        jokes = load_jokes()
        category_jokes = [j for j in jokes if j['category'].lower() == category.lower()]
        return jsonify(category_jokes)
    except FileNotFoundError:
        return jsonify({'error': 'Jokes not found'}), 404