# main.py
import sys
import sdl2
import sdl2.ext
import time

def framebuffer_res():
    try:
        with open("/sys/class/graphics/fb0/virtual_size", "r") as f:
            w, h = map(int, f.read().strip().split(","))
            return w, h
    except Exception as error:
        print(f"Failed to fetch display resolution: {error}")
        return 640, 480  # fallback

sdl2.ext.init()
# window = sdl2.ext.Window("Quartz Compositor ( Amethyine )", size=(1280, 720))
# window = sdl2.ext.Window("Quartz Compositor ( Amethyine )", size=(1600, 900))
window = sdl2.ext.Window("QuartzOS Splash", size=(framebuffer_res()[0], framebuffer_res()[1]))
sdl2.SDL_SetWindowFullscreen(window.window, sdl2.SDL_WINDOW_FULLSCREEN)

window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
renderer = factory.create_sprite_render_system(window)

background = factory.create_sprite(size=(window.size))
sdl2.ext.fill(background, (0, 0, 0))

# wallpapers_path = sdl2.ext.Resources(__file__, "../resources/wallpapers")
logo_image = factory.from_image('logo.png')

logo = factory.create_sprite(size=(300, 300))
sdl2.SDL_SetSurfaceBlendMode(logo.surface, sdl2.SDL_BLENDMODE_BLEND)

sdl2.surface.SDL_BlitScaled(logo_image.surface, None, logo.surface, None)

logo_opacity = 0

# satoshi = sdl2.sdlttf.TTF_OpenFont("Satoshi-Regular.ttf".encode("utf-8"), 20)

# title = sdl2.sdlttf.TTF_RenderUTF8_Blended(satoshi, 'QuartzOS'.encode("utf-8"),
# 	sdl2.SDL_Color(255, 0, 0, 255)
# )

# title_surface = sdl2.SDL_Rect(15, 7, 0, 0)

# sdl2.surface.SDL_BlitScaled(title.surface, None, title_surface.surface, None)

# sdl2.SDL_BlitSurface(window_title_text, None, window_surface, window_title_surface)

def run():
	global logo_opacity
	running = True
	while running:
		for event in sdl2.ext.get_events():
			if event.type == sdl2.SDL_QUIT:
				running = False
				break	

		logo_x = int((window.size[0] - logo.size[0]) / 2)
		logo_y = int((window.size[1] - logo.size[1]) / 2)
		# renderer.render(background);
		if logo_opacity != 255:
			# time.sleep(0.02)
			logo_opacity += 0.4

		sdl2.SDL_SetSurfaceAlphaMod(logo.surface, int(logo_opacity))

		renderer.render(logo, logo_x, logo_y)

		sdl2.SDL_Delay(16);

	sdl2.ext.quit()
	return 0

if __name__ == "__main__":
	sys.exit(run())
