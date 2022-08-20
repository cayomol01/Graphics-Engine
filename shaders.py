from Memepy import dot
from random import choices

def flat(render, **kwargs):
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    triangleNormal = kwargs["triangle_normal"]
    
    r /= 255
    g /= 255
    b /= 255
    
    if render.active_texture:
        
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w
        
        texture_color = render.active_texture.getColor(tU, tV)
        
        r *= texture_color[0]
        g *= texture_color[1]
        b *= texture_color[2]
        
    intensity = dot(triangleNormal, render.light_direction) * -1
    
    if intensity < 0:
        return (0, 0, 0)
    
    return (r * intensity, g * intensity, b * intensity)

def gourad(render, **kwargs):
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    nA, nB, nC = kwargs["normals"]
    triangleNormal = kwargs["triangle_normal"]
    
    r /= 255
    g /= 255
    b /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]   

    intensity = dot(triangleNormal, render.light_direction) * -1

    if intensity < 0:
        return (0, 0, 0)
    
    return (r * intensity, g * intensity, b * intensity)

def duality(render, **kwargs):
    #Based on gourad
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    nA, nB, nC = kwargs["normals"]
    triangleNormal = kwargs["triangle_normal"]
       
    r /= 255
    g /= 255
    b /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u  / 99 + nB[0] * v  / 99 + nC[0] * w / 99 ,
                      nA[1] * u  / 99 + nB[1] * v  / 99 + nC[1] * w / 99 ,
                      nA[2] * u  / 99 + nB[2] * v  / 99 + nC[2] * w / 99 ]   

    intensity = dot(triangleNormal, render.light_direction) * -1

    if intensity < 0:
        return (0, 0, 0)
    
    return (1 - r * intensity, 1- g * intensity, 1 - b * intensity)

def negative(render, **kwargs):
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    triangleNormal = kwargs["triangle_normal"]
    
    r /= 255
    g /= 255
    b /= 255
    
    if render.active_texture:
        
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w
        
        texture_color = render.active_texture.getColor(tU, tV)
        
        r *= texture_color[0]
        g *= texture_color[1]
        b *= texture_color[2]
        
    intensity = dot(triangleNormal, render.light_direction) * -1
    
    if intensity < 0:
        return (0, 0, 0)
    
    return (1 - r * intensity, 1 - g * intensity, 1 - b * intensity)

def dissolvefade(render, **kwargs):
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    nA, nB, nC = kwargs["normals"]
    triangleNormal = kwargs["triangle_normal"]
       
    r /= 255
    g /= 255
    b /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]   

    intensity = dot(triangleNormal, render.light_direction) * -1
    
    fade = False
    
    if intensity > 0:
        fade = choices([True, False],weights=[(1-intensity)**5,intensity**5])[0]
    
    if intensity < 0 or fade:
        return (0, 0, 0)
    
    return (r * intensity, g * intensity, b * intensity)


def pride(render, **kwargs):
    
    u, v, w = kwargs["bary_coords"]
    b, g, r = kwargs["v_color"]
    tA, tB, tC = kwargs["text_coords"]
    nA, nB, nC = kwargs["normals"]
    triangleNormal = kwargs["triangle_normal"]
       
    r /= 255
    g /= 255
    b /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                      nA[1] * u + nB[1] * v + nC[1] * w,
                      nA[2] * u + nB[2] * v + nC[2] * w]   

    intensity = dot(triangleNormal, render.light_direction) * -1
    
    if intensity < 0:
        return (0 * 0.9, 0 * 0.9, 0 * 0.9)
    elif intensity < 0.1:
        return (0 * 0.9, 0 * 0.9, 1 * 0.9)
    elif intensity < 0.2:
        return (0 * 0.9, 0.5 * 0.9, 1 * 0.9)
    elif intensity < 0.3:
        return (0 * 0.9, 1 * 0.9, 1 * 0.9)
    elif intensity < 0.4:
        return (0 * 0.9, 1 * 0.9, 0.5 * 0.9)
    elif intensity < 0.5:
        return (0.5 * 0.9, 1 * 0.9, 0 * 0.9)
    elif intensity < 0.6:
        return (1 * 0.9, 1 * 0.9, 0 * 0.9)
    elif intensity < 0.7:
        return (1 * 0.9, 0.5 * 0.9, 0 * 0.9)
    elif intensity < 0.8:
        return (1 * 0.9, 0 * 0.9, 0 * 0.9)
    elif intensity < 0.9:
        return (1 * 0.9, 0 * 0.9, 0.5 * 0.9)
    elif intensity < 1:
        return (1 * 0.9, 0 * 0.9, 1 * 0.9)