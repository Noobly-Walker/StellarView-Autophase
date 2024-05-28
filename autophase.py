import os
from PIL import Image, ImageEnhance

VERSION = "1.1.0"

# Directory paths
planet_directory = 'planet'
phases_overlay_path = 'phases_overlay.png'
halo_template_path = 'halo_template.png'
output_directory = 'planet_phases'

# Create the input and output directories if they don't exist
os.makedirs(planet_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

def process_planet_texture(planet_name, planet_path, phases_overlay, halo_template):
    # Open the planet texture
    planet_texture = Image.open(planet_path).convert("RGBA")
    
    # Extract the 8x8 square from the center
    planet_crop = planet_texture.crop((12, 12, 20, 20))
    
    # Get the average color
    average_color = tuple([int(sum(planet_crop.getdata(band)) / 64) for band in range(3)])
    
    # Lighten the average color by 50%
    lightened_color = tuple(min(255, int(c * 1.5)) for c in average_color)
    
    # Create a new image with the lightened color
    halo_colored = Image.new('RGBA', halo_template.size)
    for y in range(halo_template.size[1]):
        for x in range(halo_template.size[0]):
            r, g, b, a = halo_template.getpixel((x, y))
            halo_colored.putpixel((x, y), (lightened_color[0]//128*r, lightened_color[1]//128*g, lightened_color[2]//128*b, a))
    
    # Tile the planet texture across a 128x64 canvas
    planet_tiled = Image.new('RGBA', (128, 64), (0, 0, 0, 0))
    for x in range(0, 128, 32):
        for y in range(0, 64, 32):
            planet_tiled.paste(planet_texture, (x, y))
    
    # Overlay the phases
    planet_tiled_with_phases = Image.alpha_composite(planet_tiled, phases_overlay)
    
    # Save the result
    planet_tiled_with_phases.save(os.path.join(output_directory, f'{planet_name}_phases.png'))
    
    # Tile the halo across a 128x64 canvas
    halo_tiled = Image.new('RGBA', (128, 64), (0, 0, 0, 0))
    for x in range(0, 128, halo_colored.size[0]):
        for y in range(0, 64, halo_colored.size[1]):
            halo_tiled.paste(halo_colored, (x, y))
    
    # Save the result
    halo_tiled.save(os.path.join(output_directory, f'{planet_name}_halo_phases.png'))

print(f"""Autophase for StellarView, version {VERSION} by Noobly Walker
Written in Python 3.12 using the Python Image Library (PIL)

This tool iterates through the planet directory, combining each planet's texture with phases_overlay.png and halo_template.png to quickly and easily generate phase graphics for planets.
If you want to create custom halos and phases for your planet, please rename your planet's texture such that it begins with c_ (i.e. 'c_vesta.png').
Planets that don't start with c_ in the file names will have any existing phase or halo textures OVERWRITTEN. The old versions will NOT be recoverable!
Make backups of custom textures if you're worried about messing someting up.
""")

input("""Press ENTER to begin generating phases.
""")

# Load the overlay and halo template images
phases_overlay = Image.open(phases_overlay_path).convert('RGBA')
halo_template = Image.open(halo_template_path).convert('RGBA')

while True:

    # Process each planet texture in the planet directory
    for filename in os.listdir(planet_directory):
        if filename.endswith('.png') and not filename.startswith('c_'):
            print(f"Autophasing {filename}!")
            planet_name = filename.split('.')[0]
            planet_path = os.path.join(planet_directory, filename)
            process_planet_texture(planet_name, planet_path, phases_overlay, halo_template)
        elif filename.startswith('c_'): print(f"Skipped {filename}: marked as custom...")

    input("""
Autophase process complete. Feel free to close this program, or press ENTER to rerun Autophase.
""")
