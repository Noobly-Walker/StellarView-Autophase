# Autophase.EXE
This serves as a tool for developers of [StellarView](https://github.com/Povstalec/StellarView) to rapidly generate phase and halo graphics with ease.

## How to Use - Standalone
1. Download Autophase.EXE, as well as halo_template.png and phases_overlay.png.
2. Drop these three files in a folder of your choosing, preferably an empty one.
3. Run Autophase.EXE. This will create two folders, planet\ and planet_phases\. It will tell you to press Enter to begin generation, but hold off.
4. Add planet textures to the planet\ directory. These should be 32x32 transparent PNGs with an 8x8 graphic in the center.
   - Refer to the planet\ directory of this repo for examples of what planets should look like.
5. Tab back to Autophase.EXE and press Enter. This will combine each of your planet textures with halo_template.png and phases_overlay.png to make a *_phases.png and *.halo_phases.png for each planet.
   - Prefix a planet texture's name with c_ if you want to manually create either *_phases.png or *.halo_phases.png, in case your planet has rings or an odd shape.
6. Move the planet_phases\ directory into your StellarView fork, to src\main\resources\assets\stellarview\textures\environment\

## How to Use - Drop-in Tool
1. Download Autophase.EXE
2. Drop the file into your StellarView fork, into src\main\resources\assets\stellarview\textures\environment\
3. Run Autophase.EXE. It will tell you to press Enter to begin generation, but hold off.
4. Add or modify textures in the planet\ directory as desired.
5. Tab back to Autophase.EXE and press Enter. This will combine each of your planet textures with halo_template.png and phases_overlay.png to make a *_phases.png and *.halo_phases.png for each planet.
   - Prefix a planet texture's name with c_ if you want to manually create either *_phases.png or *.halo_phases.png, in case your planet has rings or an odd shape.
6. Remove Autophase.EXE from your fork before committing or opening a pull request.
   - If you include this executable in a pull request for StellarView, if Povstalec doesn't flog you, I will.
