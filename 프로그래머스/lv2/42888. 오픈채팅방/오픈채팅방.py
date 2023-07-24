def solution(record):
    op_kor = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    id_nick = dict()
    msg = []
    for re in record:
        op, id, *nick = re.split()
        if nick:
            id_nick[id] = nick.pop()
        if op != "Change":
            msg.append((id, op))
    return [f"{id_nick[id]}님이 {op_kor[op]}" for id, op in msg]