import pathlib
import getpass
import re
import lib.pc

class GTA5_LOD_SCALE:
    def __init__(self, pc_score):
        self.pc_score = pc_score
            
    def generate(self):
        score = self.pc_score
        # 0 - 40
        if score < 40:
            return '-0.500000'
         # 40 - 60
        elif score < 60:
            return '-0.360000'
        # 60 - 80
        elif score <= 80:
            return '-0.250000'
        # 80 - 100
        elif score > 80:
            return '0.000000'

class Fix:
    def __init__(self):
        self.path = self.get_settings_path()
        self.settings_content = self.get_settings_content()

        client_pc = lib.pc.PC()

        lod = GTA5_LOD_SCALE(pc_score=client_pc.get_score())

        self.change_game_lod(lod.generate())

        self.save_settings()

        print("\n\nScript executed successfully!\n\n")

    def change_game_lod(self, lod):
        if not self.settings_content:
            return exit("[x] Invalid or empty 'settings.xml' file.")

        new_lod_scale = lod

        print("[!] Decreasing the LOD scale of the game...")
        
        modified_file_content = re.sub(r'LodScale value="(.?)+"', 'LodScale value="' + str(new_lod_scale) + '"', self.settings_content)
        modified_file_content = re.sub(r'LodBias value="(.?)+"', 'LodBias value="'+ str(new_lod_scale) +'"', modified_file_content)
        
        self.settings_content = modified_file_content 


    def get_settings_path(self):
        return pathlib.Path.home().drive + "\\Users\\"+ getpass.getuser() +"\\Documents\\Rockstar Games\\GTA V\\settings.xml"
    
    def get_settings_content(self):
        settings_file = False

        try:
            settings_file = open(self.path, 'r+')
            self.settings_file = settings_file
        except:
            return exit("[x] Error trying to read 'settings.xml' file")

        settings_content = settings_file.read()
        return settings_content
    
    def save_settings(self):
        settings_file = False
        self.settings_file.truncate(0)

        try:
            settings_file = open(self.path, 'w')
        except:
            return exit("[x] Error trying to write in 'settings.xml' file")
    
        settings_file.write(self.settings_content)
        

if __name__ == "__main__":
    print("GTA5 Stuttering Fix - especially for old CPUs")
    print("Version 1.0.0")
    print("https://github.com/br0keh")
    print("\n")


    fix = Fix()
