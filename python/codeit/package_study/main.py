import youtube_dl

ydl_opt = {
    # 'listformats' : True
    # 다운로드 가능한 포맷 출력
    # 'format' : '18',
    # 18번 포맷 다운
    'format' : 'best[height<=480]',
    # 이런 형식의 포맷도 가능 이건 해상도가 480p 이하인 것중에 가장 높은 해상도 파일 다운 받으라는 것
    # 다양한 파라미터도 사용가능
    'outtmpl' : '%(title)s %(resolution)s.%(ext)s'
    # 파일 명도 정할 수 있음

}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=SPlOfpaY_qc'])
