def solution(dots):
    answer = 0
    
    widths = []
    heights = []
    
    for dot in dots:
        widths.append(dot[0])
        heights.append(dot[1])
    
    widths = list(set(widths))
    heights = list(set(heights))
    
    width = abs(widths[0]-widths[1])
    height = abs(heights[0]-heights[1])
    
    answer = width*height
    
    return answer