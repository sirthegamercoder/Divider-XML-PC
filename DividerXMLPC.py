import os
import xml.etree.ElementTree as ET
import webbrowser

def main():
    ### USER INPUT FOR FILE PATHS ###
    # INPUT #
    input_file = input("Enter the path to the input XML file : ")
    # OUTPUT #
    output_file = input("Enter the path for the output XML file : ")
    # DIVIDE BY? #
    number = 2
    
    ### CODES ###
    try:
        tree = ET.parse(input_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return
    except ET.ParseError:
        print(f"Error: The file {input_file} is not a valid XML file.")
        return

    for subtexture in tree.iter('SubTexture'):
        x = subtexture.get('x')
        y = subtexture.get('y')
        width = subtexture.get('width')
        height = subtexture.get('height')
        fX = subtexture.get('frameX')
        fY = subtexture.get('frameY')
        fW = subtexture.get('frameWidth')
        fH = subtexture.get('frameHeight')

        if x is not None:
            subtexture.set('x', str(int(x) // number))
        if y is not None:
            subtexture.set('y', str(int(y) // number))
        if width is not None:
            subtexture.set('width', str(int(width) // number))
        if height is not None:
            subtexture.set('height', str(int(height) // number))
        if fX is not None:
            subtexture.set('frameX', str(int(fX) // number))
        if fY is not None:
            subtexture.set('frameY', str(int(fY) // number))
        if fW is not None:
            subtexture.set('frameWidth', str(int(fW) // number))
        if fH is not None:
            subtexture.set('frameHeight', str(int(fH) // number))

    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    if os.path.exists(output_file):
        print("File Converted Successfully!")
        print(f"INPUT='{os.path.abspath(input_file)}'")
        print(f"OUTPUT='{os.path.abspath(output_file)}'")

        ### USER CHOICE FOR REDIRECTION ###
        redirect_choice = input("Do you want to be redirected to ResizePixel? (Y/N): ").strip().lower()
        if redirect_choice == 'Y':
            webbrowser.open('https://www.resizepixel.com/') 
        else:
            print("You chose not to be redirected.")

if __name__ == '__main__':
    print("Divider XML PC")
    main()