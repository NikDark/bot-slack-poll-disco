from chat.messages.chat_msg_functions import send_msg_to_user

from poll import Poll
from slack import WebClient


def check_top_arguments(poll: Poll, request_form: dict) -> int:
    """
    Check the argument of /poptop command and return the value of song.
    """
    args = request_form.get('text')

    try:
        song_index = int(args)
    except ValueError:
        return 2

    if 1 < song_index < poll.number_of_songs:
        return song_index
    else:
        return 2 

def get_top_songs(num_of_songs: int, all_songs: list) -> list:
    """
    Get num_of_songs top song from all_songs.
    Use bubble sort.
    """
    
    for i in range(len(all_songs)-1):
        for j in range(len(all_songs)-i-1):
            if len(all_songs[j]['voted_users']) < len(all_songs[j+1]['voted_users']):
                all_songs[j], all_songs[j+1] = all_songs[j+1], all_songs[j]

    return all_songs[:num_of_songs]
    

def create_final_top_msg(top_songs: list) -> str:
    """
    Function that create top command response message.
    """
    msg = f"TOP {len(top_songs)} songs\n"

    for song in top_songs:
        msg += f"{song['title']} ---- {len(song['voted_users'])}\n"

    return msg

def start_top(client: WebClient, poll: Poll, request_form: dict):
    """
    Function that is invoked when we run /top command.
    """
    if poll.is_started:
        num_of_songs = check_top_arguments(poll, request_form)
        current_songs = poll.storage.data['songs']
        top_list_songs = get_top_songs(num_of_songs, current_songs)
        msg = create_final_top_msg(top_list_songs)
        send_msg_to_user(client, request_form, msg)
    else:
        send_msg_to_user(client, request_form, 'To invoke /top, the poll needs to be started.')