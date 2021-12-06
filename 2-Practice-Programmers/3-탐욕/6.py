# [단속카메라] 필요한 카메라의 최소대수 (탐욕)

def solution(routes):
    camera = []

    # (탐욕) 최소로 하기 위해 진출 지점에 카메라를 세운다
    routes.sort(key=lambda x: x[1])

    for s, e in routes:
        if not camera or camera[-1] < s:
            camera.append(e)

    return len(camera)


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
