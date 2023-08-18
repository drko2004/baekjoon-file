def solution(id_pw, db):
    is_id_match = False
    id = id_pw[0]
    pw = id_pw[1]
    for i in db:
        if id == i[0]:
            is_id_match = True
            if pw == i[1]:
                return "login"
    if is_id_match:
        return "wrong pw"
    return "fail"