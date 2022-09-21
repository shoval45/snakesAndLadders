import pygame

import Screen
import board_grid
import consts
import player

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "num of mistakes": 0,
    "player_location": [6, 0]
}

grid = board_grid.returned_initialized_grid()

def main():
    pygame.init()
    main_player = player.player()

    while state["is_window_open"]:
        handle_user_events(main_player)

        if is_lose():
            state["state"] = consts.LOSE_STATE
            state["is_window_open"] = False

        elif is_win():
            state["state"] = consts.WIN_STATE
            state["is_window_open"] = False

        Screen.draw_game(state)


def handle_user_events(main_player):
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if keys_pressed[pygame.K_RETURN]:
            main_player.x

        # need randomized and present question if question not presented in 3 times




def compare_lists_locations(list1, list2):
    if list1[0] == list2[0]:
        if list1[1] == list2[2]:
            return True
    return False

def is_lose():
    if state["num of mistakes"] >= 3:
        return True
    return False

def is_win():
    win_location_in_grid = [0, 6]
    if compare_lists_locations(state["player_location"], win_location_in_grid):
        return True
    return False

if __name__ == '__main__':
    main()