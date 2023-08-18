func solution(id_pw []string, db [][]string) string {
    isIdMatch := false
    for _, e := range db {
        if id_pw[0] == e[0] {
            isIdMatch = true
            if id_pw[1] == e[1] {
                return "login"
            }
        }
    }
    if isIdMatch {
        return "wrong pw"
    }
    return "fail"
}