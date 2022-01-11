'''
    알고리즘:
    1. 문자열로 그냥 구현만 잘하면 되는듯. 
    (#을 다루는 게 어려웠는데, 다른 사람 아이디어 얻어서, replace로 C#, D#, F#, G#은 소문자로 바꾸는 풀이 참고함)
'''
def solution(m, musicinfos):
    answer = ''
    
    music = []
    for i in range(len(musicinfos)):
        info = list(map(str, musicinfos[i].split(",")))
        # print(info)
    
        s_h, s_m = map(int, info[0].split(':'))
        e_h, e_m = map(int, info[1].split(':'))
        dur = (e_h - s_h) * 60 + (e_m - s_m)
        # print(dur)
        
        um = []
        melody = info[3]
        for j in range(len(melody)):
            if melody[j] == '#':
                continue
                
            if j+1 != len(melody) and melody[j+1] == '#':
                temp = melody[j] + melody[j+1]
                um.append(temp)
            else:
                um.append(melody[j])      
        # print(um)

        mok = dur // len(um)
        namuji = dur % len(um)
       
        str_mel = (''.join(um)) * mok
        for k in range(namuji):
            str_mel += um[k]
            
        str_mel = str_mel.replace("C#", "c")
        str_mel = str_mel.replace("D#", "d")
        str_mel = str_mel.replace("F#", "f")
        str_mel = str_mel.replace("G#", "g")

        m = m.replace("C#", "c")
        m = m.replace("D#", "d")
        m = m.replace("F#", "f")
        m = m.replace("G#", "g")
        
        if m in str_mel:
            music.append((i, dur, info[2]))            
            
    # print(music)
    
    if len(music) == 1:
        answer = music[0][2]
    elif len(music) > 1:
        music.sort(key = lambda x:(-x[1], x[0]))
        answer = music[0][2]
    else:
        answer = "(None)"
        
    return str(answer)
