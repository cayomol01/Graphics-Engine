from Memepy import dot

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
        
    direct_light = render.light_direction
    intensity = dot(triangleNormal, direct_light) * -1
    
    r *= intensity
    g *= intensity
    b *= intensity
    
    if intensity > 0:
        return r,g,b
    else:
        return 0,0,0