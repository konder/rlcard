from rlcard.utils import elegent_form_card, elegent_form_cards
from tabulate import tabulate


def print_trajectories(trajectories_humanization, payoffs):
    data = {'玩家': [], '位置': [], '初始筹码': [], '手牌': []}

    '''
    解析每个玩家ID、位置、手牌、初始筹码
    '''
    players = trajectories_humanization['players_info']
    for player_id, player in enumerate(players):
        data['玩家'].append(f'玩家{player_id + 1}')
        data['位置'].append(player.position)
        data['手牌'].append(f'{elegent_form_card(player.hand[0])} {elegent_form_card(player.hand[1])}')
        data['初始筹码'].append(100)

    for stage, actions in trajectories_humanization['actions'].items():
        stage_key = f"{stage}({elegent_form_cards(actions['public_cards'])})"
        data[stage_key] = ['' for _ in players]
        for i, action in enumerate(actions['player_actions']):
            for player in players:
                data[stage_key][
                    player.player_id] += f'{i + 1}:{action["action"]} ({action['in_chips']})' if player.player_id == \
                                                                                                 action[
                                                                                                     'player_id'] else ','
    data[f"SD({elegent_form_cards(trajectories_humanization['final']['public_cards'])})"] = []
    data['结算'] = payoffs

    print(tabulate(data, headers='keys', tablefmt='simple'))
