from copy import deepcopy

from rlcard.games.nolimitholdem import Action

class Trajectory:
    trajectory = None

    def __init__(self):
        self.trajectory = {
            'players_info': [],
            'actions': {}
        }

    def set_players_info(self, players):
        self.trajectory['players_info'] = deepcopy(players)

    def add_blind_action(self, s_player, b_player):
        self.add_action_to_stage('PREFLOP', [], s_player, Action.SMALL_BLIND.value)
        self.add_action_to_stage('PREFLOP', [], b_player, Action.BIG_BLIND.value)

    def add_final(self, public_cards, players):
        self.trajectory['final'] = {
            'public_cards': deepcopy(public_cards),
        }

    def add_action_to_stage(self, stage, public_cards, player, action):
        if stage not in self.trajectory['actions']:
            self.trajectory['actions'][deepcopy(stage)] = {
                'public_cards': deepcopy(public_cards),
                'player_actions': []
            }

        self.trajectory['actions'][stage]['player_actions'].append({
            'player_id': player.player_id,
            'position': player.position,
            'action': Action.value_of(action).name,
            'status': player.status,
            'in_chips': int(player.in_chips),
            'remained_chips': int(player.remained_chips)
        })