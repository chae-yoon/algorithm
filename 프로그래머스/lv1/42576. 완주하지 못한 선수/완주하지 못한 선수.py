def solution(participant, completion):
    answer = ''
    participant_dict = {}
    completion_dict = {}
    
    for people in participant:
        participant_dict[people] = participant_dict.get(people, 0) + 1
    for people in completion:
        completion_dict[people] = completion_dict.get(people, 0) + 1
    
    for people in participant_dict:
        if participant_dict.get(people, 0) -completion_dict.get(people, 0) == 1:
            answer = people
            
    return answer